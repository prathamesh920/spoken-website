# Third Party Stuff
from django.conf.urls import url
from masquerade import views
urlpatterns = [ 
    url(r'^$', views.masquerade_home, name="masquerade_home"),
    url(r'^mask/(\d+)/$', views.mask, name="mask"),
    url(r'^unmask/$', views.unmask),
]
