from django.urls import path
from . import views

urlpatterns = [
    path('pdf/', views.gerar_pdf),
]
