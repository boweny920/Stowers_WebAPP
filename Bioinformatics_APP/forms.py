from django import forms
from django.conf import settings
import pandas as pd
import os 

roboindex_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'static', 'tables', 'sampleSheet_ROBOINDEX.csv'))
genomes = roboindex_df['name'].unique()
GENOMES = [(n+1, i) for n, i in enumerate(genomes)]
# GENOMES = (
#     (1, "Mouse"),
#     (2, "Human"),
#     (3,"Fish"),
# )

class PublicDataForm(forms.Form):
    SRAID = forms.CharField(max_length=2000, required=True, 
                            widget=forms.Textarea(attrs={'placeholder': 'Enter Sample SRA ID here', 'rows': 1, 'cols': 25})
                            )
    SampleName = forms.CharField(max_length=2000, required=True,
                                 widget=forms.Textarea(attrs={'placeholder': 'Enter Sample Name here', 'rows': 1, 'cols': 25})
                                 )
    Reference = forms.ChoiceField(choices=GENOMES, 
                                  widget=forms.Select(attrs={'placeholder': 'ONE Genome Per Submission', 'rows': 1, 'cols': 15})
                                  )

    Description = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Put a short description of your sample. Leave empty if None', 'rows': 1, 'cols': 55})
        )
    
    def clean_SRAID(self):
        """Splits SRAID by '|' into a list"""
        data = self.cleaned_data['SRAID']
        return [item.strip() for item in data.split('|') if item.strip()]  # Remove empty values

    def clean_SampleName(self):
        """Splits SampleName by '|' into a list"""
        data = self.cleaned_data['SampleName']
        return [item.strip() for item in data.split('|') if item.strip()]

    def clean_Description(self):
        """Splits Description by '|' into a list"""
        data = self.cleaned_data['Description']
        return [item.strip() for item in data.split('|') if item.strip()]


