# Third Party Stuff
from django.conf.urls import url
from cdcontent import views
urlpatterns = [ 
    # Main pages dispatcher
    url(r'^$', views.home, name="cdcontenthome"),
    url(r'^ajax-fill-languages/$', views.ajax_fill_languages, name="ajax_fill_languages"),
    url(r'^ajax-add-foss/$', views.ajax_add_foss, name="ajax_add_foss"),
    url(r'^ajax-show-added-foss/$', views.ajax_show_added_foss, name="ajax_show_added_foss"),
]
