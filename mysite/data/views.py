from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def personal_info(request):
	return render(request,'data/personal_info.html', {})

def address(request):
    form = AddressForm()
    return render(request,'data/address.html', {'form':form})

def work_info(request):
	return render(request,'data/work_info.html', {})

def insignia(request):
	return render(request,'data/insignia.html', {})

def education(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)		
        if form.is_valid():
            print(form)
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return render(request, 'home.html')
            return redirect('home')
    else:
        # form = ChoiceForm()
        article = get_object_or_404(Choice, choice_text="1234")
        form = ChoiceForm(request.POST or None,instance=article)    
    return render(request,'data/education.html', {'form':form})