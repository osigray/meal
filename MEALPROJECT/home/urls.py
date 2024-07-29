from .import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('service/', views.service, name='service'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    

]
