# encoding: utf-8
from os.path import join
from os import walk
import re
import subprocess
from StringIO import StringIO

import requests

from django.core.management.base import BaseCommand
from django.core.files import File

from rest_framework.parsers import JSONParser

from positions.serializers import ContributorSerializer
from positions.models import Contributor


lobbying_section = {
    'I - Professional consultancies/law firms/self-employed consultants': 'Business',
    'II - In-house lobbyists and trade/professional associations': 'Business',
    'III - Non-governmental organisations': 'Civil society',
    'IV - Think tanks, research and academic institutions': 'Civil society',
    'V - Organisations representing churches and religious communities': 'Civil society',
    'VI - Organisations representing local, regional and municipal authorities, other public or mixed entities, etc.':'Government',
}

lobbying_subsection = {
    'Professional consultancies': 'Consultancy',
    'Law firms': 'Law firms',
    'Self-employed consultants': 'Consultancy',
    'Companies & groups': 'Company',
    'Trade, business & professional associations': 'Business association',
    'Trade unions': 'Trade union',
    'Other similar organisations': 'Business association',
    'Non-governmental organisations, platforms and networks and similar': 'NGO',
    'Think tanks and research institutions': 'Think tanks and research institutions',
    'Academic institutions': 'Academic institutions',
    'Organisations representing churches and religious communities': 'Church',
    'Local, regional and municipal authorities (at sub-national level)': 'Local authority',
    'Other public or mixed entities, etc.': 'Public entity',
}

re_id = re.compile(r'([0-9]{10,12}-[0-9]{2})')


def id_from_pdf(f):
    proc = subprocess.Popen(
        ["pdftotext %s -" % f, ],
        stdout=subprocess.PIPE,
        shell=True
    )
    (out, err) = proc.communicate()
    matches = re_id.search(out)
    if matches:
        return matches.groups(1)
    else:
        return None


def get_data(original_id):
    url = "https://api.morph.io/cirotix/eu_lobbyists_register/data.json"
    payload = {
        'key': '0TVT6O82E5ZLNutfXf3Z',
        'query': "select * from 'data' where id='%s'" % original_id
    }
    r = requests.get(url, params=payload, verify=False)
    try:
        return r.json()
    except ValueError:
        return None


class Command(BaseCommand):
    args = '<root_directory>'
    def handle(self, *args, **options):

        for root_path in args:
            for root, dirs, files in walk(root_path):
                for name in files:
                    status = Contributor.STATUS_FILE
                    matches = re.search('(pdf|doc|docx|odt|rtf)', name)
                    file_path = join(root, name)
                    print "\n"
                    print file_path

                    if 'pdf' in matches.groups(1):
                        original_id = id_from_pdf(file_path)


                        if original_id:
                            status = Contributor.STATUS_ID
                            try:
                                data = get_data(original_id)[0]
                                serializer = ContributorSerializer(data=data)
                                serializer.is_valid()
                                status = Contributor.STATUS_DATA
                                contributor = serializer.save()
                            except IndexError:
                                contributor = Contributor()

                            contributor.original_id = original_id[0]
                        else:
                            contributor = Contributor()

                        # file
                        f = open(file_path)
                        contribution_file = File(f)
                        filefield = contributor.contribution_file
                        filefield.save(
                            "contribution.pdf",
                            contribution_file
                        )

                        # language_code
                        matches = re.search(r'(_|-)([a-zA-Z]{2})-*\.pdf', name)
                        if matches:
                            contributor.language_code = matches.groups()[1]

                        # mapping of EU categories into our own
                        try:
                            contributor.org_type = lobbying_section[contributor.lobbying_section]
                        except KeyError:
                            pass
                        try:
                            contributor.org_subtype = lobbying_subsection[contributor.lobbying_subsection]
                        except KeyError:
                            pass


                        contributor.status = status
                        contributor.save()
