from .mails import Mails
from .receiptocr import ReceiptOCR
from background_task import background
from .models import BasicDataModel
import time
class FileHandler():

    @staticmethod
    @background(schedule=180)
    def manage_files():
        print('start ')
        # new_mail = Mails.check_and_download()
        # print('new mail ',new_mail)
        # if new_mail == True:
        #     print('entering json loop ')
        #     list_to_save_in_db = ReceiptOCR.get_text_from_receipt()
        #     data_model = BasicDataModel()
        #     for element in list_to_save_in_db:
        #         data_model.save(element)

        print('stop')

