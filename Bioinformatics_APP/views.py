from django.shortcuts import render
import os,time
from django.http import HttpResponse
from django.utils import timezone
from .forms import PublicDataForm
from django.http import HttpResponseRedirect
from django.conf import settings
from .utils import pubdata

### home page
def Home(request):
    return render(request,"Bioinformatics/Home.html")

### public data submission
def publicdata(request):
    if request.method == "POST":
        data = request.POST # This is not validated data. The below function validates the data, but only takes the last value of each field. 

        form = PublicDataForm(data)
        if form.is_valid():
            sraid = form.cleaned_data['SRAID']
            Lab=userInfo.cleaned_data["Lab"],
            UserID=userInfo.cleaned_data["UserID"]
            print(sraid, Lab, UserID)

            # Using utils to create the xlsx file
            # pubdata_obj = pubdata(
            #     Lab=userInfo.cleaned_data["Lab"],
            #     UserID=userInfo.cleaned_data["UserID"],
            #     PROJECT_NAME=userInfo.cleaned_data["PROJECT_NAME"],
            #     ReadType=userInfo.cleaned_data["ReadType"],
            #     Reference=userInfo.cleaned_data["Reference"],
            #     SRAID=sraid,
            #     SampleName=samplename,
            #     ReadLength=readLength,
            #     Description=description,
            # )
            
            # xlsx_table = pubdata_obj.public_xlsx_maker()
            # # pubdata_obj.run_nextflow(xlsx_path)
            # pubdata_obj.script_nextflow(xlsx_table)

            return render(request,"Bioinformatics/publicData_submitted.html")
        else:
            print(form.errors) # This will print the errors in the form
            return render(request, "Bioinformatics/publicData_submitted_formatError.html", context = {"form": form})

    else:
        form = PublicDataForm()
    context = { "form": form }
    
    return render(request, "Bioinformatics/publicData_form.html", context=context)

