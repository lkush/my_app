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
    objects = Sampleinfo.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoibGVuYWt1c2giLCJhIjoiY2s4aHdjY3pyMDQ1dzNsbWNucWQ0Znh0eCJ9.4CrzJDbd-sbqv2vAHtb93w'
    return render(request, 'samples/map.html',
                  {'mapbox_access_token': mapbox_access_token, 'objects': objects})
