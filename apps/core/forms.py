from django import forms

from apps.core.models import Produto


class ProdutoForm(forms.ModelForm):
    url = forms.URLField(
        label='URL do produto',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'https://produto.mercadolivre.com.br/MLB-1207263399'
            }
        )
    )

    class Meta:
        model = Produto
        fields = ['url']
