from uuid import uuid4
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import activate, timezone

from backend_test import settings
from option.models import Option
from order.forms import OrderMenuForm
from order.models import Order
from order.timeutils import is_time_limit
from .forms import MenuForm
from datetime import datetime
# Create your views here.
from .models import Menu

activate(settings.TIME_ZONE)


@login_required(login_url="/accounts/login/")
def home_menu(request):
    """
    Returns a list of Menus created with date greater or equal than today
    """
    today = datetime.today().strftime("%Y-%m-%d")
    menu_list = Menu.objects.filter(published_date__gte=today).order_by('published_date')

    return render(request, 'home_menu.html', {'menu_list': menu_list, 'today': today})


def show_error(error, form, request):
    return render(request, 'add_menu.html', {'form': form, 'error_message': error})


@login_required(login_url="/accounts/login/")
def create(request):
    """
    Validates te request to add a new Menu or return the found validations
    """
    today = datetime.today().strftime("%d/%m/%Y")
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            published_date = form.cleaned_data.get("publish_date_input")
            name = form.cleaned_data.get("name")
            try:
                Menu.objects.create(uuid=uuid4(), name=name, published_date=published_date).save()
                return redirect('menu:list_menu')
            except Exception as error:
                return show_error(error, form, request)
    else:
        form = MenuForm()
    return render(request, 'add_menu.html', {'form': form, 'today': today})


@login_required(login_url="/accounts/login")
def menu_add(request):
    """
    Validates te request to add a new Menu
    """
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            published_date = request.REQUEST['published_date_input']
            print(published_date)
            Menu.objects.create(published_date=published_date).save()
            return redirect('menu:index')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form})


@login_required(login_url="/accounts/login")
def menu_delete(request, uuid):
    if request.method == 'GET':
        menu = Menu.objects.filter(uuid=uuid)
        menu.delete()
        return redirect('menu:list_menu')
    else:
        form = MenuForm()
    return render(request, 'list_menu.html', {'form': form})


@login_required(login_url="/accounts/login")
def list_of_menu(request):
    """
    Returns a list of Menus created with date greater or equal than today
    """
    user_time_zone = request.session.get('django_timezone')
    today = datetime.now(user_time_zone).strftime("%Y-%m-%d")
    menu_list = Menu.objects.filter(published_date__gte=today).order_by('published_date')

    return render(request, 'list_menu.html', {'menu_list': menu_list, 'today': today})


@login_required(login_url='/accounts/login')
def menu_order(request, uuid):
    """
    Search a Menu and its Options by an uiid
    Validates the time limit to display the Menu
    """
    if is_time_limit():
        menu = get_object_or_404(Menu, uuid=uuid)
        context = {'menu': menu}
    else:
        context = {'error_message': 'It is not possible to recieve your Order after 11 AM'}

    return render(request, 'order.html', context)


@login_required(login_url='/accounts/login')
def order_add(request, uuid):
    """
    Creates an Order.
    """
    error_message = None
    option = get_object_or_404(Option, uuid=uuid)

    if request.method == 'POST':
        form = OrderMenuForm(request.POST)

        if is_time_limit() and form.is_valid():
            order = Order.objects.create(option=option, order_uuid=uuid4(), **form.cleaned_data)
            order.save()
            return redirect('menu:order_details', order.uuid)
        error_message = 'It is not possible process your Order after 11 AM, try tomorrow'
    else:
        form = OrderMenuForm()

    return render(request,
                  'order_add.html',
                  {'form': form, 'option': option, 'error_message': error_message})
