from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# Examples:
	url(r'^$', 'spoken.views.home', name='home'),
	url(r'^home/', 'spoken.views.home', name='home'),
	# url(r'^spoken/', include('spoken.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	#events urls
	url(r'^events/', include('events.urls', namespace='events')),
	url(r'^moodle/', include('mdldjango.urls', namespace='mdldjango')),

	url(r'^creation/', include('creation.urls', namespace='creation')),
	url(r'^captcha/', include('captcha.urls')),
	
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
	#cms
	url(r'', include('cms.urls', namespace='cms')),
)
