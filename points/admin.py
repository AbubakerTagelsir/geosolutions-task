from django.contrib import admin

# Register your models here.
from .models import Point, History,RefernceTable


admin.site.register(Point)
admin.site.register(RefernceTable)
admin.site.register(History)