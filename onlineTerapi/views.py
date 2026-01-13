from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import TherapyFormForm
from .models import TherapyForm, CHILD_QUESTIONS, PARENT_QUESTIONS, CHOICE_LABELS

def home(request):
    return redirect('home')

def therapy_form(request):
    if request.method == 'POST':
        form = TherapyFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formunuz başarıyla gönderildi! Psikologlarımız sizinle yakında iletişime geçecek.')
            return redirect('online_therapy:success')
    else:
        form = TherapyFormForm()
    return render(request, 'online_therapy/form.html', {'form': form})

def success(request):
    return render(request, 'online_therapy/success.html')

@login_required
def psychologist_dashboard(request):
    # Filtreleme
    form_type_filter = request.GET.get('form_type', '')
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    # Tüm formları al
    forms = TherapyForm.objects.all()
    
    # Filtreleri uygula
    if form_type_filter:
        forms = forms.filter(form_type=form_type_filter)
    if status_filter:
        forms = forms.filter(status=status_filter)
    if search_query:
        forms = forms.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query) | Q(phone__icontains=search_query))
    
    context = {
        'forms': forms,
        'form_type_filter': form_type_filter,
        'status_filter': status_filter,
        'search_query': search_query,
    }
    return render(request, 'online_therapy/psychologist_dashboard.html', context)

@login_required
def form_detail(request, pk):
    form_obj = get_object_or_404(TherapyForm, pk=pk)
    
    # Form türüne göre soruları seç
    questions = CHILD_QUESTIONS if form_obj.form_type == 'child' else PARENT_QUESTIONS
    
    # Formdan cevapları al
    answers = [
        form_obj.question1, form_obj.question2, form_obj.question3, form_obj.question4, form_obj.question5,
        form_obj.question6, form_obj.question7, form_obj.question8, form_obj.question9, form_obj.question10,
        form_obj.question11, form_obj.question12, form_obj.question13, form_obj.question14, form_obj.question15,
    ]
    
    # Soru + cevap + label kombinasyonu oluştur
    qa_pairs = []
    for i, (question, answer) in enumerate(zip(questions, answers), 1):
        qa_pairs.append({
            'number': i,
            'question': question,
            'answer': answer,
            'label': CHOICE_LABELS.get(answer, 'Bilinmeyen'),
        })
    
    # Status güncellemesi
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update_status':
            new_status = request.POST.get('status')
            form_obj.status = new_status
            form_obj.save()
            messages.success(request, f'Form durumu "{new_status}" olarak güncellendi.')
            return redirect('online_therapy:form_detail', pk=pk)
        elif action == 'update_notes':
            form_obj.notes = request.POST.get('notes', '')
            form_obj.save()
            messages.success(request, 'Notlar kaydedildi.')
            return redirect('online_therapy:form_detail', pk=pk)
    
    context = {
        'form': form_obj,
        'qa_pairs': qa_pairs,
        'status_choices': [('pending', 'Beklemede'), ('reviewed', 'İncelendi'), ('completed', 'Tamamlandı')],
    }
    return render(request, 'online_therapy/form_detail.html', context)

def admin_panel(request):
    forms = TherapyForm.objects.all()
    return render(request, 'online_therapy/admin_panel.html', {'forms': forms})
