from .models import CalculatedDataModel
from .statisticdevil import StatisticDevil


class StatsHandler:

    def lets_make_a_data(self, id_from_db):
        shopping_data_frame = StatisticDevil()
        json = shopping_data_frame.take_out_my_json(id_from_db)
        print('json[0] ',json[0],' json[1] ',json[1])
        data_frame = shopping_data_frame.make_yourself_a_table(json[0])
        CalculatedDataModel.objects.create(shoppig_id=id_from_db,
                                           date_of_shoppings=json[1],
                                           total_cost=shopping_data_frame.calculate_sum(data_frame),
                                           vat_a=shopping_data_frame.calculate_vat_a(data_frame),
                                           vat_b=shopping_data_frame.calculate_vat_b(data_frame),
                                           vat_c=shopping_data_frame.calculate_vat_c(data_frame),
                                           max_price=shopping_data_frame.calculate_max_cost(data_frame),
                                           min_price=shopping_data_frame.calculate_min_cost(data_frame),
                                           mean_cost=shopping_data_frame.calculate_mean_cost(data_frame),
                                           median_cost=shopping_data_frame.calculate_median_of_costs(data_frame)
                                           )
