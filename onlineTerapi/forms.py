from django import forms
from .models import TherapyForm, CHILD_QUESTIONS, PARENT_QUESTIONS, CHOICE_LABELS

class TherapyFormForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Form type'a göre sorular belirleme
        form_type = self.data.get('form_type') if self.data else None
        questions = CHILD_QUESTIONS if form_type == 'child' else PARENT_QUESTIONS
        
        # Soru etiketlerini güncelleme
        question_fields = [f'question{i}' for i in range(1, 16)]
        for idx, field_name in enumerate(question_fields):
            if idx < len(questions):
                self.fields[field_name].label = f"{idx + 1}. {questions[idx]}"
                # Seçenek etiketlerini güncelleme
                self.fields[field_name].choices = [(i, label) for i, label in CHOICE_LABELS.items()]
    
    class Meta:
        model = TherapyForm
        fields = ['form_type', 'name', 'age', 'email', 'phone', 
                  'question1', 'question2', 'question3', 'question4', 'question5',
                  'question6', 'question7', 'question8', 'question9', 'question10',
                  'question11', 'question12', 'question13', 'question14', 'question15',
                  'notes']
        labels = {
            'form_type': 'Kiminiz?',
            'name': 'Ad Soyad',
            'age': 'Yaş',
            'email': 'E-mail',
            'phone': 'Telefon',
            'notes': 'Ek Notlar / Açıklamalar',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad ve soyadınızı girin'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Yaşınızı girin'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail adresinizi girin'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon numaranızı girin'}),
            'form_type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Lütfen ek notlarınızı veya açıklamalarınızı yazın...'}),
        }
