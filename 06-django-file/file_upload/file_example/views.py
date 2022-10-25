from django.http import Http404, HttpResponse
from .forms import UploadFileForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import seaborn as sns
import matplotlib.pyplot as plt


def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def uploaded_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        return HttpResponse("Great! " + str(file))
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form' : form})

