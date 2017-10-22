from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import Http404
from .models import *
# Create your views here.
def personal_info(request):
    return render(request,'data/personal_info.html', {})

def address(request):
    if request.user.is_authenticated:        
        print(request.user.is_staff)

        try: # edit
            print("edit")
            addressObj = Address.objects.get(user=request.user.id)
            form = AddressForm(request.POST or None, instance=addressObj)
            isCreate = False
        except Address.DoesNotExist: # create
            print("create")
            form = AddressForm()
            isCreate = True

        print("create2")
        if request.method == 'POST' :
            print("in")
            if isCreate:
                form = AddressForm(request.POST)
            if form.is_valid():
                print("in2")
                recipe = form.save(commit=False)
                recipe.user = request.user
                recipe.save()
                return redirect('home')
        
        return render(request,'data/address.html', {'form':form})
    else:
        return render(request,'home.html', {})

def work_info(request):
    return render(request,'data/work_info.html', {})

def insignia(request):
    return render(request,'data/insignia.html', {})

def education(request):
    if request.user.is_authenticated:        
        print(request.user.is_staff)

        try: # edit
            print("edit")
            addressObj = Choice.objects.get(question=2)
            form = ChoiceForm(request.POST or None, instance=addressObj)
            isCreate = False
        except Choice.DoesNotExist: # create
            print("create")
            form = ChoiceForm()
            isCreate = True

        print("create2")
        if request.method == 'POST' :            
            print("in")
            if isCreate:
                form = ChoiceForm(request.POST)
            print(form)    
            if form.is_valid():
                print("in2")
                recipe = form.save(commit=False)
                # recipe.user = request.user.id
                recipe.save()
                return redirect('home')
        
        return render(request,'data/education.html', {'form':form})
    else:
        return render(request,'home.html', {})