from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.usercadastrado, name="Cadastro"),
    path('login/', views.login, name="Login"),
    path('login/submit', views.logar),
    path('logout/', views.logout, name='Logout'),
    # path('profile/<str:pk>/', views.profile, name='Profile'),

]
