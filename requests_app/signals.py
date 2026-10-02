import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomerRequest

# ضع التوكن ورقم الشات الخاص بك هنا (سنقوم بنقلها إلى بيئة أمنة لاحقاً)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

@receiver(post_save, sender=CustomerRequest)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        # تنسيق نص الرسالة
        service_name = "طباعة مستندات" if instance.service_type == "print_docs" else "تسجيل بالمراسلة"
        message = (
            f"🔔 *طلب جديد وصل!*\n\n"
            f"📌 **نوع الخدمة:** {service_name}\n"
            f"👤 **الاسم:** {instance.name or 'غير محدد'}\n"
            f"📞 **الهاتف:** {instance.phone}\n"
            f"🔢 **رقم الطلب:** #{instance.id}\n"
        )
        
        # إرسال الرسالة إلى التلغرام
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"Error sending Telegram notification: {e}")