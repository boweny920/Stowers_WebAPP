from django.shortcuts import render
import os,time
from django.http import HttpResponse
from django.utils import timezone
from .forms import PublicDataForm, User_Info_Form
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

        userData = {"Lab": data.get("Lab"), 
                    "UserID": data.get("UserID"), 
                    "PROJECT_NAME": data.get("PROJECT_NAME"),
                    "ReadType": data.get("ReadType"),
                    "Reference": data.get("Reference")
                    }
        
        userInfo = User_Info_Form(userData)
        if not userInfo.is_valid():
            print(userInfo.errors)
            return render(request, "Bioinformatics/publicData_submitted_formatError.html", context = {"form": userInfo})

        sraid_values = data.getlist("SRAID")
        samplename_values = data.getlist("SampleName")
        read_length_values = data.getlist("ReadLength")
        description_values = data.getlist("Description")
        # Join the values into a string using "|"
        sraid_values_concate = "|".join(sraid_values)
        samplename_values_concate = "|".join(samplename_values)
        read_length_values_concate = "|".join(read_length_values)
        description_values_concate = "|".join(description_values)
        data = data.copy() #beacuse QueryDict is immutable
        data["SRAID"] = sraid_values_concate
        data["SampleName"] = samplename_values_concate
        data["ReadLength"] = read_length_values_concate
        data["Description"] = description_values_concate
        print(data)
        form = PublicDataForm(data)
        if form.is_valid():
            sraid = form.cleaned_data["SRAID"]
            samplename = form.cleaned_data["SampleName"]
            readLength = form.cleaned_data["ReadLength"]
            description = form.cleaned_data["Description"]

            # Using utils to create the xlsx file
            pubdata_obj = pubdata(
                Lab=userInfo.cleaned_data["Lab"],
                UserID=userInfo.cleaned_data["UserID"],
                PROJECT_NAME=userInfo.cleaned_data["PROJECT_NAME"],
                ReadType=userInfo.cleaned_data["ReadType"],
                Reference=userInfo.cleaned_data["Reference"],
                SRAID=sraid,
                SampleName=samplename,
                ReadLength=readLength,
                Description=description,
            )
            
            xlsx_path = pubdata_obj.public_xlsx_maker()
            # pubdata_obj.run_nextflow(xlsx_path)
            pubdata_obj.script_nextflow(xlsx_path)

            return render(request,"Bioinformatics/publicData_submitted.html")
        else:
            print(form.errors) # This will print the errors in the form
            return render(request, "Bioinformatics/publicData_submitted_formatError.html", context = {"form": form})

    else:
        form = PublicDataForm()
        userInfo = User_Info_Form()
    context = {"form": form, "userInfo": userInfo}
    
    return render(request, "Bioinformatics/publicData_form.html", context=context)

