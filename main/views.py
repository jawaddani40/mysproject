from django.shortcuts import render




# الصفحة الرئيسية
def home(request):
    return render(request, 'main/home.html')

# --- دوال الخدمات الأخرى (مؤقتة حتى لا يعطي Django خطأ) ---


def extract_docs(request):
    return render(request, 'main/extract_docs.html')

def write_docs(request):
    return render(request, 'main/write_docs.html')

def gold_card_form(request):
    return render(request, 'main/gold_card.html')

def demand_trvl(request):
    return render(request, 'main/demand_trvl.html')

def ansej_anm(request):
    return render(request, 'main/ansej_anm.html')

def m_justice(request):
    return render(request, 'main/m_justice.html')

def demand_aff(request):
    return render(request, 'main/demand_aff.html')


