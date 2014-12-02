from django.db import models


class AxisManager(models.Manager):

    def get_random_axis(self):
        # TODO: filter by cleared status (i.e. not all contributors cleared)
        # TODO: verify that a contributor with the given language exists
        return self.order_by('?').first()


class ContributorManager(models.Manager):

    def get_random_contributor(self):
        # TODO: filter by cleared status (i.e. all contributors cleared)
        # TODO: verify that a contributor with the given language exists
        return self.order_by('?').first()
