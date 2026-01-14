# Django-Apps E-Rehber
E -REHBER
BUSE NUR AKMAZ
BERFİN TOK
VİLDAN ÇİFTÇİ 
DAMLA SUDE ER
E-REHBER 
Ebeveyn ve çocuk için yapılmış randevu sistemli bir web site
Buse Nur Akmaz:randevular
Vildan Çiftçi:form sayfası 
Berfin Tok:login ekrani
Damla Sude Er: yapmadı


# Django-Apps — E-Rehber

E-Rehber, ebeveyn ve çocuklar için geliştirilmiş; randevu yönetimi, form toplama ve temel kimlik doğrulama sunan bir Django web uygulamasıdır.

## Proje Özeti
Basit, öğretici amaçlı bir uygulama olarak:
- Randevu oluşturma ve yönetme
- Form (bilgi/görüş) sayfaları
- Kullanıcı girişi (login)

## Katkı ve Sorumluluklar

| İsim               | Sorumluluk / Görev             | Durum           |
|--------------------|--------------------------------|-----------------|
| Buse Nur Akmaz     | Randevular (randevu yönetimi)  | Tamamlandı      |
| Vildan Çiftçi      | Form sayfası                   | Tamamlandı      |
| Berfin Tok         | Login ekranı                   | Tamamlandı      |
| Damla Sude Er      | (Boş / Henüz yapılmadı)        | Beklemede       |

## Hızlı Başlangıç (Yerel)
1. Depoyu klonlayın:
   ```
   git clone https://github.com/busenurakmaz/Django-Apps-main.git
   cd Django-Apps-main
   ```
2. Sanal ortam oluşturup etkinleştirin:
   - macOS / Linux:
     ```
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
3. Bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   ```
   (requirements.txt yoksa `pip install django` komutu ile Django yükleyin.)
4. Migrasyonları çalıştırın:
   ```
   python manage.py migrate
   ```
5. Sunucuyu başlatın:
   ```
   python manage.py runserver
   ```
   Tarayıcıda http://127.0.0.1:8000 adresini açın.

## Teknolojiler
- Python 3.8+
- Django 3.x / 4.x
- SQLite (varsayılan)

## TODO / İyileştirmeler
- Eksik özelliklerin tamamlanması (Damla Sude Er için atölye/görev tanımı)
- Unit/integration testleri eklenmesi
- Form doğrulamaları ve kullanıcı deneyimi iyileştirmeleri
- Dokümantasyon genişletme

## Katkıda Bulunma
Değişiklik yapmak için fork → branch → pull request akışını kullanın veya bir issue açın.

## İletişim
Proje sahibi / sürüm kontrolü: [busenurakmaz](https://github.com/busenurakmaz)
