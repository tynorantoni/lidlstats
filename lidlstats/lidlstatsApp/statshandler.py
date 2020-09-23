from .statisticdevil import StatisticDevil
from .models import CalculatedDataModel

class StatsHandler():


    def lets_make_a_data(shopping_id):
        calculations = CalculatedDataModel.objects.create()
        json = StatisticDevil.take_out_my_json(shopping_id)
        data_frame = StatisticDevil.make_yourself_a_table(json)
        calculations.total_cost(StatisticDevil.calculate_sum(data_frame)).save()