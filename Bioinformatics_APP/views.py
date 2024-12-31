from django.shortcuts import render
import os,time
from django.http import HttpResponse
from django.utils import timezone
from .forms import PublicDataForm
from django.http import HttpResponseRedirect


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ## root of project
static_root = os.path.join(BASE_DIR,"static")

### home page
def Home(request):
    return render(request,"Bioinformatics/Home.html")

# def publicdata_submit(request):
#     return render(request,"Bioinformatics/publicData_submitted.html")

def publicdata(request):
    if request.method == "POST":
        data = request.POST # This is not validated data. The below function validates the data, but only takes the last value of each field. 
        if len(data["SRAID"]>1):
            validation_list =[] # a list of TRUE or Falses for data validation
            data_dic = {}
            i=0
            while i < len(data["SRAID"]):


        else:
            form = PublicDataForm(request.POST)
            if form.is_valid():
                sraid = form.cleaned_data["SRAID"]
                samplename = form.cleaned_data["SampleName"]
                reference = form.cleaned_data["Reference"]
                description = form.cleaned_data["Description"]
                print(form.cleaned_data)
                
                # Add app processes func from utils.py
                return render(request,"Bioinformatics/publicData_submitted.html")
    else:
        form = PublicDataForm()
    context = {"form": form}
    
    return render(request, "Bioinformatics/publicData_form.html", context=context)

