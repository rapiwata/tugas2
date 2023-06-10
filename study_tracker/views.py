import json
from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/study_tracker/login/')
def assignment_list(request):
    assignments_data = Assignment.objects.all()
    context = {
        'list_of_study': assignments_data,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('study_tracker:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("study_tracker:assignment_list")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:login'))
    response.delete_cookie('last_login')
    return response

def modify_study(request, id):
    # Get data berdasarkan ID
    studi = Assignment.objects.get(pk = id)

    # Set instance pada form dengan data dari transaction
    form = AssignmentForm(request.POST or None, instance=studi)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:assignment_list'))

    context = {'form': form}
    return render(request, "modify_study.html", context)

def delete_study(request, id):
    # Get data berdasarkan ID
    studia = Assignment.objects.get(pk = id)
    # Hapus data
    studia.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('study_tracker:assignment_list'))

@csrf_exempt
def create_study_ajax(request):  
# create object of form
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = Assignment.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'name':data.name,
            'lesson':data.lesson,
            'subject':data.subject,
            'date':data.date,
            'progress':data.progress,
            'description':data.description
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_study.html", context)

@csrf_exempt
def create_transaction_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_transaction = Assignment.objects.create(
            name = data["name"],
            type = data["type"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_transaction.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)














    












    


