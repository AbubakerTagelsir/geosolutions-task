from django.db import models

# Create your models here.


class Point(models.Model):

    x = models.FloatField(_("X"))
    y = models.FloatField(_("Y"))
    pid = models.IntegerField(_("Point ID"))

    class Meta:
        verbose_name = _("point")
        verbose_name_plural = _("points")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("point_detail", kwargs={"pk": self.pk})
