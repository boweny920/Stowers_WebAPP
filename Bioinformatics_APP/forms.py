from django import forms
from django.conf import settings
import pandas as pd
import os 
from django.conf import settings
from .utils import pubdata_run


genomes = pubdata_run().species_genome_annotation_nameMake()
GENOMES = [(i, i) for i in genomes]
LABS = [(line.strip(), line.strip()) for line in open(os.path.join(settings.BASE_DIR, 'static', 'tables', 'labs.txt')).readlines()]


class PublicDataForm(forms.Form):
    
    Lab = forms.ChoiceField(choices=LABS, 
                            widget=forms.Select(attrs={'placeholder': 'Choose Your lab', 'rows': 1, 'cols': 20})
    )
    
    UserID = forms.CharField(max_length=10, required=True,
                            widget=forms.Textarea(attrs={'placeholder': 'e.g. by2747', 'rows': 1, 'cols': 15})
                            )

    Analysis = forms.ChoiceField(choices=[('bulk-RNA-Seq', 'bulk-RNA-Seq'), ('Download-Fastqs', 'Download-Fastqs')], # DO NOT include "_" in the choices!
                                widget=forms.Select(attrs={'placeholder': 'Choose Your Analysis Type', 'rows': 2, 'cols': 25})
                                )
    
    Reference = forms.ChoiceField(choices=GENOMES, 
                                widget=forms.Select(attrs={'placeholder': 'Choose One Genome Per Submission', 'rows': 2, 'cols': 20})
                                )
    
    Identifiers = forms.CharField(max_length=2000, required=True, 
                            widget=forms.Textarea(attrs={'placeholder': 
                            'e.g.\n'
                            'SRA123456\n'
                            'SRR123456\n'
                            'SRX8171613\n'
                            'GSE123456\n'
                            'GSM123456\n'
                            'ERR4007730\n'
                            'ERX4009132\n'
                            'DRR171822\n'
                            'DRX123456','rows': 4, 'cols': 18})
                            )

    
    def clean_Identifiers(self):
        data = self.cleaned_data['Identifiers']
        # Consider security issues with the input
        if "/bin/bash" in data or "/bin/sh" in data:
            raise forms.ValidationError("Invalid input detected in Identifiers. Please check your input.")
        if "rm" in data or "mv" in data:
            raise forms.ValidationError("Invalid input detected in Identifiers. Please check your input.")

        # Make sure you have SRA IDs in the input 
        ids = str(data.upper()).split('\n')
        allowed_IDs = ["SRA", "SRR", "SRX", "GSE", "GSM", "ERR", "ERX", "DRR", "DRX"]
        checkallIDs = all( # This checks if all IDs start with one of the allowed prefixes
                        any(v.startswith(prefix) for prefix in allowed_IDs)
                        for v in ids
                        )
        if not checkallIDs:
            raise forms.ValidationError("Identifiers field must contain one of the allowed IDs (e.g., 'SRA', 'SRX', 'SRR', 'GSE', 'ERX', 'ERR', 'DRX', 'DRR').")
        
        ## Need to consider the table to NOT have two SRA ids in the same table!
        if any(item.rstrip() for item in data.split('\n') if " " in item.rstrip()):
            raise forms.ValidationError("Identifiers field must not contain spaces.")
        
        """Splits SRAID by '|' into a list"""
        return set(item.strip() for item in data.split('\n'))  # Remove empty values

    def clean_UserID(self):
        data = self.cleaned_data['UserID']
        if "/bin/bash" in data or "/bin/sh" in data:
            raise forms.ValidationError("Invalid input detected in UserID. Please check your input.")
        if "rm" in data or "mv" in data:
            raise forms.ValidationError("Invalid input detected in UserID. Please check your input.")
        
        return data
