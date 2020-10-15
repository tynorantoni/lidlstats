import os

class UploadHandler:

    def upload_img(self,img_file):
        img_upload_folder = 'lidlstatsPics/receipts'
        print('mamo jestem w handlerze')
        if not os.path.isdir(img_upload_folder):
            os.makedirs(img_upload_folder, exist_ok=True)
        with open(img_upload_folder, 'wb+') as destination:
            for chunk in img_file.chunks():
                destination.write(chunk)