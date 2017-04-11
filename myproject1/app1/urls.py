from django.conf.urls import url
from . import views
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
urlpatterns = [    
    url(r'^$', views.home, name='home'),    
    url(r'^register/$', views.register, name='register'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^logout/', auth.views.logout),     
    url(r'^login_firsttime/$', views.login_firsttime,name='login_firsttime'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/products/$', views.products, name='products'),
    url(r'^dashboard/products/create_product/$', views.create_product, name='create_product'),
]
