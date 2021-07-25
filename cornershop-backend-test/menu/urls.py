from django.urls import path

from .views import home_menu, create, menu_add,list_of_menu, menu_delete

app_name = 'menu'
urlpatterns = [
    path('home/', home_menu, name='index'),
    path('create/', create, name='create_menu'),
    path('list/', list_of_menu, name='list_menu'),
    path('add/', menu_add, name='add'),
    path('<uuid:uuid>/delete', menu_delete, name='menu_delete'),

]
