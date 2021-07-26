from django.urls import path

from .views import home_order, order_add, order_details, list_order_by_user

app_name = 'order'
urlpatterns = [
    path('home/', home_order, name='index'),
    path('<uuid:uuid>/add', order_add, name='order_add'),
    path('<uuid:uuid>/details', order_details, name='order_details'),
    path('list/', list_order_by_user, name='list_order_by_user'),
]
