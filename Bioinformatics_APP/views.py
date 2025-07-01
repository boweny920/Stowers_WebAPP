from django.shortcuts import render
import os,time
from django.http import HttpResponse
from django.utils import timezone
from .forms import PublicDataForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .utils import pubdata_run
from .models import pubData_RunData

### public data submission
def publicdata(request):
    if request.method == "POST":
        data = request.POST # This is not validated data. The below function validates the data, but only takes the last value of each field. 

        form = PublicDataForm(data)
        if form.is_valid():
            sraid = form.cleaned_data['Identifiers']
            Lab = form.cleaned_data["Lab"]
            UserID = form.cleaned_data["UserID"]
            Reference = form.cleaned_data["Reference"]
            # print(sraid, Lab, UserID, Reference)

            # Save the run data to the database"
            pubData_RunData.objects.create(
                Identifiers="|".join(str(v) for v in sraid),
                Reference=Reference,
                UserID=UserID,
                Lab=Lab,
            )

            pubdata_run(ID_Set=sraid, Lab=Lab, UserID=UserID).ID_Csv_maker()

            return render(request,"Bioinformatics/publicData_submitted.html")
        else:
            print(form.errors) # This will print the errors in the form
            return render(request, "Bioinformatics/publicData_submitted_formatError.html", context = {"form": form})

    else:
        form = PublicDataForm()
    context = { "form": form }
    
    return render(request, "Bioinformatics/publicData_form.html", context=context)
