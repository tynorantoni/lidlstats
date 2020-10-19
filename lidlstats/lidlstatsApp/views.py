from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, UploadedImageForm
from .filehandler import FileHandler
from .models import CalculatedDataModel, BasicDataModel
from .statisticdevil import StatisticDevil


@login_required(login_url='/')
def index(request):
    FileHandler.manage_files()
    list_of_all_shoppings = BasicDataModel.objects.all()
    shopping_data = CalculatedDataModel.objects.all()
    no_of_shop = shopping_data.count()
    total_shopping_cost = 0
    # max_cost=shopping_data.aggregate(Max('total_cost'))   stay in touch
    min_max_values = shopping_data.order_by('total_cost')
    max_cost = min_max_values.last().total_cost, min_max_values.last().date_of_shoppings
    min_cost = min_max_values[0].total_cost, min_max_values[0].date_of_shoppings

    for cost in shopping_data:
        total_shopping_cost += cost.total_cost

    context = {'no_of_shop': no_of_shop,
               'total_shopping_cost': round(total_shopping_cost, 2),
               'min_cost': round(min_cost[0], 2),
               'min_cost_date': min_cost[1],
               'max_cost': round(max_cost[0], 2),
               'max_cost_date': max_cost[1],
               'list_of_all_shoppings': list_of_all_shoppings
               }

    return render(request, 'lidlstatsApp/index.html', context)


def upload_file(request):
    list_of_all_shoppings = BasicDataModel.objects.all()
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            msg = 'Paragon został dodany, wkrótce zostanie przetworzony'
            return render(request, 'lidlstatsApp/upload.html', {'form': form,
                                                                'img_obj': img_obj,
                                                                'msg': msg,
                                                                'list_of_all_shoppings': list_of_all_shoppings
                                                                })
    else:
        form = UploadedImageForm()
    return render(request, 'lidlstatsApp/upload.html', {'form': form, 'list_of_all_shoppings': list_of_all_shoppings})


def detail_of_shopping(request, id_of_shopping):
    list_of_all_shoppings = BasicDataModel.objects.all()
    shopping_db_record = list_of_all_shoppings.get(pk=id_of_shopping)
    shopping_data = CalculatedDataModel.objects.get(shoppig_id=id_of_shopping)

    table_df = StatisticDevil()
    column_names = {'name': 'Nazwa Produktu', 'amount': 'Ilość', 'price': 'Cena', 'sale': 'rabat', 'VAT': 'VAT'}
    table_to_show = table_df.make_yourself_a_table(shopping_db_record.product_data).rename(
        columns=column_names).to_html(
        classes='table table-light table-bordered table-hover table-striped ',
        justify='left'
    )
    no_of_bought_items = len(table_df.make_yourself_a_table(shopping_db_record.product_data))
    total_vat = round((shopping_data.vat_a + shopping_data.vat_b + shopping_data.vat_c), 2)
    net_value = round((shopping_data.total_cost - total_vat), 2)
    tax_value = round(((total_vat / shopping_data.total_cost) * 100), 2)
    vat_a_value = round(((shopping_data.vat_a / total_vat) * 100), 2)
    vat_b_value = round(((shopping_data.vat_b / total_vat) * 100), 2)
    vat_c_value = round(((shopping_data.vat_c / total_vat) * 100), 2)

    values_of_shopping = {'total_vat': total_vat,
                          'net_value': net_value,
                          'tax_value': tax_value,
                          'vat_a_value': vat_a_value,
                          'vat_b_value': vat_b_value,
                          'vat_c_value': vat_c_value,
                          'no_of_bought_items': no_of_bought_items}

    context = {'table_to_show': table_to_show,
               'shopping_bd_record': shopping_db_record,
               'list_of_all_shoppings': list_of_all_shoppings,
               'shopping_data': shopping_data,
               'values_of_shopping': values_of_shopping
               }

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
