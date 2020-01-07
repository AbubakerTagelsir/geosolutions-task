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

class Result(models.Model):

    number_points = models.IntegerField(_("NO. Points"))
    points_list = models.CharField(_("Points List"), max_length=50)

    class Meta:
        verbose_name = _("result")
        verbose_name_plural = _("results")

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("result_detail", kwargs={"pk": self.pk})


class History(models.Model):

    x = models.FloatField(_("X"))
    y = models.FloatField(_("Y"))
    n = models.IntegerField(_("Number of points"))
    operation_type = models.IntegerField(choices=((1, _("Nearest")),
                                        (2, _("Furthest"))),
                                default=1)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("history")
        verbose_name_plural = _("historys")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("history_detail", kwargs={"pk": self.pk})


class RefernceTable(models.Model):

    pid = models.IntegerField(_("ID"))
    x = models.FloatField(_("X"))
    y = models.FloatField(_("Y"))

    class Meta:
        verbose_name = _("referncetable")
        verbose_name_plural = _("referncetable")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("referncetable_detail", kwargs={"pk": self.pk})


