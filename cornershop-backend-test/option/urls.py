from django.urls import path

from .views import option_menu_add, option_menu_edit, options_menu_details_by_uuid, option_menu_delete

app_name = 'option'
urlpatterns = [
    path('<uuid:uuid>/add', option_menu_add, name='option_menu_add'),
    path('<uuid:uuid>/edit', option_menu_edit, name='option_menu_edit'),
    path('<uuid:uuid>/details', options_menu_details_by_uuid, name='options_menu_details_by_uuid'),
    path('<uuid:uuid>/delete', option_menu_delete, name='option_menu_delete'),
]
