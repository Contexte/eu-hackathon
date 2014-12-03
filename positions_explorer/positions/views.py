from string import split
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.utils.translation.trans_real import parse_accept_lang_header

from . import models
from . import forms


class Home(TemplateView):

    template_name = 'positions/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['total_positions'] = models.Contributor.objects.all().count()
        context['total_processed_positions'] = models.Contributor.objects.filter(
            status=models.Contributor.STATUS_QUALIFIED
        ).count()
        try:
            context['processed_percentage'] = (context['total_processed_positions'] / context['total_positions']) * 100
        except ZeroDivisionError:
            context['processed_percentage'] = 0
        return context


class AxisDetail(DetailView):

    model = models.Axis

    def get_languages_codes_from_request(self):
        return [
            lang[0] for lang
            in parse_accept_lang_header(self.request.META.get('HTTP_ACCEPT_LANGUAGE', ''))
        ]

    def post(self, request, *args, **kwargs):
        form = forms.AxisValuesForm(
            data=request.POST, axis=self.get_object(),
            contributor_pk=request.POST['contributor']
        )
        if form.is_valid():
            contributor = form.cleaned_data['contributor']
            contributor.contribution_values.add(*form.cleaned_data['values'])
            contributor.status = contributor.STATUS_QUALIFIED
            contributor.save()
        return HttpResponseRedirect(reverse('random-axis'))

    def get_object(self):
        if self.kwargs.get('pk'):
            return super(AxisDetail, self).get_object()
        return models.Axis.objects.get_random_axis(languages=self.get_languages_codes_from_request())

    def get_context_data(self, **kwargs):
        context = super(AxisDetail, self).get_context_data(**kwargs)
        context['contributor'] = models.Contributor.objects.get_random_contributor(
            languages=self.get_languages_codes_from_request()
        )
        context['contributor'] = models.Contributor.objects.get(pk=493)
        print context['contributor']
        import pprint; pprint.pprint(vars(context['contributor']))
        context['contributor'].members = ', '.join(split(context['contributor'].org_members, ';'))
        if context['contributor']:
            context['form'] = forms.AxisValuesForm(axis=self.object, contributor_pk=context['contributor'].pk)
        return context

class AxisResults(DetailView):

    model = models.Axis
    template_name = 'positions/axis_results.html'

    def get_context_data(self, **kwargs):
        context = super(AxisResults, self).get_context_data(**kwargs)
        contributors = models.Contributor.objects.get_by_axis(self.object)
        organisations_types = contributors.values_list('org_type', flat=True).distinct()
        data = {}
        context['organisations_types'] = data
        for organisation_type in organisations_types:
            subtypes = contributors.filter(org_type=organisation_type).values_list('org_subtype', flat=True).distinct()
            data[organisation_type] = []
            for subtype in subtypes:
                data[organisation_type].append({
                    'subtype': subtype,
                    'positions': contributors.filter(org_type=organisation_type, org_subtype=subtype),
                    'values': [],
                })
                for value in self.get_object().values.values_list('value', flat=True):
                    data[organisation_type][-1]['values'].append({
                        value: data[organisation_type][-1]['positions'].filter(contribution_values__value=value).count()
                    })

        return context
