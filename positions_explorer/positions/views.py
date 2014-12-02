from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from . import models
from . import forms


class Home(TemplateView):

    template_name = 'positions/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['total_positions'] = models.Contributor.objects.all().count()
        # FIXME: filter by state below
        context['total_processed_positions'] = models.Contributor.objects.filter().count()
        context['processed_percentage'] = (context['total_processed_positions'] / context['total_positions']) * 100
        return context


class AxisDetail(DetailView):

    model = models.Axis

    def post(self, request, *args, **kwargs):
        form = forms.AxisValuesForm(
            data=request.POST, axis=self.get_object(),
            contributor_pk=request.POST['contributor'][0]
        )
        if form.is_valid():
            contributor = form.cleaned_data['contributor']
            contributor.contribution_values.add(*form.cleaned_data['values'])
            contributor.save()

    def get_object(self):
        if self.kwargs.get('pk'):
            return super(AxisDetail, self).get_object()
        return models.Axis.objects.get_random_axis()

    def get_context_data(self, **kwargs):
        context = super(AxisDetail, self).get_context_data(**kwargs)
        context['contributor'] = models.Contributor.objects.get_random_contributor()
        context['form'] = forms.AxisValuesForm(axis=self.object, contributor_pk=context['contributor'].pk)
        return context
