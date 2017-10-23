from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def getForm(request,modelInput,modelFormInput,path,user_id_input,dict_send):

    if user_id_input == None:
        userInput = request.user
    elif request.user.is_staff:
        userInput = get_object_or_404(User, pk=user_id_input)

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
        dict_send['form'] = form
        # print(type(form))
        # for field in form:
        #     print(field)
        # for key, value in form.iteritems() :
        #     print(key)
        return render(request,'data/'+path+'.html', dict_send)
    else:
        return render(request,'login.html', {})

# def checkUser(request,modelInput,modelFormInput,path,user_id_input):
    if user_id_input == None:
        return getForm(request,modelInput,modelFormInput,path,request.user)    
    elif request.user.is_staff:
        userObj = get_object_or_404(User, pk=user_id_input)
        return getForm(request,modelInput,modelFormInput,path,userObj)

def personal_info(request,user_id_input=None):
    dict_send = {'title':'Personal Information'}
    return getForm(request,PersonalInfo,PersonalInfoForm,'baseInfo',user_id_input,dict_send)

def address(request,user_id_input=None):
    dict_send = {'title':'Address'}
    return getForm(request,Address,AddressForm,'address',user_id_input,dict_send)

def work_info(request,user_id_input=None):
    dict_send = {'title':'Work Infomation'}
    return getForm(request,WorkInfo,WorkInfoForm,'baseInfo',user_id_input,dict_send)

def insignia(request,user_id_input=None):
    dict_send = {'title':'Insignia'}
    return getForm(request,Insignia,InsigniaForm,'baseInfo',user_id_input,dict_send)

def education(request,user_id_input=None):
    dict_send = {'title':'Education'}
    return getForm(request,Education,EducationForm,'baseInfo',user_id_input, dict_send)

def list_teacher(request):
    teacher_obj_list = User.objects.filter(is_staff=False).order_by('username')  #[:5]
    return render(request,'data/list_teacher.html', {'teacher_obj_list':teacher_obj_list})
