from django.shortcuts import render
from .models import Sampleinfo

# Create your views here.

def home(request):
    return render(request, 'samples/home.html')

def sample_list(request):
    objects = Sampleinfo.objects.all()
    return render(request, 'samples/sample_list.html', {'objects': objects})

def sample_detail(request, sampleid):
    details = Sampleinfo.objects.get(pk=sampleid)
    return render(request, 'samples/sample_detail.html', {'details': details})

def map(request):
    return render(request, 'samples/map.html')
