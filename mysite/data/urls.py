from django.conf.urls import url

from . import views

app_name = 'data'
urlpatterns = [
    url(r'^personal_info/(?P<user_id_input>[0-9]+)?', views.personal_info,  name='personal_info'),
    url(r'^address/(?P<user_id_input>[0-9]+)?', views.address,  name='address'),
    url(r'^work_info/(?P<user_id_input>[0-9]+)?', views.work_info,  name='work_info'),
    url(r'^insignia/(?P<user_id_input>[0-9]+)?', views.insignia,  name='insignia'),
    url(r'^education/(?P<user_id_input>[0-9]+)?', views.education,  name='education'),


    url(r'^list_teacher/', views.list_teacher,  name='list_teacher'),
]