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
        status = Contributor.STATUS_FILE

        for root_path in args:
            for root, dirs, files in walk(root_path):
                for name in files:
                    matches = re.search('(pdf|doc|docx|odt|rtf)', name)
                    file_path = join(root, name)
                    print file_path
                    if 'pdf' in matches.groups(1):
                        original_id = id_from_pdf(file_path)
                        if original_id:
                            status = Contributor.STATUS_ID
                            data = get_data(original_id)
                            try:
                                print (data[0]['goals'])
                                serializer = ContributorSerializer(data=data[0])
                                serializer.is_valid()
                                status = Contributor.STATUS_DATA
                                contributor = serializer.save()
                            except IndexError:
                                contributor = Contributor()

                            contributor.original_id = original_id[0]

                        f = open(file_path)
                        contribution_file = File(f)
                        filefield = contributor.contribution_file
                        filefield.save("contribution.pdf", contribution_file)
                        print "STATUS >> %s" % status

                        contributor.status = status
                        contributor.save()
