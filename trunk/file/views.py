# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from django.contrib import messages

from django.template import RequestContext

from trunk.settings import SITEHOST, MEDIA_TEMP_DIRECTORY, MEDIA_UPLOADS_DIRECTORY
from models import File
from forms import FileUploadForm


import os
import shutil
import random
import string

def home(request):
    context = {}
    return render(request, 'home.html', context)

def file_view(request, permalink):

    entries_all = File.objects.all()[:20]
    # print all_entries.len()
    count = len(entries_all)
    if count > 200:
        entries = File.objects.all()[:1]

        for f in entries:
            # delete_file(a)
            # print a.permalink
            filename = '%s.%s' % (f.permalink, f.filetype)
            delete_file(MEDIA_UPLOADS_DIRECTORY + filename)
            f.delete()
            #messages.success(request, u'File deleted %s' % filename) 
            # print len(entries)


    file = get_object_or_404(File, permalink__exact = permalink)
    return render(request, 'file/view.html', {'file': file})

def upload(request):
    ALLOWED_FILE_TYPES = ['application/x-shockwave-flash', 'image/jpeg', 'image/gif']
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            content_type = request.FILES['file_file'].content_type
            if content_type in ALLOWED_FILE_TYPES:
                if request.FILES.get('file_file',''):            
                    destination_path = '%s%s' % (MEDIA_TEMP_DIRECTORY, make_random_string(12))
                    if not handle_uploaded_file(request.FILES['file_file'], destination_path):
                        messages.error(request, u'15Mb max ;(')
                        # template_data = RequestContext(request, {'form': form})
                        return render(request, 'banner/upload.html', {'form': form})

                    # ALLOWED_FILE_TYPES = ['application/x-shockwave-flash', 'image/jpeg', 'image/gif']

                    # file_type = file.content_type.split('/')[0]
                    if content_type == 'application/x-shockwave-flash': filetype = 'swf'
                    if content_type == 'image/jpeg': filetype = 'jpeg'
                    if content_type == 'image/gif': filetype = 'gif'

                    f = File(filename = '0')
                    f.filetype = filetype
                    f.width = form.cleaned_data['width']
                    f.height = form.cleaned_data['height']
                    f.comment = form.cleaned_data['comment']
                    f.file_size = request.FILES['file_file'].size
                    f.save()
                        
                    f.permalink = make_key(f.id)
                    f.save()

                    filename = '%s.%s' % (f.permalink, f.filetype)
                    shutil.move(destination_path, MEDIA_UPLOADS_DIRECTORY + filename)
                    f.save()

                    messages.success(request, u'File uploaded')            
                    return redirect('%s/%s/' % (SITEHOST, f.permalink))

                else:
                    messages.error(request, u'Something wrong')
                    return render(request, 'file/upload.html', {'form': form})
            else:
                messages.error(request, u'File type is not supported')
                return render(request, 'file/upload.html', {'form': form})
        else:
            messages.error(request, u'No File ;(')
            return render(request, 'file/upload.html', {'form': form})
    else:
        form = FileUploadForm(initial = {'width': '240', 'height': '400',}) 
        return render(request, 'file/upload.html', {'form': form})

def make_key(num):
    characters = string.digits + string.ascii_lowercase
    base = len(characters)
    rem, res = divmod(num, base);
    return ('' if rem == 0 else make_key(rem)) + characters[res]


def handle_uploaded_file(f, path):
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return True
    
def make_random_string(ln):
    return ''.join( [random.choice(string.letters) for i in xrange(ln)] )

def check_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
        
def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

def remove_directory(dir):
    if os.path.isdir(dir):
        shutil.rmtree(dir)
        
def check_file_exists(path):
    if os.path.isfile(path):
        return True
    else:
        return False
        
def move_file(src, dst):
    shutil.move(src, dst)
    return