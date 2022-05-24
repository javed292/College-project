
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="Home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("courses/", views.courses, name="courses"),
    path("products/<int:myid>", views.productView, name="ProductView"),
     path("payment/", views.payment, name="payment"),
     path("debitpay/", views.debitpay, name="debitpay"),
     path("courseslist/", views.listcourse, name="listcourse"),
    # path("login/", views.login, name="login"),
    path("account/", include("user_app.urls")),


    # path("webb/", include('webb.urls')),



]