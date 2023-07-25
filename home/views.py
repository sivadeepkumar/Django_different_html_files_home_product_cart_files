from django.shortcuts import render,redirect

from django.http import HttpResponse 

from home.models import *

def home(request):
    if request.method == 'POST':

        data = request.POST
        receipe_name = data.get('receipe-name')
        receipe_description = data.get('receipe-description')
        receipe_image = request.FILES.get('receipe-image')

        print(receipe_name,receipe_description,receipe_image)   


        # Receipe.objects.create(receipe_name = receipe_name,receipe_description = receipe_description,receipe_image = receipe_image)
        Receipe.objects.create(receipe_name = receipe_name,receipe_description = receipe_description,receipe_image = receipe_image)
        return redirect('/')
    return render(request,'home.html')




