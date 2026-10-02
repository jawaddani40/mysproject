from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
      
       path('extract-docs/', views.extract_docs, name='extract_docs'),
       path('write-docs/', views.write_docs, name='write_docs') ,
             #الاختيارات الموجودة في صفحة "extract_docs"   
       path('gold-card/', views.gold_card_form, name='gold_card_form'),
       path('demand-trvl/' , views.demand_trvl, name='demand_trvl' ),
       path('ansej-anm/' , views.ansej_anm, name='ansej_anm' ), 
       path('m_justice/' , views.m_justice, name='m_justice' ), 
       path('demand-aff/' , views.demand_aff, name='demand_aff' ), 
       
       
    
   
    ]