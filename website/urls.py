from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'), Se vc quiser criar uma página separada 
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('add_record',views.add_record, name='add_record'),
    path('update_record/<int:pk>',views.update_record, name='update_record'),
]

#3 steps to create a webpage 1. create a template/html file 2. Create URL and create a view