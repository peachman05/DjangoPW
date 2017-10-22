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
            addressObj = Address.objects.get(user=request.user.id)
            form = AddressForm(request.POST or None, instance=addressObj)
        except MyModel.DoesNotExist: # create
            form = AddressForm()

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request,'data/address.html', {'form':form})
    else:
        return render(request,'home.html', {})

def work_info(request):
    return render(request,'data/work_info.html', {})

def insignia(request):
    return render(request,'data/insignia.html', {})

def education(request):
    # choiceObject = get_object_or_404(Choice, choice_text="1234")
    print(request.user.id)
    print(get_object_or_404(Address, user=request.user.id))
    if request.method == 'POST' and form.is_valid():
        print("in")
        article = get_object_or_404(Choice, choice_text="1234")
        form = ChoiceForm(request.POST, instance=article)		
        
        print(form)
        form.save()
        return redirect('home')
    else:
        # form = ChoiceForm()
        print("else")
        article = get_object_or_404(Choice, choice_text="1234")
        form = ChoiceForm(request.POST or None,instance=article)
        # form.votes = 9
        # form = ChoiceForm()
        # choiceEn = form.save(commit=False)
        # choiceEn.votes = 9
        # print(choiceEn.votes)    
        # print(form)
    return render(request,'data/education.html', {'form':form})