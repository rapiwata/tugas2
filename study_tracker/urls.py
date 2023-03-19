from django.urls import path
from study_tracker.views import assignment_list
from study_tracker.views import create_study
from study_tracker.views import show_xml 
from study_tracker.views import show_json 
from study_tracker.views import show_xml_by_id, show_json_by_id
from study_tracker.views import register
from study_tracker.views import login_user 
from study_tracker.views import logout_user
from study_tracker.views import modify_study
from study_tracker.views import delete_study
from study_tracker.views import create_study_ajax



app_name = 'study_tracker'

urlpatterns = [
    path('', assignment_list, name='assignment_list'),
    path('xml/', show_xml, name='show_xml'),
    path('create', create_study, name='create_study'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
     path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('modify/<int:id>', modify_study, name='modify_study'),
    path('delete/<int:id>', delete_study, name='delete_study'),
    path('create-ajax/', create_study_ajax, name='create_study_ajax'),



]