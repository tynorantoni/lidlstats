import os
from imbox import Imbox
import traceback


class Mails():

    @staticmethod
    def check_and_dowload(self):

        imap_ssl_host = 'imap.poczta.onet.pl'
        username = 'lidl.app@spoko.pl'
        password = 'ARp<s/<]`Z82c?F6'
        download_folder = "./lidlstatsPics"

        if not os.path.isdir(download_folder):
            os.makedirs(download_folder, exist_ok=True)

        mail = Imbox(imap_ssl_host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
        messages = mail.messages(unread=True)

        for (uid, message) in messages:
            mail.mark_seen(uid)

            for idx, attachment in enumerate(message.attachments):
                try:
                    att_fn = attachment.get('filename')
                    download_path = f"{download_folder}/{att_fn}"
                    print(download_path)
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get('content').read())
                except:
                    pass
                    print(traceback.print_exc())

        mail.logout()
