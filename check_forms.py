#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from online_therapy.models import TherapyForm

total = TherapyForm.objects.count()
child_forms = TherapyForm.objects.filter(form_type="child").count()
parent_forms = TherapyForm.objects.filter(form_type="parent").count()

print(f"Toplam Form Sayısı: {total}")
print(f"Çocuk Formları: {child_forms}")
print(f"Ebeveyn Formları: {parent_forms}")
print(f"\nTüm Formlar:")

for form in TherapyForm.objects.all():
    print(f"- {form.name} ({form.form_type}) - Durum: {form.status}")
