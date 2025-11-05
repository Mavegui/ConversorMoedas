from . import views
from django.urls import path

urlpatterns = [
    path('', views.conversor_moedas, name='conversor_moedas'),
    path('calculo-desconto/', views.calculo_desconto, name='calculo_desconto')
]

