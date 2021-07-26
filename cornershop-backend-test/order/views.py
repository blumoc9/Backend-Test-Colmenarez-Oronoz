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

    if request.method == 'POST':
        form = OrderMenuForm(request.POST)
        customization = form.cleaned_data.get('customization')
        phone_number = form.cleaned_data.get('customization')
        if is_time_limit() and form.is_valid():
            order = Order.objects.create(phone_number=phone_number, customization=customization,
                                         option=option,
                                         order_uuid=uuid4(), **form.cleaned_data)
            order.save()
            return redirect('menu:order_details', order.uuid)
        error_message = message_error_hour_validation()
    else:
        form = OrderMenuForm()

    return render(request,
                  'add_order.html',
                  {'form': form, 'option': option, 'error_message': error_message})
