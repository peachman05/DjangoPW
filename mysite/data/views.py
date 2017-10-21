from django.shortcuts import render

# Create your views here.
def personal_info(request):
	return render(request,'data/personal_info.html', {})

def address(request):
	return render(request,'data/address.html', {})

def work_info(request):
	return render(request,'data/work_info.html', {})

def insignia(request):
	return render(request,'data/insignia.html', {})

def education(request):
	return render(request,'data/education.html', {})