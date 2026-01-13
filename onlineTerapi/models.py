from django.db import models

# Çocuk Soruları
CHILD_QUESTIONS = [
    "Okuldaki akademik başarınız nasıl?",
    "Sosyal ortamlarda kendini rahat hissediyor musun?",
    "Aile içindeki ilişkileriniz nasıl?",
    "Uyku düzeni ve kalitesi nasıl?",
    "İştah değişiklikleri yaşadın mı?",
    "Arkadaşlarınla münasebetleriniz nasıl?",
    "Gelecek hakkında kaygılar yaşıyor musun?",
    "Konsantrasyon sorunun var mı?",
    "Fiziksel aktivitelere katılıyor musun?",
    "Öfke kontrolünde sorun yaşıyor musun?",
    "Mobil cihazları ne kadar kullanıyorsun?",
    "Ailede ciddi olaylar yaşadın mı?",
    "Kendine güven düzeyiniz nedir?",
    "Motivasyon ve enerji seviyesi nasıl?",
    "Terapiye açık mısın?",
]

# Ebeveyn Soruları
PARENT_QUESTIONS = [
    "Çocuğunuzun akademik başarısı hakkında endişeli misiniz?",
    "Çocuğunuzun sosyal becerilerine dair kaygılar var mı?",
    "Aile içi iletişimde sorun yaşıyor musunuz?",
    "Çocuğunuzun uyku davranışında değişiklik gördünüz mü?",
    "İştah veya yeme alışkanlıklarında değişiklik var mı?",
    "Okul öğretmenleri çocuğunuz hakkında kaygı belirttiler mi?",
    "Çocuğunuzda anksiyete belirtileri görmüş müsünüz?",
    "Konsantrasyon veya dikkat sorunları var mı?",
    "Fiziksel aktivite seviyeleri yeterli mi?",
    "Davranışsal sorunlar yaşanıyor mu?",
    "Ekran süresi aşırı derecede yüksek mi?",
    "Ailede travmatik olaylar yaşandı mı?",
    "Çocuğunuzun öz-saygısı iyi düzeyde mi?",
    "Evde motivasyon eksikliği görülüyor mu?",
    "Psikolojik danışmanlığa açık mısınız?",
]

# Seçenek etiketleri
CHOICE_LABELS = {
    1: 'Hiç katılmıyorum',
    2: 'Kısmen katılıyorum',
    3: 'Nadiren katılıyorum',
    4: 'Katılıyorum',
    5: 'Kesinlikle katılıyorum',
}

class TherapyForm(models.Model):
    FORM_TYPE_CHOICES = [
        ('child', 'Çocuk'),
        ('parent', 'Ebeveyn'),
    ]
    
    form_type = models.CharField(max_length=10, choices=FORM_TYPE_CHOICES)
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    age = models.IntegerField(verbose_name="Yaş")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    
    # 15 soru için yanıtlar (Her soru 1-5 ölçeğinde)
    question1 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 1")
    question2 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 2")
    question3 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 3")
    question4 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 4")
    question5 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 5")
    question6 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 6")
    question7 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 7")
    question8 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 8")
    question9 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 9")
    question10 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 10")
    question11 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 11")
    question12 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 12")
    question13 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 13")
    question14 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 14")
    question15 = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name="Soru 15")
    
    # Ek notlar
    notes = models.TextField(blank=True, verbose_name="Ek Notlar")
    
    # Tarih bilgileri
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Beklemede'), ('reviewed', 'İncelendi'), ('completed', 'Tamamlandı')], default='pending')
    
    def __str__(self):
        return f"{self.name} - {self.get_form_type_display()}"
    
    class Meta:
        verbose_name = "Terapi Formu"
        verbose_name_plural = "Terapi Formları"
        ordering = ['-created_at']
