from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect
from .forms import RegisterForm, ImageUpload
from .filehandler import FileHandler
from .models import CalculatedDataModel
from .uploadhandler import UploadHandler


@login_required(login_url='/')
def index(request):
    FileHandler.manage_files()
    shopping_data = CalculatedDataModel.objects.all()
    data_to_show = CalculatedDataModel.objects.get(id=1)
    no_of_shop = shopping_data.count()
    total_shopping_cost = 0
    # max_cost=shopping_data.aggregate(Max('total_cost'))   stay in touch
    min_max_values = shopping_data.order_by('total_cost')
    max_cost = min_max_values.last().total_cost, min_max_values.last().date_of_shoppings
    min_cost = min_max_values[0].total_cost, min_max_values[0].date_of_shoppings

    for cost in shopping_data:
        total_shopping_cost += cost.total_cost


    context = {'data_to_show': data_to_show,
               'no_of_shop': no_of_shop,
               'total_shopping_cost': round(total_shopping_cost,2),
               'min_cost': round(min_cost[0],2),
               'min_cost_date':min_cost[1],
               'max_cost': round(max_cost[0],2),
               'max_cost_date':max_cost[1]
               }
    return render(request, 'lidlstatsApp/index.html', context)


def upload_file(request):
    new_img = UploadHandler()
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            new_img.upload_img(request.FILES['file']) #
            return render(request, 'upload.html', {'form': form}) # HttpResponseRedirect('/success/url/')
    else:
        form = ImageUpload()
    return render(request, 'upload.html', {'form': form})

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
