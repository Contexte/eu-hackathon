from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models


class ContributorsList(ListView):

    model = models.Contributor


class ContributorDetail(DetailView):

    model = models.Contributor
