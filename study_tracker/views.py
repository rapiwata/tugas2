from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

def assignment_list(request):
    assignments_data = Assignment.objects.all()
    context = {
        'list_of_study': assignments_data,
        'name': 'M.Raffi'
    }

    return render(request, "assignment.html", context)

def create_study(request):
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:assignment_list'))

    context = {'form': form}
    return render(request, "create_study.html", context)

def show_xml(request):
    data = Assignment.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Assignment.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Assignment.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = Assignment.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")












    












    


