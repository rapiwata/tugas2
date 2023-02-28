from django.urls import path
from study_tracker.views import assignment_list
from study_tracker.views import create_study
from study_tracker.views import show_xml 
from study_tracker.views import show_json 
from study_tracker.views import show_xml_by_id, show_json_by_id

app_name = 'study_tracker'

urlpatterns = [
    path('', assignment_list, name='assignment_list'),
    path('xml/', show_xml, name='show_xml'),
    path('create', create_study, name='create_study'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 



]