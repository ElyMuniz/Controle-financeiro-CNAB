from django import forms

# Create your views here.


class UploadFileForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()
    Arquivo = forms.FileField()
