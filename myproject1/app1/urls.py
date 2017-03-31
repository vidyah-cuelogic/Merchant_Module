from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.home, name='home'),    
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_firsttime/$', views.login_firsttime,name='login_firsttime'),
    url(r'^login_firsttime/login/$', views.login_firsttime,name='loginpage'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/products/$', views.products, name='products'),
    url(r'^dashboard/products/create_product/$', views.create_product, name='create_product'),
]



