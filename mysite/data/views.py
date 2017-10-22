from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def getForm(request,modelInput,modelFormInput,path,userInput):
    print(userInput.username)
    if request.user.is_authenticated:  
        try: # edit
            modelObj = modelInput.objects.get(user=userInput.id)
            form = modelFormInput(request.POST or None, instance=modelObj)
            isCreate = False
        except modelInput.DoesNotExist: # create
            print("create")
            form = modelFormInput()
            isCreate = True

        if request.method == 'POST' :
            print("in")
            if isCreate:
                form = modelFormInput(request.POST)
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.user = userInput
                recipe.save()
                return redirect('home')
        
        return render(request,'data/'+path+'.html', {'form':form})
    else:
        return render(request,'login.html', {})

def personal_info(request):
    return render(request,'data/personal_info.html', {})

def address(request,user_id_input=None):
    if user_id_input == None:
        return getForm(request,Address,AddressForm,'address',request.user)    
    elif request.user.is_staff:
        userObj = get_object_or_404(User, pk=user_id_input)
        print("ffff")
        return getForm(request,Address,AddressForm,'address',userObj)

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

def list_teacher(request):
        teacher_obj_list = User.objects.filter(is_staff=False).order_by('username')  #User.objects.order_by('username')[:5]

        return render(request,'data/list_teacher.html', {'teacher_obj_list':teacher_obj_list})
    # <!-- {% for user in teacher_obj_list %}
    #     <li><a href="{% url 'data:detail' user.id %}">{{ question.question_text }}</a></li>
    # {% endfor %}
    # {{teacher_obj_list}}-->