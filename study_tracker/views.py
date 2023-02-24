from django.shortcuts import render
from .models import Assignment

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_study': assignment_list,
        'name': 'M.Raffi'
    }

    return render(request, "assignment.html", context)










    


