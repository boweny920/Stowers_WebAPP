from django import forms

GENOMES = (
    (1, "Mouse"),
    (2, "Human"),
    (3,"Fish"),
)

class PublicDataForm(forms.Form):
    SRAID = forms.CharField(max_length=100, required=True, 
                            widget=forms.Textarea(attrs={'placeholder': 'Enter Sample SRA ID here', 'rows': 1, 'cols': 25})
                            )
    SampleName = forms.CharField(max_length=100, 
                                 widget=forms.Textarea(attrs={'placeholder': 'Enter Sample Name here', 'rows': 1, 'cols': 25})
                                 )
    Reference = forms.ChoiceField(choices=GENOMES)

    Description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Put a short description of your sample. Put NA if None', 'rows': 1, 'cols': 50})
        )

