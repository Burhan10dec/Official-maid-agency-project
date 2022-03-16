from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('logout',views.logoutuser),


    path('FDWs', views.FDWs),
    path('add_FDWs', views.add_FDWs),
    path('FDWs_profile', views.FDWs_profile),
    path('myagency', views.myagency),
    path('myagencyedit', views.myagencyedit),
    path('contract', views.contract),
    # path('users', views.users),
    path('user_role', views.user_role),
    path('add_contract', views.Add_contract),
]

