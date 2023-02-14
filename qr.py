from segno import helpers
import os
import shutil

class QRCode:
    def __init__(self):
        self.creatImageDir()




    def creatImageDir(self):
        dirName= 'QR_Codes'
        path = os.path.join(os.getcwd(), dirName)
        while True:
            if not os.path.exists(path):
                os.mkdir(path)
                break
            else:
                ask = input(f'{dirName} is already exists, you wanna replace it ?? (y/n)')
                if ask == 'y':
                    shutil.rmtree(path)
                    os.mkdir(path)
                    break
                elif ask == 'n':
                    break
                else:
                    continue
                
                

        return dirName

    def mvImg(self):
        imgList = []
        fromDir = os.getcwd()
        toDir = os.path.join(fromDir, 'QR_Codes')
        filesList = os.listdir(fromDir)
        for file in filesList:
            if file.endswith('.png'):
                imgList.append(file)
                shutil.move(f'{fromDir}/{file}', f'{toDir}/{file}')




    def generate(self, contactList):
        for contact in contactList:

            name = contact["Name"]
            position = contact["Position"]
            mail = contact["Email"]
            phoneNum = contact["Phone_Number"]
            url = contact["Url"]
            country = contact["Country"]
            city = contact["City"]

            #(name, reading, email, phone, videophone, memo, nickname, birthday, url, pobox, roomno, houseno, city, prefecture, zipcode, country)
            qrcode = helpers.make_mecard(
                name= name ,
                email= mail,
                phone= phoneNum,
                nickname= position,
                url= url,
                country= country,
                city= city,
            )
            
            qrcode.designator
            qrcode.save(f'{name}.png', scale=4)
            self.mvImg()

        print('QR_Codes Generated Sucessfully \U0001f600')






