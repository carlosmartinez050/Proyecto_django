from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.paginaPrincipal, name='home')
]
