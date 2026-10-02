from django.db import models

class CustomerRequest(models.Model):
    SERVICE_CHOICES = [
        ('onefd', 'تسجيلات بالمراسلة'),
        ('print', 'طبع وثائق'),
        ('extract', 'استخراج وثائق'),
        ('write', 'خدمات كتابية'),
        ('gold_card', 'بطاقة ذهبية'),
        ('travel', 'طلب سفر'),
        ('justice', 'وزارة العدل'),
        ('ansej', 'أنساج / أنام'),
    ]

    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    phone = models.CharField(max_length=20, db_index=True)
    data = models.JSONField(default=dict)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.service_type} (Verified: {self.is_verified})"