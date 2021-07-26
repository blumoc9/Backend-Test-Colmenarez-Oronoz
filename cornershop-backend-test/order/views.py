from datetime import datetime
from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from option.models import Option
from order.forms import OrderMenuForm
from order.models import Order
from order.timeutils import is_time_limit
from .messagevalidation import message_error_hour_validation


def home_order(request):
    """
    Returns a list  of options of menu for today
    """
    today = datetime.today().strftime("%Y-%m-%d")
    menu_list = Option.objects.filter(publish_date=today).order_by('publish_date')

    return render(request, 'home_order.html', {'menu_list': menu_list, 'today': today})


def home_by_uuid(request, uuid):
    """
    Returns a list  of options of menu for today
    """
    today = datetime.today().strftime("%Y-%m-%d")
    menu_list = Option.objects.filter(menu_uuid=uuid, publish_date=today).order_by('description')
    if is_time_limit():
        error_message = message_error_hour_validation()
    else:
        error_message = ""
    return render(request, 'home_order.html', {'menu_list': menu_list,
                                               'today': today,
                                               'error_message': error_message,
                                               'is_time_limit': is_time_limit()})


@login_required(login_url='/accounts/login')
def order_add(request, uuid):
    """
    Creates an Order.
    """
    error_message = None
    option = get_object_or_404(Option, code=uuid)
    today = datetime.today().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = OrderMenuForm(request.POST)
        print(request.POST)
        if is_time_limit() and form.is_valid():
            username = request.POST['username']
            customization = request.POST['customization']
            phone_number = request.POST['phone_number']
            order = Order.objects.create(customization=customization,
                                         username=username,
                                         option=option,
                                         option_uuid=uuid,
                                         phone_number=phone_number,
                                         order_uuid=uuid4(),
                                         order_date=today)
            order.save()
            return redirect('order:order_details', order.order_uuid)
        error_message = message_error_hour_validation()
    else:
        form = OrderMenuForm()

    return render(request,
                  'add_order.html',
                  {'form': form, 'option': option, 'error_message': error_message})


@login_required(login_url='/accounts/login')
def order_details(request, uuid):
    """
    Search a Menu and its Options by an uiid
    """
    order = get_object_or_404(Order, order_uuid=uuid)

    return render(request, 'detail_order.html', {'order': order})


@login_required(login_url='/accounts/login')
def list_order_by_user(request):
    """
    Returns a list  of options of menu for today
    """
    username = request.user.username
    print(request.user.username)
    today = datetime.today().strftime("%Y-%m-%d")
    order_list = Order.objects.filter(username=username, order_date__gte=today).order_by('customization')

    return render(request, 'list_order.html', {'order_list': order_list, 'today': today})
