from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Point(models.Model):

    x = models.FloatField(_("X"))
    y = models.FloatField(_("Y"))
    pid = models.IntegerField(_("Point ID"))

    class Meta:
        verbose_name = _("point")
        verbose_name_plural = _("points")

    def __str__(self):
        return self.pid

    def get_absolute_url(self):
        return reverse("point_detail", kwargs={"pk": self.pk})


class History(models.Model):

    x = models.FloatField(_("X"))
    y = models.FloatField(_("Y"))
    n = models.IntegerField(_("Number of points"))
    operation_type = models.IntegerField(choices=((1, _("Nearest")),
                                        (2, _("Furthest"))),
                                default=1)

    class Meta:
        verbose_name = _("history")
        verbose_name_plural = _("historys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("history_detail", kwargs={"pk": self.pk})
