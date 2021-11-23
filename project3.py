import os 
import dropbox


def uploaddropbox(file):
    dropbox_access_token= "sl.A83hqGALkHa8WevUraFi7F_jHC6Yu6gVLASnoZr9m0nTN0gIv6dYWKKoRfOSirXdqelaWoEEZFDD4wTZJSiTERKhvHk7HioK2P9QNX2dgkVMXK-h0TgsSa05FaVE4XVbZ_RVCdbjE7I"    #Enter your own access token
    dropbox_path= "/Cloud storage/"+file
    computer_path="C:/Users/ngupt/OneDrive/Desktop/Python/Functions/"+file

    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))



k = os.listdir('C:/Users/ngupt/OneDrive/Desktop/Python/Functions')
print(k)

for a in k:
    h= os.path.splitext(a)
    print(h[1])
    f = h[1]

    if f=='.py':
        uploaddropbox(a)

