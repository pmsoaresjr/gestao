from django.forms import ModelForm
from .models import Cliente
from django import forms

class ClienteForm (ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone"]
        widgets = { 'nome': forms.TextInput(attrs={'class': 'form-control'}) ,
                   'telefone': forms.TextInput(attrs={'class': 'form-control'}) 
                   
                   }
        # widgets = { 'cpf': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'logradouro': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'numero': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'cep': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'bairro': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'cidade': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'estado': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'complemento': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'pais': forms.TextInput(attrs={'class': 'form-control'}) }
        # widgets = { 'email': forms.TextInput(attrs={'class': 'form-control'}) }



                