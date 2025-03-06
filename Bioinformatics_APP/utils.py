import pandas as pd
import os
from datetime import datetime

now = datetime.now()
formated_run_time = now.strftime("%Y-%m-%d %H:%M:%S")

class pubdata:
    def __init__(
        self,
        Lab,
        UserID,
        PROJECT_NAME,
        ReadType,
        Reference,
        SRAID,
        SampleName,
        ReadLength,
        Description,
        saveDir,
    ):
        self.Lab = Lab
        self.UserID = UserID
        self.PROJECT_NAME = PROJECT_NAME
        self.ReadType = ReadType
        self.Reference = Reference
        # lists from here on:
        self.SRAIDs = SRAID
        self.SampleNames = SampleName
        self.ReadLength = ReadLength
        self.Descriptions = Description
        # The location of where the xlsx file will be saved
        self.saveDir = saveDir

    def public_xlsx_maker(self):
        # What to do with the lab and user ID? Maybe include them in the file name?
        data = {
            "GSE_ID": [self.PROJECT_NAME] * len(self.SRAIDs),
            "GSM_ID": self.SRAIDs,
            "SampleName": self.SampleNames,
            "ExprimentType": ["RNA-seq"] * len(self.SRAIDs),
            "ReadType": [self.ReadType] * len(self.SRAIDs),
            "ReadLength": [self.ReadLength] * len(self.SRAIDs),
            "Genome": [self.Reference] * len(self.SRAIDs),
            "Comments": [self.Descriptions] * len(self.SRAIDs),
        }

        df = pd.DataFrame(data)
        df.to_excel(os.path.join(self.saveDir,f"{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.xlsx"), index=False)

        return os.path.join(self.saveDir,f"{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.xlsx") # Return the path to the table
    
