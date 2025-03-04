from django import forms
from django.conf import settings
import pandas as pd
import os 

roboindex_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'static', 'tables', 'sampleSheet_ROBOINDEX.csv'))
genomes = roboindex_df['name'].unique()
GENOMES = [(i, i) for i in genomes]


class PublicDataForm(forms.Form):
    
    SRAID = forms.CharField(max_length=2000, required=True, 
                            widget=forms.Textarea(attrs={'placeholder': 'Enter Sample SRA ID here', 'rows': 1, 'cols': 25})
                            )
    SampleName = forms.CharField(max_length=2000, required=True,
                                 widget=forms.Textarea(attrs={'placeholder': 'Enter Sample Name here', 'rows': 1, 'cols': 25})
                                 )
    
    Description = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Put a short description of your sample. Leave empty if None', 'rows': 1, 'cols': 55})
        )
    
    def clean_SRAID(self):
        data = self.cleaned_data['SRAID']
        # Make sure you have SRA IDs in the input 
        if "SRA" not in data.upper():
            raise forms.ValidationError("SRAID field must contain 'SRA'.")
        """Splits SRAID by '|' into a list"""
        return [item.strip() for item in data.split('|') if item.strip()]  # Remove empty values

    def clean_SampleName(self):
        data = self.cleaned_data['SampleName']
        """Splits SampleName by '|' into a list"""
        return [item.strip() for item in data.split('|') if item.strip()]

    def clean_Description(self):
        data = self.cleaned_data['Description']
        """Splits Description by '|' into a list"""
        return [item.strip() for item in data.split('|') if item.strip()]


LABS = [(line.strip(), line.strip()) for line in open(os.path.join(settings.BASE_DIR, 'static', 'tables', 'labs.txt')).readlines()]

class User_Info_Form(forms.Form):
    UserID = forms.CharField(max_length=100, required=True,
                             widget=forms.Textarea(attrs={'placeholder': 'Enter Stowers User ID here', 'rows': 1, 'cols': 25})
                             )
    Lab = forms.ChoiceField(choices=LABS, 
                            widget=forms.Select(attrs={'placeholder': 'Choose Your lab', 'rows': 1, 'cols': 15})
    )
    PROJECT_NAME = forms.CharField(max_length=100, required=True,
                                   widget=forms.Textarea(attrs={'placeholder': 'Enter Project Name here', 'rows': 1, 'cols': 25})
                                   )
    ReadType = forms.ChoiceField(choices=[('PE', 'Paired-End'), ('SE', 'Single-End')],
                                 widget=forms.Select(attrs={'placeholder': 'Choose One Read Type Per Submission', 'rows': 1, 'cols': 15})
                                 )
    Reference = forms.ChoiceField(choices=GENOMES, 
                                  widget=forms.Select(attrs={'placeholder': 'Choose One Genome Per Submission', 'rows': 1, 'cols': 15})
                                  )