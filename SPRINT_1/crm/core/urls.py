from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/customer/', views.regcustumer, name='RegCustumer'),
]