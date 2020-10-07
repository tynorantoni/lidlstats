from .mails import Mails
from .receiptocr import ReceiptOCR
from background_task import background
from .models import BasicDataModel


class FileHandler:

    # @background(schedule=3600)
    @staticmethod
    def manage_files():
        print('start ')
        new_mail = Mails()
        new_mail.check_and_download()
        print('new mail ', new_mail)
        if new_mail == True:
            print('entering json loop ')
            list_to_save_in_db = ReceiptOCR()
            list_to_save_in_db.get_text_from_receipt()
            print("to ma być zapisane w DB ", list_to_save_in_db)

            for element in list_to_save_in_db:
                print('element z ostatniej pętli ', element)
                BasicDataModel.objects.create(date_of_shopping=element[1], product_data=element[0]) #in one line, or two? tuple problem?

        print('stop')
