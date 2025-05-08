from django import forms
from django.conf import settings
import pandas as pd
import os 
from django.conf import settings

roboindex_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'static', 'tables', 'sampleSheet_ROBOINDEX.csv'))
genomes = roboindex_df['name'].unique()
GENOMES = [(i, i) for i in genomes]
LABS = [(line.strip(), line.strip()) for line in open(os.path.join(settings.BASE_DIR, 'static', 'tables', 'labs.txt')).readlines()]


class PublicDataForm(forms.Form):
    
    SRAID = forms.CharField(max_length=2000, required=True, 
                            widget=forms.Textarea(attrs={'placeholder': 'Enter Sample SRA ID here, one per line', 'rows': 5, 'cols': 25})
                            )
    
    UserID = forms.CharField(max_length=10, required=True,
                             widget=forms.Textarea(attrs={'placeholder': 'Enter Stowers User ID here', 'rows': 1, 'cols': 25})
                             )
    
    Lab = forms.ChoiceField(choices=LABS, 
                            widget=forms.Select(attrs={'placeholder': 'Choose Your lab', 'rows': 1, 'cols': 15})
    )
    
    Reference = forms.ChoiceField(choices=GENOMES, 
                                  widget=forms.Select(attrs={'placeholder': 'Choose One Genome Per Submission', 'rows': 1, 'cols': 15})
                                  )
    
    def clean_SRAID(self):
        data = self.cleaned_data['SRAID']
        # Consider security issues with the input
        if "/bin/bash" in data or "/bin/sh" in data:
            raise forms.ValidationError("Invalid input detected in SRAID. Please check your input.")
        if "rm" in data or "mv" in data:
            raise forms.ValidationError("Invalid input detected in SRAID. Please check your input.")

        # Make sure you have SRA IDs in the input 
        if "SRA" not in data.upper():
            raise forms.ValidationError("SRAID field must contain 'SRA'.")
        ## Need to consider the table to NOT have two SRA ids in the same table!
        if any(item.rstrip() for item in data.split('\n') if " " in item.rstrip()):
            raise forms.ValidationError("SRAID field must not contain spaces.")
        
        
        """Splits SRAID by '|' into a list"""
        return set(item.strip() for item in data.split('\n'))  # Remove empty values

    def clean_UserID(self):
        data = self.cleaned_data['UserID']
        if "/bin/bash" in data or "/bin/sh" in data:
            raise forms.ValidationError("Invalid input detected in UserID. Please check your input.")
        if "rm" in data or "mv" in data:
            raise forms.ValidationError("Invalid input detected in UserID. Please check your input.")
        
        return data


    