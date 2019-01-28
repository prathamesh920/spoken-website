# Third Party Stuff
from django.conf.urls import url
from youtube import views

urlpatterns = [ 
    url(r'^$', views.home, name="home"),
    url(r'^delete-videos/$', views.delete_all_videos, name="delete_all_videos"),
    url(r'^remove-youtube-video/$', views.remove_youtube_video, name="remove_youtube_video"),
    url(r'^remove-video-entry/(\d+)/(\d+)/$', views.remove_video_entry, name="remove_video_entry"),
    url(r'^ajax-foss-based-language-tutorial/$', views.ajax_foss_based_language_tutorial,
        name="ajax_foss_based_language_tutorial"),
    url(r'^oauth2callback/$', views.auth_return, name="auth_return"),
]
