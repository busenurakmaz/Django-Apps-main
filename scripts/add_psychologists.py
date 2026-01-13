"""
Psikolog Ekleme Rehberi
========================

## Yöntem 1: Django Admin Paneli (Önerilen)

1. Eğer admin kullanıcınız yoksa, yeni bir terminal açın ve şu komutu çalıştırın:
   python manage.py createsuperuser
   
   Kullanıcı adı, email ve şifre girin.

2. Tarayıcıda http://127.0.0.1:8000/admin adresine gidin

3. Admin kullanıcınızla giriş yapın

4. "Users" (Kullanıcılar) bölümüne tıklayın ve "Add User" (Kullanıcı Ekle)

5. Kullanıcı adı ve şifre girin, kaydedin

6. Açılan sayfada:
   - First name: Psikolog adı
   - Last name: Psikolog soyadı
   - Email: E-posta adresi
   - Active: ✓ işaretleyin
   - Kaydedin

7. Ana admin sayfasına dönün, "Psychologist profiles" bölümüne tıklayın

8. "Add Psychologist profile" butonuna tıklayın

9. Formu doldurun:
   - User: Az önce oluşturduğunuz kullanıcıyı seçin
   - Title: "Uzman Psikolog Dr. Ahmet Yılmaz" gibi
   - Bio: Psikolog hakkında kısa bilgi
   - Phone: Telefon numarası
   - Active: ✓ işaretleyin
   
10. Kaydedin

## Yöntem 2: Django Shell ile (Hızlı Test)

Terminal'de:
python manage.py shell

Sonra:
from django.contrib.auth.models import User
from Randevular.models import PsychologistProfile

# Kullanıcı oluştur
user = User.objects.create_user(
    username='dr_ahmet',
    password='sifre123',
    first_name='Ahmet',
    last_name='Yılmaz',
    email='ahmet@example.com'
)

# Psikolog profili oluştur
profile = PsychologistProfile.objects.create(
    user=user,
    title='Uzman Psikolog Dr. Ahmet Yılmaz',
    bio='10 yıllık deneyim, çocuk psikolojisi uzmanı',
    phone='0532 111 22 33',
    active=True
)

print(f"Psikolog eklendi: {profile}")

## Örnek: Birkaç Psikolog Eklemek için Script

Aşağıdaki scripti kullanabilirsiniz:
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Psyora.settings')
django.setup()

from django.contrib.auth.models import User
from Randevular.models import PsychologistProfile

# Örnek psikologlar
psychologists = [
    {
        'username': 'dr_ayse_kaya',
        'first_name': 'Ayşe',
        'last_name': 'Kaya',
        'email': 'ayse.kaya@e-rehber.com',
        'title': 'Uzman Klinik Psikolog',
        'university': 'İstanbul Üniversitesi Psikoloji Bölümü',
        'specialization': 'Kaygı Bozuklukları, Depresyon, Travma Tedavisi (CBT, EMDR)',
        'bio': '2013 yılından bu yana psikoterapi alanında aktif olarak çalışmaktadır. Bilişsel Davranışçı Terapi (CBT) ve EMDR sertifikalarına sahiptir. Kaygı bozuklukları, panik atak, travma sonrası stres bozukluğu ve depresyon tedavisinde uzmanlaşmıştır. Danışanlarına güvenli bir terapi ortamı sunarak, yaşam kalitelerini artırmalarına yardımcı olmaktadır.',
        'phone': '0532 111 11 11'
    },
    {
        'username': 'dr_mehmet_yilmaz',
        'first_name': 'Mehmet',
        'last_name': 'Yılmaz',
        'email': 'mehmet.yilmaz@e-rehber.com',
        'title': 'Uzman Psikolog',
        'university': 'Hacettepe Üniversitesi Psikoloji Bölümü',
        'specialization': 'Aile ve Çift Terapisi, İlişki Danışmanlığı',
        'bio': 'Sistemik Aile Terapisi ve Çift Terapisi alanlarında sertifikalı eğitim almıştır. İlişkilerde iletişim sorunları, evlilik öncesi danışmanlık, boşanma süreci desteği ve ebeveyn-çocuk ilişkileri konularında deneyimlidir. Çiftlerin ve ailelerin sağlıklı iletişim kurabilmeleri için çözüm odaklı yaklaşımlar kullanmaktadır.',
        'phone': '0532 222 22 22'
    },
    {
        'username': 'dr_zeynep_demir',
        'first_name': 'Zeynep',
        'last_name': 'Demir',
        'email': 'zeynep.demir@e-rehber.com',
        'title': 'Uzman Çocuk Psikoloğu',
        'university': 'Ankara Üniversitesi Gelişim Psikolojisi',
        'specialization': 'Çocuk ve Ergen Psikolojisi, DEHB, Gelişimsel Bozukluklar',
        'bio': 'Çocuk ve ergen ruh sağlığı alanında 10 yıllık deneyime sahiptir. DEHB, otizm spektrum bozukluğu, öğrenme güçlükleri ve davranış problemleri konularında uzmanlaşmıştır. Oyun terapisi ve aile eğitimi teknikleri kullanarak çocukların sağlıklı gelişimlerini desteklemektedir. Ebeveynlere çocuk yetiştirme konusunda da danışmanlık hizmeti sunmaktadır.',
        'phone': '0532 333 33 33'
    },
    {
        'username': 'dr_ali_ozturk',
        'first_name': 'Ali',
        'last_name': 'Öztürk',
        'email': 'ali.ozturk@e-rehber.com',
        'title': 'Klinik Psikolog',
        'university': 'Ege Üniversitesi Klinik Psikoloji',
        'specialization': 'Bağımlılık Tedavisi, Öfke Kontrolü, Kişilik Bozuklukları',
        'bio': 'Madde ve alkol bağımlılığı, davranışsal bağımlılıklar (kumar, internet, oyun), öfke kontrolü ve impuls kontrol bozuklukları tedavisinde deneyimlidir. Motivasyonel görüşme ve Diyalektik Davranış Terapisi (DBT) teknikleri kullanarak danışanlarına destek olmaktadır. Bireysel ve grup terapisi seansları yürütmektedir.',
        'phone': '0532 444 44 44'
    },
    {
        'username': 'dr_elif_arslan',
        'first_name': 'Elif',
        'last_name': 'Arslan',
        'email': 'elif.arslan@e-rehber.com',
        'title': 'Uzman Psikolog',
        'university': 'Boğaziçi Üniversitesi Psikoloji Bölümü',
        'specialization': 'Online Terapi, Stres Yönetimi, Kariyer Danışmanlığı',
        'bio': 'Online psikoterapi hizmetleri konusunda yurt içi ve yurt dışında sertifikalara sahiptir. İş hayatı stresi, tükenmişlik sendromu, kariyer değişimi ve iş-yaşam dengesi konularında danışmanlık vermektedir. Farkındalık temelli stres azaltma (MBSR) ve pozitif psikoloji yaklaşımlarını uygulamaktadır. Genç yetişkinlerin kariyer planlaması ve kişisel gelişim süreçlerinde rehberlik etmektedir.',
        'phone': '0532 555 55 55'
    }
]

def create_psychologists():
    print("Psikologlar ekleniyor...\n")
    
    for psy_data in psychologists:
        # Kullanıcı zaten var mı kontrol et
        if User.objects.filter(username=psy_data['username']).exists():
            print(f"⚠️  {psy_data['username']} zaten mevcut, atlanıyor...")
            continue
        
        # Kullanıcı oluştur
        user = User.objects.create_user(
            username=psy_data['username'],
            password='psikolog123',  # Varsayılan şifre
            first_name=psy_data['first_name'],
            last_name=psy_data['last_name'],
            email=psy_data['email']
        )
        
        # Psikolog profili oluştur
        profile = PsychologistProfile.objects.create(
            user=user,
            title=psy_data['title'],
            bio=psy_data['bio'],
            phone=psy_data['phone'],
            university=psy_data['university'],
            specialization=psy_data['specialization'],
            active=True
        )
        
        print(f"✓ {profile} eklendi")
    
    print(f"\nToplam {PsychologistProfile.objects.count()} psikolog sistemde kayıtlı.")
    print("\nNot: Tüm psikologların şifresi: psikolog123")

if __name__ == '__main__':
    create_psychologists()
