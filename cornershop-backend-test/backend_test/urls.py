""""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from .utils.healthz import healthz
from core.views import home

urlpatterns = [
    path("healthz", healthz, name="healthz"),
    path('', home, name="login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('core/', include('core.urls', namespace="core")),
    path('menu/', include('menu.urls', namespace="menu_nora")),
    path('option/', include('option.urls', namespace="options_menu")),
    path('order/', include('order.urls', namespace="order_of_menu"))
]
