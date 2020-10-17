from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import RegisterForm, AllShoppingsFromDB, UploadedImageForm
from .filehandler import FileHandler
from .models import CalculatedDataModel, BasicDataModel
from .statisticdevil import StatisticDevil


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
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            msg='Paragon został dodany, wkrótce zostanie przetworzony'
            return render(request, 'lidlstatsApp/upload.html', {'form': form,'img_obj':img_obj,'msg':msg})
    else:
        form = UploadedImageForm()
    return render(request, 'lidlstatsApp/upload.html', {'form': form})




def details(request):

    # query_results = BasicDataModel.objects.all()
    # location_list = AllShoppingsFromDB()
    #
    # context = {
    #     'query_results': query_results,
    #     'location_list': location_list
    # }
    # return render(request, 'lidlstatsApp/details.html', context)



    all_db_records = BasicDataModel.objects.all().reverse()[0]
    shopping_choices = AllShoppingsFromDB()

    table_df = StatisticDevil()
    column_names = {'name': 'Nazwa Produktu', 'amount': 'Ilość', 'price': 'Cena', 'sale': 'rabat', 'VAT': 'VAT'}
    table_to_show = table_df.make_yourself_a_table(all_db_records.product_data).rename(columns=column_names).to_html(
        classes='table table-light table-striped',
        justify='left'
    )
    # if request.method == "GET":
    #     print('w ifie')
    #     shopping_choices = AllShoppingsFromDB(request.POST)
    #     if shopping_choices.is_valid:
    #         print("im valid")
    #         # redirect to the url where you'll process the input
    #         return HttpResponseRedirect('lidlstatsApp/details/1')
    context = {'table_to_show': table_to_show,
               'shopping_choices': shopping_choices}

    return render(request, 'lidlstatsApp/details.html', context)




# def detail_of_shopping(request, id_of_shopping):

    # data_from_db = BasicDataModel.objects.get(id=id_of_shopping)
    #
    # table_df = StatisticDevil()
    # column_names = {'name': 'Nazwa Produktu', 'amount': 'Ilość', 'price': 'Cena', 'sale': 'rabat', 'VAT': 'VAT'}
    # table_to_show = table_df.make_yourself_a_table(data_from_db.product_data).rename(columns=column_names).to_html(
    #     classes='table table-light table-striped',
    #     justify='left'
    # )
    #
    # context = {'table_to_show': table_to_show}
    #
    #
    # return render(request, 'lidlstatsApp/details/<str:pk>',context)


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

