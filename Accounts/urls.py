from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    # path('employee/', views.employee, name='employee'),
    path('logout/',views.deconnexion, name='logout'),

]