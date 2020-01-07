from django.urls import path

from . import views

app_name = "points"
urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.HistoryView.as_view(), name='history'),
    # path('new/<int:pk>', views.NewView.as_view(), name='new'),
    path('new', views.new_form, name='new'),
    path('submit', views.submit_form, name='submit'),
]