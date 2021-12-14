from django.urls import path

from apps.core import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:pk>', views.detalhes, name='detalhes'),
    path('excluir/<int:pk>', views.excluir, name='excluir'),
]
