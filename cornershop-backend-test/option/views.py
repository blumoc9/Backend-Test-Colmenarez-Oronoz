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
                                  , code=uuid4(), menu_uuid=uuid).save()
            return redirect(reverse('menu_nora:list_menu'), {'form': form, 'uuid': uuid})
    else:
        form = OptionMenuForm()

    return render(request, 'option_menu_add.html', {'form': form, 'uuid': uuid})


@login_required(login_url="/accounts/login")
def option_menu_edit(request, uuid):
    """
    Validates the request to edit an Option or return the found validations
    """

    option = get_object_or_404(Option, code=uuid)
    if request.method == 'POST':
        form = OptionMenuForm(request.POST, instance=option)
        if form.is_valid():
            form = OptionMenuForm(request.POST, instance=option)
            form.save()
            return redirect('options_menu:options_menu_details_by_uuid', option.menu.uuid)
    else:
        form = OptionMenuForm(instance=option)
        form.save(commit=False)

    return render(request, 'option_menu_edit.html', {'form': form})


def options_menu_details_by_uuid(request, uuid):
    """
    options menu by uuid
    """
    menu = Menu.objects.filter(uuid=uuid)
    options = Option.objects.filter(menu_id=menu[0].id)

    context = {'menu': menu[0], 'options': options}

    return render(request, 'options_menu_details_by_uuid.html', context)
