import pandas as pd

from lidlstatsApp.models import BasicDataModel


class StatisticDevil:

    def take_out_my_json(self, id_from_db):
        jsonSample = BasicDataModel.objects.get(pk=id_from_db)
        return jsonSample.product_data

    def make_yourself_a_table(self, json_from_db):
        tables = pd.read_json(json_from_db)
        tables = tables.astype(str)
        tables = tables.apply(lambda x: x.str.replace(',', '.'))
        tables_trans = tables.transpose()

        return tables_trans

    def calculate_max_cost(self, data_table_set):
        numTabl = pd.to_numeric(data_table_set['price'])
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
        df_count = data_table_set.loc[data_table_set['VAT'] == 'A']
        df_count['vatA'] = (float(df_count['price']) * 0.23)
        return round(df_count['vatA'].sum(),2)

    def calculate_vat_b(self, data_table_set):
        df_count = data_table_set.loc[data_table_set['VAT'] == 'B']
        df_count['vatB'] = (float(df_count['price']) * 0.08)
        return round(df_count['vatB'].sum(),2)

    def calculate_vat_c(self, data_table_set):
        try:
            df_count = data_table_set.loc[data_table_set['VAT'] == 'C']
            df_count['vatC'] = (float(df_count['price']) * 0.05)
            return round(df_count['vatC'].sum(),2)
        except TypeError:
            return 0

    def chart_histogram(self):
        pass

    def chart_pie(self):
        pass

    def chart_line(self):
        pass

