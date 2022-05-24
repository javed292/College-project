from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path("register/", views.register,name="register"),
    path('login/', views.loginp, name='login'),
    path("logout/", views.logoutp,name="logout"),
    path("mycourses/", views.mycourses,name="mycourses"),


]