from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name="Contacts"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('register/', views.register, name="Register"),
    path('register/customer/', views.regcustumer, name='RegCustumer'),
    path('register/employee/', views.regemployee, name='RegEmployee'),

]