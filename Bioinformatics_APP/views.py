from django.shortcuts import render
import os,time
from django.http import HttpResponse
from django.utils import timezone
from .forms import PublicDataForm, User_Info_Form
from django.http import HttpResponseRedirect


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
            return render(request, "Bioinformatics/publicData_submitted_formatError.html")

        sraid_values = data.getlist("SRAID")
        samplename_values = data.getlist("SampleName")
        read_length_values = data.getlist("ReadLength")
        description_values = data.getlist("Description")
        # Join the values into a string using "|"
        sraid_values_concate = "|".join(sraid_values)
        samplename_values_concate = "|".join(samplename_values)
        read_length_values_concate = "|".join(str(v) for v in read_length_values) # Convert to string
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
            reference = form.cleaned_data["Reference"]
            readLength = form.cleaned_data["ReadLength"]
            description = form.cleaned_data["Description"]

            # Add app processes func from utils.py
            return render(request,"Bioinformatics/publicData_submitted.html")
        else:
            print(form.errors) # This will print the errors in the form
            return render(request, "Bioinformatics/publicData_submitted_formatError.html")

    else:
        form = PublicDataForm()
        userInfo = User_Info_Form()
    context = {"form": form, "userInfo": userInfo}
    
    return render(request, "Bioinformatics/publicData_form.html", context=context)

