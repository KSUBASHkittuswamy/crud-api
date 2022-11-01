from datetime import date
from email.mime import image
from tkinter import image_names
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Details
# Create your views here.


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def create_user(request):
    if request.method == "POST":

        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        gender = request.POST['gender']
        degree = request.POST['degree']
        date_field = request.POST['txtdate']
        # image_user = request.FILES.get('image_name')
        obj = Details.objects.create(name=name, age=age, address=address, gender=gender,degree=degree, date_field=date_field)
        obj.save()
        print(obj)
        return redirect('retrieve')
    else:
        return render(request, 'index.html')


def retrieve_user(request):
    details = Details.objects.all()
    return render(request, 'retrieve.html', {'details': details})


def edit_user(request, id):

    object = Details.objects.get(id=id)
    data_dict = model_to_dict(object)
    print(data_dict)
    return JsonResponse(data_dict,safe=False)
    #return render(request, 'edit.html', {'object': object})


def update_user(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['Address']
        gender = request.POST['gender']
        degree = request.POST['degree']
        date = request.POST['txtdate']
        # image_user = request.FILES.get('image_name')
        Details.objects.filter(id=id).update(name=name, age=age, address=address,gender=gender, degree=degree, date_field=date)
        return redirect('retrieve')


def delete_user(request, id):
    Details.objects.filter(id=id).delete()
    return redirect('retrieve')