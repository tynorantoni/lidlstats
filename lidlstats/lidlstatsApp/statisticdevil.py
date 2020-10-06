import pandas as pd

from lidlstatsApp.models import BasicDataModel


class StatisticDevil:

    def take_out_my_json(self, shopping_id):  # niech przyjmuje ID i zwraca jsona
        jsonSample = BasicDataModel.objects.get(pk=shopping_id)

        return jsonSample.product_data

    def make_yourself_a_table(self, json_from_db):
        tables = pd.read_json(json_from_db)
        tables_trans = tables.transpose()
        tables_trans = tables_trans.apply(lambda x: x.str.replace(',', '.'))
        return tables_trans

    def calculate_max_cost(self, data_table_set):
        numTabl = pd.to_numeric(self, data_table_set['price'])
        return numTabl.max()

    def calculate_min_cost(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.min()

    def calculate_mean_cost(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.mean()

    def calculate_median_of_costs(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.median()

    def calculate_sum(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.sum()

    def calculate_vat_a(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.sum()

    def calculate_vat_b(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.sum()

    def calculate_vat_c(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
        return numTabl.sum()

    def chart_histogram(self):
        pass

    def chart_pie(self):
        pass

    def chart_line(self):
        pass
