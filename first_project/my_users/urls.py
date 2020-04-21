from django.conf.urls import url
from my_users import views

urlpatterns = [
    url('', views.my_users_dis, name='my_users'),
]