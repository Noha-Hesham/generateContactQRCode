import os

class ReadExcelFile:
    fName = None
    def __init__(self):
        pass

    @classmethod
    def getFile(cls):
        '''
        Info: get xlsx from The Directory

        Requirments: must have only one xslx files in the script directory
        Input: No input
        Output: excel file Name
        '''

        fPath = os.path.join(os.getcwd())
        filesList = os.listdir(fPath)
        for file in filesList:
            if '.xlsx' in file:
                cls.fName = file