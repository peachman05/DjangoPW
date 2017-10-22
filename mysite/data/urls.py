from django.conf.urls import url

from . import views

app_name = 'data'
urlpatterns = [
    url(r'^personal_info/', views.personal_info,  name='personal_info'),
    url(r'^address/(?P<user_id_input>[0-9]+)?', views.address,  name='address'),
    url(r'^work_info/', views.work_info,  name='work_info'),
    url(r'^insignia/', views.insignia,  name='insignia'),
    url(r'^education/', views.education,  name='education'),

    # url(r'^addressStaff/(?P<pk>[0-9]+)?', views.addressStaff,  name='addressStaff'),

    url(r'^list_teacher/', views.list_teacher,  name='list_teacher'),
]