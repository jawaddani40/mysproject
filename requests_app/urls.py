from django.urls import path
from . import views

urlpatterns = [
    path('insc-onefd/', views.insc_onefd, name='insc_onefd'),
    path('print-docs/', views.print_docs, name='print_docs'),
]