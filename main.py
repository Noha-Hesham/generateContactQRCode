from readFiles import ReadExcelFile
from excel import Excel
from qr import QRCode



if __name__ == '__main__':

    excelFName = ReadExcelFile().getFile()

    excel = Excel()
    contactList = excel.reader()
    
    QR = QRCode()
    QR.generate(contactList)
    