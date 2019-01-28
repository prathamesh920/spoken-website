# Third Party Stuff
from django.conf.urls import url
from reports import views
urlpatterns = [
    url(r'events/training/csv/$', views.events_training_csv, name='events_training_csv'),
    url(r'events/test/csv/$', views.events_test_csv, name='events_test_csv'),
    url(r'(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/csv/$', views.export_csv, name='export_csv'),
    url(r'(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/report/$', views.report_filter, name='report_filter'),
    url(r'elibrary/$', views.elibrary, name='elibrary'),
]
