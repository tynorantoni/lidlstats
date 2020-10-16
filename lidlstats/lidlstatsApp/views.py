from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect
from .forms import RegisterForm, ImageUpload, AllShoppingsFromDB
from .filehandler import FileHandler
from .models import CalculatedDataModel, BasicDataModel
from .statisticdevil import StatisticDevil
from .uploadhandler import UploadHandler


@login_required(login_url='/')
def index(request):
    FileHandler.manage_files()
    shopping_data = CalculatedDataModel.objects.all()
    data_to_show = CalculatedDataModel.objects.get(id=1)  # hmmmmm??
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
               'total_shopping_cost': round(total_shopping_cost, 2),
               'min_cost': round(min_cost[0], 2),
               'min_cost_date': min_cost[1],
               'max_cost': round(max_cost[0], 2),
               'max_cost_date': max_cost[1]
               }

    return render(request, 'lidlstatsApp/index.html', context)


def upload_file(request):
    new_img = UploadHandler()
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            print('form jest validą')
            new_img.upload_img(request.FILES['file'])
            FileHandler.manage_files()
            return render(request, 'lidlstatsApp/upload.html', {'form': form})  # HttpResponseRedirect('/success/url/')
    else:
        form = ImageUpload()
    return render(request, 'lidlstatsApp/upload.html', {'form': form})


def details(request):
    all_db_records = BasicDataModel.objects.all()
    shopping_choices = AllShoppingsFromDB()

    table_df = StatisticDevil()
    column_names = {'name': 'Nazwa Produktu', 'amount': 'Ilość', 'price': 'Cena', 'sale': 'rabat', 'VAT': 'VAT'}
    # table_to_show = table_df.make_yourself_a_table(data_from_db.product_data).rename(columns=column_names).to_html(
    #     classes='table table-light table-striped',
    #     justify='left'
    # )

    context = {  # 'table_to_show': table_to_show,
        'all_db_records': all_db_records,
        'shopping_choices': shopping_choices}

    return render(request, 'lidlstatsApp/details.html', context)


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
