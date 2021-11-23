import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A83hqGALkHa8WevUraFi7F_jHC6Yu6gVLASnoZr9m0nTN0gIv6dYWKKoRfOSirXdqelaWoEEZFDD4wTZJSiTERKhvHk7HioK2P9QNX2dgkVMXK-h0TgsSa05FaVE4XVbZ_RVCdbjE7I'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/ngupt/OneDrive/Desktop/Python/Functions/text1.txt'
    file_to = '/Cloud storage/text1.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()