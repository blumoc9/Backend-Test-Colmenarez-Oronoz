from django.urls import path

from .views import home_menu, create

app_name = 'menu'
urlpatterns = [
    path('home/', home_menu, name='index'),
    path('create/', create, name='create'),
    path('list/', list, name='list'),

]
