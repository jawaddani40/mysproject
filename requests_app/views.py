import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomerRequest

def insc_onefd(request):
    if request.method == "POST":
        phone = request.POST.get("phone", "").strip()

        # تنظيف وتحسين صيغة رقم الهاتف
        clean_phone = "".join(filter(str.isdigit, phone))
        if clean_phone.startswith("0"):
            clean_phone = "213" + clean_phone[1:]
        elif clean_phone and not clean_phone.startswith("213"):
            clean_phone = "213" + clean_phone

        # التحقق هل الرقم مؤكد سابقاً
        is_already_verified = CustomerRequest.objects.filter(
            phone=clean_phone, 
            is_verified=True
        ).exists()

        # إنشاء الطلب في قاعدة البيانات
        new_request = CustomerRequest.objects.create(
            service_type='onefd',
            phone=clean_phone,
            data=request.POST.dict(),
            is_verified=is_already_verified
        )

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                "status": "success",
                "is_verified": is_already_verified,
                "request_id": new_request.id
            })

    return render(request, "main/insc_onefd.html")


def print_docs(request):
    if request.method == "POST":
        # قراءة البيانات سواء كانت مرسلة كـ JSON أو Form
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.POST.dict()

        phone = str(data.get("phone", "")).strip()

        # تنظيف وتنسيق رقم الهاتف بالصيغة الدولية (213)
        clean_phone = "".join(filter(str.isdigit, phone))
        if clean_phone.startswith("0"):
            clean_phone = "213" + clean_phone[1:]
        elif clean_phone and not clean_phone.startswith("213"):
            clean_phone = "213" + clean_phone

        # التحقق هل الرقم مؤكد سابقاً في قاعدة البيانات
        is_already_verified = CustomerRequest.objects.filter(
            phone=clean_phone, 
            is_verified=True
        ).exists()

        # حفظ الطلب في قاعدة البيانات
        new_request = CustomerRequest.objects.create(
            service_type='print_docs',
            phone=clean_phone,
            data=data,  # يحوي اسم الزبون وقائمة الملفات والمجموع
            is_verified=is_already_verified
        )

        return JsonResponse({
            "status": "success",
            "is_verified": is_already_verified,
            "request_id": new_request.id
        })

    return render(request, "main/print_docs.html")