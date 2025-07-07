import pandas as pd
import os
from datetime import datetime
import subprocess
from pathlib import Path
from django.conf import settings

now = datetime.now()
formated_run_time = now.strftime("%Y-%m-%d_%H:%M:%S")
roboindex_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'static', 'tables', 'sampleSheet_ROBOINDEX_2023.csv'))
genome_ver_dic = {row['name']: row['id'] for _, row in roboindex_df.iterrows()}

class pubdata_run:

    def __init__(
        self,
        ID_Set,
        Lab,
        UserID,
        Reference,
    ):
        self.ID_Set = ID_Set  # Split the input by '|'
        self.Lab = Lab
        self.UserID = UserID
        self.Reference = Reference

    def ID_Csv_maker(self):
        """
        Creates a CSV file with the Sample IDs.
        """
        df = pd.DataFrame(self.ID_Set, columns=["SampleID"])
        # Define the path for the CSV file
        run_folder = settings.CSV_DIR / f"{self.UserID}_{self.Lab}_{formated_run_time}"
        if not run_folder.exists():
            run_folder.mkdir(parents=True, exist_ok=True)
        csv_file_path = run_folder / f"{self.UserID}_{self.Lab}_{formated_run_time}+{genome_ver_dic[self.Reference]}.csv"
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False, header=False)
        return csv_file_path

    # def run_nextflow(self, xls_file_path: Path):
    #     log_file = settings.NEXTFLOW_DIR / "log" / f"{self.UserID}_{self.Lab}_{formated_run_time}.nextflow.log"
    #     cmd = []
        # subprocess.run(["nextflow", "run", "/n/ngs/tools/SECUNDO3/Scundo3_v4.2/main.nf", 
        #                 "--public_dataxlsx", xls_file_path.resolve(), 
        #                 '--lab', self.Lab, '--requester', self.UserID, '--user_email', f"{self.UserID}@stowers.org" ], 
        #                text=True, stdout=log_file, stderr=subprocess.STDOUT)