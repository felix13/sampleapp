from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


from uploads.models import Document
from uploads.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'uploads/home.html', { 'documents': documents })




def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'your image was uploaded successfully') # adding a message
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {
        'form': form
    })
