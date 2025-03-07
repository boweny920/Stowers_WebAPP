import pandas as pd
import os
from datetime import datetime
import subprocess
from pathlib import Path

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
            "ReadLength": self.ReadLength,
            "Genome": [self.Reference] * len(self.SRAIDs),
            "Comments": self.Descriptions,
        }
        
        df = pd.DataFrame(data)
        df.to_excel(os.path.join(self.saveDir,f"{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.xlsx"), index=False)

        return os.path.join(self.saveDir,f"{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.xlsx") # Return the path to the table
    
    def run_nextflow(self, xls_file_path):
        log_file = self.saveDir.parent / f"/nextflow/log/{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.nextflow.log"
        subprocess.run(["nextflow", "run", "/n/ngs/tools/SECUNDO3/Scundo3_v4.2/main.nf", 
                        "--public_dataxlsx", Path(xls_file_path).resolve(), 
                        '--lab', self.Lab, '--requester', self.UserID, '--user_email', f"{self.UserID}@stowers.org" ], 
                       text=True, stdout=log_file, stderr=subprocess.STDOUT)

    def script_nextflow(self, xls_file_path):
        log_file = self.saveDir.parent / f"/nextflow/log/{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.nextflow.log"
        run_cmd = f"nextflow run /n/ngs/tools/SECUNDO3/Scundo3_v4.2/main.nf \
            --public_dataxlsx {Path(xls_file_path).resolve()} \
            --lab {self.Lab} --requester {self.UserID} \
            --user_email {self.UserID}@stowers.org > {log_file}"
        script_file = self.saveDir.parent / f"/nextflow/log/{self.UserID}_{self.PROJECT_NAME}_{formated_run_time}.nextflow.sh"
        with open(script_file, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write(run_cmd)
        
