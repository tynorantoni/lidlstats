import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lidlstatsApp.models import BasicDataModel, CalculatedDataModel


class StatisticDevil:

    def take_out_my_json(self, id_from_db):
        jsonSample = BasicDataModel.objects.get(pk=id_from_db)
        return jsonSample.product_data, jsonSample.date_of_shopping

    def make_yourself_a_table(self, json_from_db):
        if json_from_db:
            tables = pd.read_json(json_from_db)
            tables = tables.astype(str)
            tables = tables.apply(lambda x: x.str.replace(',', '.'))
            tables_trans = tables.transpose()

            return tables_trans
        else:
            tables = pd.DataFrame()
            return tables

    def calculate_max_cost(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            numTabl = pd.to_numeric(data_table_set['price'])
            return numTabl.max()

    def calculate_min_cost(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            numTabl = pd.to_numeric(data_table_set['price'])
            return numTabl.min()

    def calculate_mean_cost(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            numTabl = pd.to_numeric(data_table_set['price'])
            return numTabl.mean()

    def calculate_median_of_costs(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            numTabl = pd.to_numeric(data_table_set['price'])
            return numTabl.median()

    def calculate_sum(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            numTabl = pd.to_numeric(data_table_set['price'])
            return numTabl.sum()

    def calculate_vat_a(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            try:
                df_count = data_table_set.loc[data_table_set['VAT'] == 'A']
                df_count['vatA'] = pd.to_numeric(df_count['price'])*pd.to_numeric(df_count['amount']) * 0.23
                print(df_count)
                return round(df_count['vatA'].sum(),2)
            except TypeError as e:
                print(e)
                return 0

    def calculate_vat_b(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            try:
                df_count = data_table_set.loc[data_table_set['VAT'] == 'B']
                df_count['vatB'] = pd.to_numeric(df_count['price'])*pd.to_numeric(df_count['amount']) * 0.08
                return round(df_count['vatB'].sum(),2)
            except TypeError as e:
                print(e)
                return 0

    def calculate_vat_c(self, data_table_set):
        if data_table_set.empty:
            return 0
        else:
            try:
                df_count = data_table_set.loc[data_table_set['VAT'] == 'C']
                df_count['vatC'] = pd.to_numeric(df_count['price'])*pd.to_numeric(df_count['amount']) * 0.05
                return round(df_count['vatC'].sum(),2)
            except TypeError as e:
                print(e)
                return 0

    def chart_bar(self):
        chart_folder="lidlstatsApp/static/lidlstatsPics/charts/"
        amount_of_cash = []
        date_of_shopping = []
        shopping_data = CalculatedDataModel.objects.all()

        if not os.path.isdir(chart_folder):
            os.makedirs(chart_folder, exist_ok=True)

        for cost in shopping_data:
            amount_of_cash.append(cost.total_cost)
            date_of_shopping.append(cost.date_of_shoppings)


        y_pos = np.arange(len(amount_of_cash))

        plt.figure(figsize=(13, 5))

        # Create bars
        plt.bar(y_pos, amount_of_cash, color='#36b9cc')
        for index, value in enumerate(amount_of_cash):
            plt.text(index, value + 0.1, str(value))
        plt.xticks(y_pos, date_of_shopping)
        plt.xlabel('Data zakupów', fontsize=12, color='#030303')
        plt.ylabel('Koszt zakupów [PLN]', fontsize=12, color='#030303')
        plt.title('Twoje ostatnie zakupy w Lidlu', fontsize=16, color='#030303')
        file_name = "totalbar"

        if os.path.exists(f"{chart_folder}/{file_name}"):
            os.remove(f"{chart_folder}/{file_name}")

        plt.savefig(f"{chart_folder}/{file_name}")

    def chart_pie(self):
        pass

    def chart_line(self):
        pass

