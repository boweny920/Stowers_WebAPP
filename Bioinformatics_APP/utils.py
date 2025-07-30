import pandas as pd
import os
from datetime import datetime
import subprocess
from pathlib import Path
from django.conf import settings

class pubdata_run:

    def __init__(
        self,
        ID_Set="Default_SampleID",
        Lab="Default_Lab",
        UserID="Default_UserID",
        Reference="Default_Reference",
        Analysis="Default_Analysis",
    ):
        self.ID_Set = ID_Set  # Split the input by '|'
        self.Lab = Lab
        self.UserID = UserID
        self.Reference = "=".join(Reference
                                    .replace("Genome Version:", "")
                                    .replace("Annotation:", "")
                                    .replace(" ", "")
                                    .split(";")[1:]) 
        self.Analysis = Analysis

    def species_genome_annotation_nameMake(self) -> list:
        """
        Generates the species-genome-annotation names collection based on the sample sheet.
        """
        roboindex_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'static', 'tables', 'sampleSheet_ROBOINDEX_2023.csv'))
        # roboindex_df = roboindex_df.sort_values(by='name') # Sort the DataFrame by 'name' column
        genome_ver_list = [f"{row['name']}; Genome Version: {row['id']}; Annotation: {row['annotation_version']}" for _, row in roboindex_df.iterrows()]
        return genome_ver_list
    
    def ID_Csv_maker(self):
        """
        Creates a CSV file with the Sample IDs.
        """
        df = pd.DataFrame(self.ID_Set, columns=["SampleID"])
        
        # Define the path for the CSV file
        now = datetime.now()
        formated_run_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        run_folder = settings.CSV_DIR / f"{self.UserID}_{self.Lab}_{formated_run_time}"
        
        if not run_folder.exists():
            run_folder.mkdir(parents=True, exist_ok=True)

        csv_file_path = run_folder / f"{self.UserID}_{self.Lab}_{formated_run_time}_{self.Analysis}+{self.Reference}.csv"
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False, header=False)
        return csv_file_path