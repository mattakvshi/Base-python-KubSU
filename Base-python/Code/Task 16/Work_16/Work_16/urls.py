"""
URL configuration for Work_16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path("main/main_root", views.main_root, name="main_root.html"),
    path("main/main_aud", views.main_aud, name="main_aud.html"),
    path("main/main_sending", views.main_sending, name="main_sending.html"),
    path("sign_up/sign_up_sending", views.sign_up_sending, name="sign_up_sending.html"),
    path("log_in/log_in_sending", views.log_in_sending, name="log_in_sending.html"),
    path("password_recovery/password_recovery_sending", views.password_recovery_sending,
         name="password_recovery_sending.html"),
    path("sign_up/", views.sign_up, name="sign_up.html"),
    path("log_in/", views.log_in, name="log_in.html"),
    path("password_recovery/", views.password_recovery, name="password_recovery.html"),
    path("main/", views.main, name="main.html"),
    path("", TemplateView.as_view(template_name="home.html")),
]
