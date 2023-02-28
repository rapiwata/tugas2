from django.forms import ModelForm
from study_tracker.models import Assignment

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ["name", "lesson", "subject", "progress", "description"]