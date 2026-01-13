"""
Yetkili kullanıcı oluşturma scripti
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Psyora.settings')
django.setup()

from django.contrib.auth.models import User

# Yetkili kullanıcı kontrolü
if User.objects.filter(username='yetkili').exists():
    print("⚠️  'yetkili' kullanıcısı zaten mevcut!")
else:
    # Yetkili kullanıcı oluştur
    user = User.objects.create_user(
        username='yetkili',
        password='yetkili123',  # Şifreyi mutlaka değiştirin!
        first_name='Yetkili',
        last_name='Kullanıcı',
        email='yetkili@e-rehber.com',
        is_staff=True  # Admin paneline erişim
    )
    print("✓ Yetkili kullanıcı oluşturuldu!")
    print(f"  Kullanıcı Adı: yetkili")
    print(f"  Şifre: yetkili123")
    print(f"\n⚠️  GÜVENLİK: Şifreyi mutlaka değiştirin!")
