from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home/', views.HomeView.as_view(), name ='homeView'),
    path('register/', views.Register, name ='register'),
    path('login/', views.LoginView.as_view(), name ='login'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
]