import cv2
import pytesseract
from PIL import Image
import json
import re

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = Image.open('lidlstatsPics/11.jpg')
img2 = cv2.imread('lidlstatsPics/11.jpg')

text = pytesseract.image_to_string(img)

data_rows = text.split('\n')
data_row_dict = {}
step = 0
id_row = 0
sale = ''
# Jaja wol.wyb.M,L, XL 1 * 6,99 6,99 C
for i in data_rows:
    step += 1
    if re.match('\d+-\d+-\d+', i):
        for j in data_rows[step:]:
            if re.match('(PTU)', j):
                break
            if len(j.split(' ')) <= 5:

                try:
                    sale = re.search('(......)$',j).group(1)
                except AttributeError:
                    sale=''

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

print(data_row_dict)
#
# dżejPl = json.dumps(finaldata)
dżej = json.dumps(data_row_dict)
#
# print('Pl\n',dżejPl)
print('\nEcce Dżejson\n',dżej)


