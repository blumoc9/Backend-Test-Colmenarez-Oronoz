from django.urls import path

from .views import home_order, order_add

app_name = 'order'
urlpatterns = [
    path('home/', home_order, name='index'),
    path('<uuid:uuid>/add', order_add, name='order_add'),
]
