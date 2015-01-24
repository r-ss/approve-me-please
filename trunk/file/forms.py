# -*- coding: utf-8 -*-
from django import forms
from models import File

class FileUploadForm(forms.Form):
    file_file = forms.FileField(label=u'File', required=True, error_messages={'required': 'Select File'})
    width = forms.CharField(label=u'Width', min_length=2, max_length=4, error_messages={'required': 'Enter Width'})
    height = forms.CharField(label=u'Height', min_length=2, max_length=4, error_messages={'required': 'Enter Height'}) 
    comment = forms.CharField(label=u'Comment', required = False, max_length=300)
