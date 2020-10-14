from .mails import Mails
from .receiptocr import ReceiptOCR
from background_task import background
from .models import BasicDataModel
from .models import CalculatedDataModel
from .statisticdevil import StatisticDevil
from .statshandler import StatsHandler


class FileHandler:

    # @background(schedule=3600)
    @staticmethod
    def manage_files():
        print('start ')

        new_mail = Mails()
        list_to_save_in_db = ReceiptOCR()

        new_mail.check_and_download()
        print('new mail ', new_mail)
        if new_mail == True:
            print('entering json loop ')

            list_to_save_in_db.get_text_from_receipt()
            print("to ma być zapisane w DB ", list_to_save_in_db)
            try:
                for element in list_to_save_in_db:
                    print('element z ostatniej pętli ', element)
                    BasicDataModel.objects.create(date_of_shopping=element[1], product_data=element[0]) #in one line, or two? tuple problem?
            except Exception as e:
                raise e
            else:
                FileHandler.data_transfer()

        print('stop')

    @staticmethod
    def data_transfer():
        statistic_handling = StatsHandler()
        chart_maker = StatisticDevil()
        json_data = BasicDataModel.objects.all()
        shopping_data = CalculatedDataModel.objects.all()

        for element in json_data:

            if not shopping_data.objects.filter(shoppig_id=element.id).exists():
                statistic_handling.lets_make_a_data()
            else:
                continue

        chart_maker.chart_bar()