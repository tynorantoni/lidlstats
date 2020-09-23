import os
import pytesseract
from PIL import Image
import json
import re
from .models import BasicDataModel


class ReceiptOCR():

    def __init__(self):
        return self

    def get_text_from_receipt(self):
        download_folder = "./lidlstatsPics"
        complete_folder = "./lidlstatsPics/complete"
        list_of_jsons=[]
        if not os.path.isdir(complete_folder):
            os.makedirs(complete_folder, exist_ok=True)

        for file_name in os.listdir(download_folder):
            if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
                pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                img = Image.open(download_folder+"/" + file_name)
                text = pytesseract.image_to_string(img)
                data_rows = text.split('\n')
                list_of_jsons.append(ReceiptOCR.to_json_from_list(data_rows))
                os.rename(f"{download_folder}/{file_name}", f"{complete_folder}/{file_name}")
            else:
                continue

        return list_of_jsons

    def to_json_from_list(list_from_receipt):
        name= ''
        amount= ''
        price= ''
        sale= ''
        vat = ''
        data_row_dict = {}
        step = 0
        id_row = 0
        # sale = ''

        for i in list_from_receipt:
            step += 1
            if re.match('\d+-\d+-\d+', i):
                for j in list_from_receipt[step:]:
                    if re.match('(PTU)', j):
                        break
                    if len(j.split(' ')) <= 5:

                        try:
                            sale = re.search('(......)$', j).group(1)
                            data_row_dict[id_row] = {'name': name,
                                                           'amount': amount,
                                                           'price': price,
                                                           'sale': sale,
                                                           'VAT': vat
                                                     }
                            sale=''

                        except AttributeError:
                            sale = ''

                    else:
                        id_row += 1
                        temporary_data_row = j.split(' ')
                        name = temporary_data_row[:-5]
                        try:
                            if re.match('\d+', temporary_data_row[-4]):
                                amount = temporary_data_row[-4]
                            else:
                                amount = temporary_data_row[-5]
                        except:
                            print('shit happened', id_row, temporary_data_row)
                        price = temporary_data_row[-3]
                        vat = temporary_data_row[-1]

                        data_row_dict.update({id_row: {'name': name,
                                                       'amount': amount,
                                                       'price': price,
                                                       'sale': sale,
                                                       'VAT': vat}
                                              })
                        temporary_data_row.clear()

        receipt_json = json.dumps(data_row_dict)
        print(receipt_json)
        return receipt_json
