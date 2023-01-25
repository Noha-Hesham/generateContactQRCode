from readFiles import ReadExcelFile
import pandas as pd
import openpyxl as xl
import ast
import json



class Excel:
    def __init__(self):
        pass
    
    
    def reader(file):
        file = ReadExcelFile.fName
        finalContactList = []
        contactsDF = pd.read_excel(file)
        contactsSTR = contactsDF.to_json(orient='records')
        
        contactsList=ast.literal_eval(contactsSTR)
        
        for contact in contactsList:
            contact["Phone_Number"] = str(contact["Phone_Number"])
            
            if contact["Phone_Number"].startswith('0'):
                continue
            else:
                contact["Phone_Number"] = '0' + contact["Phone_Number"]

        return contactsList
