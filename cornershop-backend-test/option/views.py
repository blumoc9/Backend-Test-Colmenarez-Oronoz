from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from menu.models import Menu
from option.forms import OptionMenuForm
from option.models import Option
from django.urls import reverse


@login_required(login_url="/accounts/login")
def option_menu_add(request, uuid):
    """
    Validates the request to add a new Option
    """
    if request.method == 'POST':
        form = OptionMenuForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data.get('description')
            is_vegan = form.cleaned_data.get('is_vegan')
            menu = Menu.objects.filter(uuid=uuid)
            Option.objects.create(menu_id=menu[0].id, description=description, is_vegan=is_vegan
                                  , publish_date=menu[0].published_date
                                  , code=uuid4()).save()
            return redirect(reverse('menu_nora:list_menu'), {'form': form, 'uuid': uuid})
    else:
        form = OptionMenuForm()

    return render(request, 'option_menu_add.html', {'form': form, 'uuid': uuid})


@login_required(login_url="/accounts/login")
def option_menu_edit(request, uuid):
    """
    Validates the request to edit an Option or return the found validations
    """
    option = get_object_or_404(Option, uuid=uuid)

    if request.method == 'POST':
        form = OptionMenuForm(request.POST)

        if form.is_valid():
            option.description = form.cleaned_data['description']
            option.save()
            return redirect('menu:details_uuid', option.menu.uuid)
    else:
        form = OptionMenuForm(data={'description': option.description})

    context = {'form': form, 'option': option}
    return render(request, 'option_details.html', context)


def options_menu_details_by_uuid(request, uuid):
    """
    Search a Menu and its Options by an uuid
    """
    menu = get_object_or_404(Menu, uuid=uuid)
    options = Option.objects.filter(menu_id=menu.id)

    context = {'menu': menu, 'options': options}

    return render(request, 'options_menu_details_by_uuid.html', context)
