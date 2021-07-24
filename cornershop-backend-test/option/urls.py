from django.urls import path

from .views import option_menu_add, option_menu_edit

app_name = 'option'
urlpatterns = [
    path('<uuid:uuid>/add', option_menu_add, name='option_menu_add'),
    path('<uuid:uuid>/edit', option_menu_edit, name='option_menu_edit'),
]
