from .statisticdevil import StatisticDevil
from .models import CalculatedDataModel


class StatsHandler:

    def lets_make_a_data(self, shopping_id):
        shopping_data_frame = StatisticDevil()
        calculations = CalculatedDataModel.objects.create()
        json = shopping_data_frame.take_out_my_json(shopping_id)
        data_frame = shopping_data_frame.make_yourself_a_table(json)
        calculations.total_cost(shopping_data_frame.calculate_sum(data_frame)).save()
