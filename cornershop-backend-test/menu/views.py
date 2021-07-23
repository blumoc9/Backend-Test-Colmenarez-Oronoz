import uuid
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldError
from django.shortcuts import render, redirect
from .forms import MenuForm
import datetime
# Create your views here.
from .models import Menu


@login_required(login_url="")
def home_menu(request):
    """
    Returns a list of Menus created with date greater or equal than today
    """
    today = datetime.date.today()
    menu_list = Menu.objects.filter(published_date__gte=today).order_by('published_date')

    return render(request, 'home_menu.html', {'menu_list': menu_list})


@login_required(login_url="/accounts/login/")
def menu_create(request):
    """
    Validates te request to add a new Menu or return the found validations
    """
    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            published_date = form.cleaned_data['published_date_input']
            try:
                menu = Menu.objects.create(uuid=uuid4(), published_date=published_date).save()
                return redirect('menu_add', menu)
            except Exception as e:
                raise FieldError('Menu The date has been register')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form})
