import pandas as pd


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
        return df