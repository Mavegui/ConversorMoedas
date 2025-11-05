from django import forms

class ConversorForm(forms.Form):
    moeda_entrada = forms.ChoiceField(
        label="Moeda de entrada",
        choices=[
            ('USD', 'Dólar Americano'),
            ('EUR', 'Euro'),
            ('BRL', 'Real Brasileiro'),
            ('GBP', 'Libra Esterlina'),
            ('JPY', 'Iene Japonês'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    moeda_saida = forms.ChoiceField(
        label="Moeda de saída",
        choices=[
            ('BRL', 'Real Brasileiro'),
            ('USD', 'Dólar Americano'),
            ('EUR', 'Euro'),
            ('GBP', 'Libra Esterlina'),
            ('JPY', 'Iene Japonês'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    valor = forms.DecimalField(
        label="Valor",
        min_value=0.01,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite o valor a ser convertido.', 
            'step': '0.01'
        })
    )
    
    resultado = forms.CharField(
        label="Resultado",
        required=False,
        disabled=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    

class DescontoForm(forms.Form):

    porcentagem_desconto = forms.DecimalField(
        label="Porcentagem de Desconto",
        min_value=0,
        max_value=100,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a porcentagem de desconto.',
        })
    )
    
    valor_com_desconto = forms.CharField(
        label="Valor com Desconto",
        required=False,
        disabled=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
