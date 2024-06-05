# In pdfupload/forms.py
from django import forms
from .models import PdfUpload

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PdfUpload
        fields = ('file',)
 