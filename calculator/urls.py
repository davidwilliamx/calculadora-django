from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('limpar/', views.limpar_historico, name='limpar_historico'),
]
