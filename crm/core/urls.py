from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name="Contacts"),
    path('contacts/atualiza/medico/<str:pk>/', views.medic_atualiza, name='AtualizaMedico'),
    path('contacts/delete/medico/<str:pk>/', views.medic_deleta, name='DeletaMedico'),
    path('contacts/atualiza/clinic/<str:pk>/', views.clinic_atualiza, name='AtualizaClinic'),
    path('contacts/delete/clinic/<str:pk>/', views.clinic_deleta, name='DeletaClinic'),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('register/', views.register, name="Register"),
    path('register/client/', views.register_client, name='RegisterClient'),
    path('register/client/customer/', views.form_medic, name='RegCustumer'),
    path('register/client/clinic/', views.form_clinic, name='RegClinic'),
    path('leads/', views.leads, name='Leads'),
    path('proposta/', views.proposta, name='Proposta'),
    path('atualiza/<str:pk>/', views.atualizaProposta, name='Atualiza'),
    path('delete/<str:pk>/', views.deletaProposta, name='Delete'),
    path('contatos/import/', views.importacao, name="Importar"),
    path('atualiza/titulo/1/', views.titulomain, name='AtualizaTitulo')
]
