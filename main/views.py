from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home_view(request, *args, **kwargs):
	path = os.path.join(BASE_DIR, 'main/static/main/skills-img')  # insert the path to your directory   
	img_list = os.listdir(path)

	return render(request, "main/index.html", {'images': img_list})


def upload_view(request, *args, **kwargs):
	if request.method == 'POST':
		uploaded_image = request.FILES['image']
		fs = FileSystemStorage()
		fs.save(uploaded_image.name, uploaded_image)
	return render(request, "main/upload.html", {})



def time_view(request):
	if request.method == 'POST':
		return render(request, "main/contact.html", {})