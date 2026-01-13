from django.contrib import admin
from .models import TherapyForm

@admin.register(TherapyForm)
class TherapyFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'form_type', 'email', 'status', 'created_at')
    list_filter = ('form_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Kişisel Bilgiler', {
            'fields': ('form_type', 'name', 'age', 'email', 'phone')
        }),
        ('Sorular (1-15)', {
            'fields': ('question1', 'question2', 'question3', 'question4', 'question5',
                      'question6', 'question7', 'question8', 'question9', 'question10',
                      'question11', 'question12', 'question13', 'question14', 'question15')
        }),
        ('Ek Bilgiler', {
            'fields': ('notes', 'status', 'created_at')
        }),
    )
