from django.shortcuts import render
from .models import CV

def cv_view(request):
    cv_data = CV.objects.first()  # İlk kaydı çekelim
    return render(request, 'cv.html', {'cv': cv_data})

