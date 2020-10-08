from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .filehandler import FileHandler
from .models import CalculatedDataModel


@login_required(login_url='/')
def index(request):
    FileHandler.manage_files()
    data_to_show = CalculatedDataModel.objects.get(id=26)
    context = {'data_to_show':data_to_show}
    return render(request, 'lidlstatsApp/index.html', context)


def data(request):
    context = {}
    return render(request, 'lidlstatsApp/data.html', context)


def user_settings(request):
    context = {}

    return render(request, 'lidlstatsApp/user.html', context)


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, 'registration/register.html', {'form': form})

# def login(request)
# def logout(request)
