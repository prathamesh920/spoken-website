from django.conf.urls import url, include
from events import views
from events.notification import nemail


urlpatterns = [
    url(r'^$', views.events_dashboard, name='events_dashboard'),
    url(r'^init/$', views.init_events_app, name='init_events_app'),
    
    #cron job
    #todo: test and workshop auto close
    url(r'^fix-date-for-first-training/$', views.fix_date_for_first_training, name='fix_date_for_first_training'),
    #url(r'^training-gentle-reminder/$', views.training_gentle_reminder, name='training_gentle_reminder'),
    #url(r'^training-completion-reminder/$', views.training_completion_reminder, name='training_completion_reminder'),
    url(r'^close-predated-ongoing-workshop/$', views.close_predated_ongoing_workshop, name='close_predated_ongoing_workshop'),
    url(r'^close-predated-ongoing-test/$', views.close_predated_ongoing_test, name='close_predated_ongoing_test'),
    
    url(r'^test/$', nemail, name='test'),
    
    url(r'^ac/$', views.ac, name='ac'),
    url(r'^ac/new/$', views.new_ac, name='new_ac'),
    url(r'^ac/(\d+)/edit/$', views.edit_ac, name='edit_ac'),
    
    #url(r'^xmlparse/$', views.xmlparse, name='xmlparse'),
    #url(r'^pdf/$', views.pdf, name='pdf'),
    url(r'^training/permission/$', views.training_permission, name='training_permission'),
    url(r'^training/accessrole/$', views.accessrole, name='training_accessrole'),
    url(r'^training/old-training-attendance/$', views.old_training_attendance, name='old_training_attendance'),
    url(r'^training/old-training-attendance-upload/(\d+)/$', views.old_training_attendance_upload, name='old_training_attendance_upload'),
    
    url(r'^(?P<role>\w+)/(?P<status>\w+)/$', views.organiser_invigilator_index, name='organiser_invigilator_index'),
    url(r'^organiser/(?P<status>\w+)/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_organiser, name='rp_organiser'),
    
    url(r'^activate-academics/$', views.activate_academics, name='activate_academics'),
    url(r'^activate-academics-org/(?P<academic_id>\d+)/$', views.activate_academic_org, name='activate_academic_org'),

    url(r"^accountexecutive/request/(?P<username>[\w. @-]+)/$", views.accountexecutive_request, name='accountexecutive_request'),
    url(r"^accountexecutive/view/(?P<username>[\w. @-]+)/$", views.accountexecutive_view, name='accountexecutive_view'),
    url(r"^accountexecutive/(?P<username>[\w. @-]+)/edit/$", views.accountexecutive_edit, name='accountexecutive_edit'),
    url(r'^accountexecutive/(?P<status>\w+)/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_accountexecutive, name='rp_accountexecutive'),
    
    url(r"^organiser/request/(?P<username>[\w. @-]+)/$", views.organiser_request, name='organiser_request'),
    url(r"^organiser/(?P<username>[\w. @-]+)/edit/$", views.organiser_edit, name='organiser_edit'),
    url(r"^organiser/view/(?P<username>[\w. @-]+)/$", views.organiser_view, name='organiser_view'),

    url(r'^invigilator/(?P<status>\w+)/(?P<code>\w+)/(?P<userid>\d+)/$', views.rp_invigilator, name='rp_invigilator'),
    url(r"^invigilator/request/(?P<username>[\w. @-]+)/$", views.invigilator_request, name='invigilator_request'),
    url(r"^invigilator/(?P<username>[\w. @-]+)/edit/$", views.invigilator_edit, name='invigilator_edit'),
    url(r"^invigilator/view/(?P<username>[\w. @-]+)/$", views.invigilator_view, name='invigilator_view'),
    
    #live feedback
    url(r'^training/live/list/$', views.live_training, name='live_training'),
    url(r'^training/live/list/(\d+)/$', views.live_training, name='live_training'),
    
    url(r'^training/subscribe/(\w+)/(\d+)/(\d+)/$', views.training_subscribe, name='student_subscribe'),
    url(r'^training/(\d+)/attendance/$', views.training_attendance, name='training_attend'),
    url(r'^training/(\d+)/participant/$', views.training_participant, name='training_participant'),
    url(r'^training/participant/certificate/(\d+)/(\d+)/$', views.training_participant_ceritificate, name='training_participant_ceritificate'),
    url(r'^training/participant/feedback/(\d+)/(\d+)/$', views.training_participant_feedback, name='training_participant_feedback'),
    
    #live feedback
     url(r'^training/participant/lfeedback/(\d+)/(\d+)/$', views.training_participant_viewlivefeedback, name='training_participant_viewlivefeedback'),
    url(r'^training/participant/lfeedback/(\d+)/$', views.training_participant_livefeedback, name='training_participant_livefeedback'),
    
    #language Feedback
    #url(r'^training/participant/language-feedback/(\d+)/(\d+)/$', views.training_participant_view_language_feedback, name='training_participant_viewlivefeedback'),
    url(r'^training/participant/language-feedback/(\d+)/(\d+)/$', views.training_participant_language_feedback, name='training_participant_language_feedback'),
    
    url(r'^training/(?P<role>\w+)/request/$', views.training_request, name='training_request'),
    url(r'^training/(?P<role>\w+)/clone/$', views.training_clone, name='training_clone'),
    url(r'^training/(?P<role>\w+)/(?P<rid>\d+)/approvel/$', views.training_approvel, name='training_approvel'),
    url(r'^training/(?P<role>\w+)/(?P<status>\w+)/$', views.training_list, name='training_list'),
    url(r'^training/(?P<role>\w+)/(?P<rid>\d+)/edit/$', views.training_request, name='training_edit'),
    url(r'^training/(?P<role>\w+)/(?P<rid>\d+)/clone/$', views.training_clone, name='training_clone'),
    #url(r'^training/training-completion/(?P<rid>\d+)/$', views.training_completion, name="training_completion"),
    url(r'^training/view/training-completion/(?P<rid>\d+)/$', views.view_training_completion, name="view_training_completion"),
    
    #url(r'^test/subscribe/(\d+)/(\d+)/$', views.test_student_subscribe, name='test_student_subscribe'),
    url(r'^test/(\d+)/participant/$', views.test_participant, name='test_participant'),
    url(r'^test/participant/certificate/(\d+)/(\d+)/$', views.test_participant_ceritificate, name='test_participant_ceritificate'),
    url(r'^test/(\d+)/attendance/$', views.test_attendance, name='test_attendance'),
    url(r'^test/(?P<role>\w+)/request/$', views.test_request, name='test_request'),
    url(r'^test/(?P<role>\w+)/(?P<rid>\d+)/approvel/$', views.test_approvel, name='test_approvel'),
    url(r'^test/(?P<role>\w+)/(?P<status>\w+)/$', views.test_list, name='test_list'),
    url(r'^test/(?P<role>\w+)/(?P<rid>\d+)/edit/$', views.test_request, name='test_request'),

    url(r'^delete-notification/(\w+)/(\d+)/$', views.delete_events_notification, name="delete_events_notification"),
    url(r'^clear-notifications/(\w+)/$', views.clear_events_notification, name="clear_events_notification"),
    
    url(r'^resource-center/$', views.resource_center, name="resource_center"),
    url(r'^resource-center/(?P<slug>[\w-]+)/$', views.resource_center, name="resource_center"),
    
    url(r'^academic-center/(?P<academic_id>\d+)/$', views.academic_center, name="academic_center"),
    url(r'^academic-center/(?P<academic_id>\d+)/(?P<slug>[\w-]+)/$', views.academic_center, name="academic_center"),
    
    #Ajax 
    url(r'ajax-ac-state/$', views.ajax_ac_state, name='ajax_ac_state'),
    url(r'ajax-ac-location/$', views.ajax_ac_location, name='ajax_ac_location'),
    url(r'ajax-ac-pincode/$', views.ajax_ac_pincode, name='ajax_ac_pincode'),
    url(r'ajax-district/$', views.ajax_district_data, name='ajax_district_data'),
    url(r'ajax-district-collage/$', views.ajax_district_collage, name='ajax_district_collage'),
    url(r'ajax-state-collage/$', views.ajax_state_collage, name='ajax_state_collage'),
    url(r'ajax-dept-foss/$', views.ajax_dept_foss, name='ajax_dept_foss'),
    url(r'ajax-language/$', views.ajax_language, name='ajax_language'),
    url(r'ajax_state_details/$', views.ajax_state_details, name='ajax_state_details'),
    url(r'ajax-academic-center/$', views.ajax_academic_center, name='ajax_academic_center'),
    url(r'ajax-check-foss/$', views.ajax_check_foss, name='ajax_check_foss'),
    #url(r'add$', views.add_contact, name='add_contact'),
    #url(r'edit/(\d+)$', views.edit_contact, name='edit_contact'),   
    #url(r'delete/(\d+)$', views.delete_contact, name='delete_contact'),
    # EVENTS V2 URLs
    url(r'^', include('events.urlsv2')),
]
