from .models import CalculatedDataModel
from .statisticdevil import StatisticDevil


class StatsHandler:

    def lets_make_a_data(self, id_from_db):
        shopping_data_frame = StatisticDevil()
        json = shopping_data_frame.take_out_my_json(id_from_db)
        data_frame = shopping_data_frame.make_yourself_a_table(json)
        CalculatedDataModel.objects.create(shopping_id=id_from_db,
                                           total_cost=shopping_data_frame.calculate_sum(data_frame),
                                           vat_a=shopping_data_frame.calculate_vat_a(),
                                           vat_b=shopping_data_frame.calculate_vat_b(),
                                           vat_c=shopping_data_frame.calculate_vat_c(),
                                           max_price=shopping_data_frame.calculate_max_cost(),
                                           min_price=shopping_data_frame.calculate_min_cost(),
                                           mean_cost=shopping_data_frame.calculate_mean_cost(),
                                           median_cos=shopping_data_frame.calculate_median_cost()
                                           )
