import pandas as pd

class pubdata:
    def __init__(self, Lab, UserID, PROJECT_NAME, ReadType, Reference, SRAID, SampleName, Description):
        self.Lab = Lab
        self.UserID = UserID
        self.PROJECT_NAME = PROJECT_NAME
        self.ReadType = ReadType
        self.Reference = Reference
        self.SRAIDs = SRAID
        self.SampleNames = SampleName
        self.Descriptions = Description
    
    