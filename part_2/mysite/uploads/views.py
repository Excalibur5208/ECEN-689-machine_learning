from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import UploadFileForm
from uploads.models import Upload, Upload_0, Upload_1

import os
from django.conf import settings

import python_matlab
import shutil


def index(request):
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	return render(request, 'uploads/index.html', {
		'upload_list_No': upload_list_No,
		'upload_list_0_No': upload_list_0_No,
		'upload_list_1_No': upload_list_1_No,
	})
'''
	response = HttpResponse()
	response.write("<h1>Magic</h1>")
	response.write("<p>witch</p>")
	response['Age'] = 120
	del response['Age']
	response2 = HttpResponse("This is uploads index.")
	return render(request, 'uploads/index.html', {})
'''

def upload_page(request):
	res = []
	for i in range(1,10):
		res.append(str(i))
	return render(request, 'uploads/upload_page.html', {'range': res,})

def upload_action(request):
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	dir = 'D:/mysite_2/media/repository/'
	if not os.path.exists(dir):
		os.makedirs(dir)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			for index in range(10):
				title_index = "title" + str(index)
				file_index = "file" + str(index)
				if not request.FILES.has_key(file_index):
					continue
				
				upload_model = Upload(title = request.REQUEST[title_index], file = request.FILES[file_index])
				upload_model.save()
				initial_path = upload_model.file.path
				new_path = settings.MEDIA_ROOT + '\\repository\\' + request.REQUEST[title_index] + '.jpg'
				os.rename(initial_path, new_path)
				upload_model.file = new_path
				upload_model.file.name = u'repository/' + request.REQUEST[title_index] + '.jpg'
				upload_model.save()
			return HttpResponseRedirect(reverse('uploads:index'))
		else:
			return render(request, 'uploads/empty_repository.html', {
				'str': 'Invalid upload. Please upload some figures to classfy.',
				'upload_list_No': upload_list_No,
				'upload_list_0_No': upload_list_0_No,
				'upload_list_1_No': upload_list_1_No,
			})
	
def classfy(request):
	if len(Upload.objects.all()) == 0:
		return HttpResponseRedirect(reverse('uploads:empty_repository'))
	dir_pre = 'D:/mysite_2/media/'
	dir_1 = 'repository/'
	dir_2 = 'resize_fig/'
	results = python_matlab.method1()
	testFileList = os.listdir(dir_pre + dir_1)
	dir = 'D:/mysite_2/media/repository/'
	
	if not os.path.exists(dir_pre + 'cat/'):
		os.makedirs(dir_pre + 'cat/')
	if not os.path.exists(dir_pre + 'dog/'):
		os.makedirs(dir_pre + 'dog/')
		
	for index in range(len(results)):
		initial_path = dir_pre + dir_1 + testFileList[index]
		if int(results[index]) == 0:
			new_path = settings.MEDIA_ROOT + '\\cat\\' + testFileList[index]
			os.rename(initial_path, new_path)
			upload_model = Upload_0(title = testFileList[index], file = new_path)
			upload_model.file.name = u'cat/' + testFileList[index]
			upload_model.save()
		else:
			new_path = settings.MEDIA_ROOT + '\\dog\\' + testFileList[index]
			os.rename(initial_path, new_path)
			upload_model = Upload_1(title = testFileList[index], file = new_path)
			upload_model.file.name = u'dog/' + testFileList[index]
			upload_model.save()
	Upload.objects.all().delete()
	shutil.rmtree(dir_pre + dir_2)
	return HttpResponseRedirect(reverse('uploads:index'))
	
def repository(request):
	upload_list = Upload.objects.all()
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	return render(request, 'uploads/album.html', {
		'album_name': 'Repositories',
		'upload_list': upload_list,
		'upload_list_No': upload_list_No,
		'upload_list_0_No': upload_list_0_No,
		'upload_list_1_No': upload_list_1_No,
	})
	
def cats(request):
	upload_list_0 = Upload_0.objects.all()
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	return render(request, 'uploads/album.html', {
		'album_name': 'Cats',
		'upload_list': upload_list_0,
		'upload_list_No': upload_list_No,
		'upload_list_0_No': upload_list_0_No,
		'upload_list_1_No': upload_list_1_No,
	})

def dogs(request):
	upload_list_1 = Upload_1.objects.all()
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	return render(request, 'uploads/album.html', {
		'album_name': 'Dogs',
		'upload_list': upload_list_1,
		'upload_list_No': upload_list_No,
		'upload_list_0_No': upload_list_0_No,
		'upload_list_1_No': upload_list_1_No,
	})
	
def empty_repository(request):
	upload_list_No = len(Upload.objects.all())
	upload_list_0_No = len(Upload_0.objects.all())
	upload_list_1_No = len(Upload_1.objects.all())
	return render(request, 'uploads/empty_repository.html', {
		'str': 'The repository is empty. Please upload some figures to classfy.',
		'upload_list_No': upload_list_No,
		'upload_list_0_No': upload_list_0_No,
		'upload_list_1_No': upload_list_1_No,
	})