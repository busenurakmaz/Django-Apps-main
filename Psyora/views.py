from django.shortcuts import render

# Ana sayfa: Base.html'i render eder, başlık için context sağlar
def home(request):
    return render(request, 'Home.html', {'title': 'Ana Sayfa'})

def hizmetler(request):
    return render(request, 'hizmetler.html')

def sss(request):
    return render(request, 'sss.html')

def iletisim(request):
    return render(request, 'iletisim.html')

def blog(request):
    return render(request, 'blog.html')
