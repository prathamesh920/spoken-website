# Third Party Stuff
from django.conf.urls import url
from statistics import views

urlpatterns = [
    url(r'^$', views.maphome, name="maphome"),
    url(r'^india-map/$', views.maphome, name="maphome"),
    url(r'^motion-chart/$', views.motion_chart, name="motion_chart"),
    url(r'^get-state-info/(\w+)/$', views.get_state_info, name="get_state_info"),
    url(r'^training-onlinetest/$', views.training, name="statistics_training"),
    url(r'^training/$', views.training, name="statistic_training"),
    url(r'^tutorial-content/$', views.tutorial_content, name="statistics_content"),
    url(r'^training/(?P<rid>\d+)/participants/$', views.training_participant,
        name="statistics_training_participants"),
    url(r'^training/(?P<rid>\d+)/participant/students/$', views.studentmaster_ongoing,
        name="statistics_studentmaster_ongoing"),
    
    url(r'^online-test/$', views.online_test, name="statistics_online_test"),
    url(r'^onlinetest/(?P<rid>\d+)/participants/$', views.test_participant,
        name="statistics_test_participants"),
    url(r'^academic-center/$', views.academic_center, name="acdemic_center"),
    url(r'^academic-center/(?P<academic_id>\d+)/$', views.academic_center_view,
        name="academic_center_view"),
    url(r'^academic-center/(?P<academic_id>\d+)/(?P<slug>[\w-]+)/$', views.academic_center_view,
        name="academic_center_view"),
    url(r'^learners/$', views.learners, name="learners"),
    url(r'^pmmmnmtt/fdp/$', views.fdp_training, name="fdp_training"),
]
