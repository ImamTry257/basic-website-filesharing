from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import uuid

from .models import File
from .forms import UploadForm

# Create your views here.
def index(request):
    return render(request, 'sharing/index.html')


def upload(request):
    if request.method == "POST":
        # instance form
        form = UploadForm(request.POST, request.FILES)

        # check validasi form
        if form.is_valid():
            formFile = form.save(commit=False)

            # insert uuid
            uid = uuid.uuid1()
            formFile.uid = str(uid)
            formFile.save()

            return HttpResponseRedirect('/'+ formFile.uid)

    return render(request, 'sharing/index.html')


def download(request, uid):
    file = get_object_or_404(File, uid = uid)
    return render(
        request, 
        'sharing/download.html', 
        {
            'dl_url' : file.file.url, 
            'filename' : file.file.name.split('/')[-1]
        }
    )
