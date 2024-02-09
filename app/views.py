from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.conf import settings
import os
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Votre enregistrement a été pris en compte avec succès.")
            
            return redirect('home') 
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, "index.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")




def liste(request):
    users = User.objects.all().order_by('-pk')
    countUser = User.objects.count()
    per_page = 10
    
    paginator = Paginator(users, per_page)
    
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    return render(request, 'liste.html', {'users': users, 'nombre': countUser})




def telecharger_pdf(request):
    # Chemin absolu vers le fichier PDF
    chemin_pdf = os.path.join(settings.BASE_DIR, 'staticfiles/ficher.pdf')

    # Ouverture du fichier PDF en mode lecture binaire
    with open(chemin_pdf, 'rb') as fichier:
        response = HttpResponse(fichier.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="fichier.pdf"'
        return response

from django.http import FileResponse
from django.shortcuts import render

def mon_pdf_view(request):
    # Chemin vers votre fichier PDF statique
    pdf_path = os.path.join(settings.BASE_DIR, 'staticfiles/ficher.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')