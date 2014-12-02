from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models


class ContributorsList(ListView):

    model = models.Contributor


class AxisDetail(DetailView):

    model = models.Axis

    def get_object(self):
        if self.kwargs.get('pk'):
            return super(AxisDetail, self).get_object()
        return models.Axis.objects.get_random_axis()
