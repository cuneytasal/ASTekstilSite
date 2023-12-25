
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('', views.index, name='index'),
    path('ehome/', views.ehome, name='ehome'),
    path('fhome/', views.fhome, name='fhome'),
    path('eaboutus/', views.eaboutus, name='eaboutus'),
    path('faboutus/', views.faboutus, name='faboutus'),
    path('econtact/', views.econtact, name='econtact'),
    path('fcontact/', views.fcontact, name='fcontact'),
    path('eproducts/', views.eproducts, name='eproducts'),
    path('fproducts/', views.fproducts, name='fproducts'),
    path('add_product/', views.create_product, name='create_product'),
    path('edit_product/<str:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete_product'),
]
