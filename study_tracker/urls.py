from django.urls import path
from study_tracker.views import assignment_list 

app_name = 'study_tracker'

urlpatterns = [
    path('', assignment_list, name='assignment_list'),
]
