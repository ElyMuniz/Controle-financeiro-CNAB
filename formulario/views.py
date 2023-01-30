from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from .arquivo import handle_uploaded_file
import ipdb


def home(request):
    if request.method == "GET":
        form = UploadFileForm()
        context = {"form": form}
        return render(request, "home.html", context=context)
    else:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["Arquivo"])
            return HttpResponseRedirect("")
        form = UploadFileForm()
        context = {"form": form}
        return render(request, "home.html", context=context)
