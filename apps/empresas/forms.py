from django import forms
from .models import Empresa
from apps.automacoes.models import Automacao


class EmpresaCreateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco']

class EmpresaEditForm(forms.ModelForm):
    class Meta():
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco']