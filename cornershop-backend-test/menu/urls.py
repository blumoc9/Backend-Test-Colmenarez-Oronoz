from django.urls import path

from .views import home_menu

app_name = 'menu'
urlpatterns = [
    path('', home_menu, name='index'),

]
