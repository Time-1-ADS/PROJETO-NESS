from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name="Contacts"),
    path('login/', views.login, name="Login"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('register/', views.register, name="Register"),
    path('register/customer/', views.form_medic, name='RegCustumer'),
    path('leads/', views.leads, name='Leads'),
    path('proposta/', views.proposta, name='Proposta'),
    path('atualiza/<str:pk>/', views.atualizaProposta, name='Atualiza'),
    path('delete/<str:pk>/', views.deletaProposta, name='Delete'),
]
