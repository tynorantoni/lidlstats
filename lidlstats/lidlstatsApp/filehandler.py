from .mails import Mails
from .receiptocr import ReceiptOCR
from background_task import background
from .models import BasicDataModel

class FileHandler():
    # @background(schedule=180)
    @staticmethod
    def manage_files():
        print('start ')
        new_mail = Mails.check_and_download()
        print('new mail ',new_mail)
        if new_mail == False:
            print('entering json loop ')
            list_to_save_in_db = ReceiptOCR.get_text_from_receipt('test')
            print("to ma być zapisane w DB ",list_to_save_in_db)
            # data_model = BasicDataModel.objects.create()

            for element in list_to_save_in_db:
                print('element z ostatniej pętli ',element)
                BasicDataModel.objects.create(product_data=element)

        print('stop')

