from django.shortcuts import render,redirect
from django import forms
from .forms import UploadForm,GetForm
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
def list_id(request,id):
    
    flavour=Flavour.objects.get(pk=id)
    context={
        
        'flavour':flavour
    }

    return render(request,'app/details.html',context)


@login_required
def update(request,id):
    flavour=Flavour.objects.get(pk=id)
    form=GetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request,'app/update.html',{'flavour':flavour,'form':form})