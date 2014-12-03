from django.db import models


class AxisManager(models.Manager):

    def get_random_axis(self):
        from .models import Contributor
        # TODO: verify that a contributor with the given language exists
        axis = self.order_by('?').first()
        while axis.is_fully_qualified:
            axis = self.order_by('?').first()
        return axis


class ContributorManager(models.Manager):

    def get_random_contributor(self):
        from .models import Contributor
        # TODO: verify that a contributor with the given language exists
        return self.filter(status__lt=Contributor.STATUS_QUALIFIED).order_by('?').first()
