from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home_view(request, *args, **kwargs):
	path = os.path.join(BASE_DIR, 'main/static/main/skills-img')    
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

def mail_view(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	message = request.POST.get('message')

	send_mail('Name: ' + name + ' E-mail: ' + email,
	message,
	'balya.evgenij@gmail.com',
	['balya.evgenij@gmail.com'],
	fail_silently = False)
	path = os.path.join(BASE_DIR, 'main/static/main/skills-img')    
	img_list = os.listdir(path)

	return render(request, "main/index.html", {'images': img_list})


