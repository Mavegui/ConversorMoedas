import requests
from django.shortcuts import render
from .forms import ConversorForm, DescontoForm
from decimal import Decimal


MOEDA_SIMBOLO = {
    'USD': '$',
    'EUR': '€',
    'BRL': 'R$',
    'GBP': '£',
    'JPY': '¥',
}

"""
_Observação_

O código abaixo poderia ser melhor estruturado, usando uma única view para lidar com os dois formulários.
Seria até menos código digitado. Porém, optei por manter a lógica que veio na minha mente.

A lógica que pensei foi usar duas funções distintas para cada uma lidar com um formulário específico. 
Porém com isso eu precisei instanciar os dois forms gerando um código maior, para que os forms apareçam certinhos para o usuário.
"""
def conversor_moedas(request):
    erro = None
    
    conversor_form = ConversorForm()
    desconto_form = DescontoForm()

    if 'converter' in request.POST:
        conversor_form = ConversorForm(request.POST)
        if conversor_form.is_valid():
            moeda_entrada = conversor_form.cleaned_data['moeda_entrada']
            moeda_saida = conversor_form.cleaned_data['moeda_saida']
            valor = conversor_form.cleaned_data['valor']
                            
            try:
                url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_entrada}&to={moeda_saida}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                convertido = data["rates"].get(moeda_saida)
                
                if convertido is not None:
                    simbolo = MOEDA_SIMBOLO.get(moeda_saida, '')
                    conversor_form = ConversorForm(initial={
                        'moeda_entrada': moeda_entrada,
                        'moeda_saida': moeda_saida,
                        'valor': valor,
                        'resultado':  f"{simbolo} {convertido:.2f}"
                    })
                    
                    request.session['valor_convertido'] = convertido
                    request.session['simbolo_convertido'] = simbolo
                     
                else:
                    erro = "Houve um erro na conversão, tente novamente."
            
            except requests.exceptions.RequestException:
                erro = "Houve um erro na comunicação com o serviço de câmbio."
        else:
            erro = "Formulário inválido. Verifique os dados e tente novamente."
            
    context = {
        'conversor_form': conversor_form,
        'desconto_form': desconto_form,
        'erro': erro
    }
    
    return render(request, "conversor/index.html", context)


def calculo_desconto(request):
    erro = None
    conversor_form = ConversorForm()
    desconto_form = DescontoForm()
    
    if 'calcular_desconto' in request.POST:
        desconto_form = DescontoForm(request.POST)
        
        if desconto_form.is_valid():
            porcentagem = desconto_form.cleaned_data.get('porcentagem_desconto')
            
            convertido = request.session.get('valor_convertido')
            simbolo = request.session.get('simbolo_convertido', '')
            
            if convertido is not None and porcentagem is not None:
                convertido = Decimal(convertido)
                porcentagem = Decimal(porcentagem)
                
                valor_com_desconto = convertido - (convertido  * (porcentagem / 100))
                
                desconto_form = DescontoForm(initial={
                    'porcentagem_desconto': porcentagem,
                    'valor_com_desconto': f"{simbolo} {valor_com_desconto:.2f}"
                })
            
            else:
                erro = "Por favor, realize uma conversão antes de aplicar o desconto."
        
        else:
            erro = "Formulário de desconto inválido. Verifique e tente novamente."
    
    context = {
        'conversor_form': conversor_form,
        'desconto_form': desconto_form,
        'erro': erro
    }
    
    return render(request, "conversor/index.html", context)
    
    
    