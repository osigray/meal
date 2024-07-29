from . import views
from django.urls import path

urlpatterns = [
   
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
     path('logout/', views.logout_user, name='logout'),
    
    
    

]
