"""from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from pdfminer.high_level import extract_text
import os
import re
import yaml

def upload_file(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_upload = form.save()
            file_path = pdf_upload.file.path
            texxt = extract_text(file_path)
            text = texxt.replace(" ", "").replace("\n","").lower()

            # Load keywords from YAML file
            yaml_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'keywords.yml')
            with open(yaml_file_path, 'r') as file:
                config = yaml.safe_load(file)
                keywords = config['list1']

            # Search for keywords in text
            keyword_matches = {}
            for keyword in keywords:
                matches = re.findall(keyword, text)
                keyword_matches[keyword] = len(matches)

            return render(request, 'pdfupload/result.html', {'text':text, 'keyword_matches': keyword_matches})
    else:
        form = PDFUploadForm()
    return render(request, 'pdfupload/upload.html', {'form': form})
"""
"""
"""
from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from pdfminer.high_level import extract_text
import os
import re
import yaml

def upload_file(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_upload = form.save()
            file_path = pdf_upload.file.path
            texxt = extract_text(file_path)
            text = texxt.replace(" ", "").lower()

            # Load keywords from YAML file
            yaml_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'keywords.yml')
            with open(yaml_file_path, 'r') as file:
                config = yaml.safe_load(file)
                keywords = config['list1']

            # Find matched skills
            matched_skills = []
            for keyword in keywords:
                if re.search(r'\b' + keyword + r'\b', text):
                    matched_skills.append(keyword)

            # Calculate percentage of matched skills
            total_keywords = len(keywords)
            matched_keywords_count = len(matched_skills)
            percentage_matched = (matched_keywords_count / total_keywords) * 100

            return render(request, 'pdfupload/result.html', {'percentage_matched': percentage_matched, 'matched_skills': matched_skills})
        
    else:
        form = PDFUploadForm()
    return render(request, 'pdfupload/upload.html', {'form': form})

