

class UploadHandler:

    def upload_img(self,img_file):
        img_upload_folder = 'lidlstatsApp/static/lidlstatsPics/receipts'
        with open(img_upload_folder, 'wb+') as destination:
            for chunk in img_file.chunks():
                destination.write(chunk)