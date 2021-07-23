from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from menu.models import Menu
from option.forms import OptionMenuForm
from option.models import Option


@login_required(login_url="/accounts/login")
def option_add(request, uuid):
    """
    Validates the request to add a new Option
    """
    if request.method == 'POST':
        form = OptionMenuForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['description']
            menu = Menu.objects.filter(uuid=uuid)
            Option.objects.create(menu_id=menu[0].id, description=description, code=uuid4()).save()
            return redirect('menu:details_uuid', uuid)
    else:
        form = OptionMenuForm()

    return render(request, 'option_add.html', {'form': form})
