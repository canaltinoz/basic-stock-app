from django.shortcuts import render,redirect
from django import forms
from .forms import UploadForm
from .models import Flavour
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'app/index.html')

@login_required
def upload(request):
    if request.POST:
    
        form=UploadForm(request.POST,request.FILES)
        print(request.FILES)

        if form.is_valid():
            form.save()
        return redirect(list)
        
    return render(request,'app/upload.html',{'form':UploadForm})

@login_required
def list(request):

    flavour_list=Flavour.objects.all()
    return render(request, 'app/list.html', {
        'flavour_list':flavour_list
    })

@login_required
def get(request):
    return render(request,'app/get.html')