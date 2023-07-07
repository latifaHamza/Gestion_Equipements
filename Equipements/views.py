from django.shortcuts import render,redirect
from appEquipements.forms import TypeEquipeForms,AttribueForms
from appEquipements.models import TypeEquipe,Attribue,Equipements,Tache,TypeAttribue,Valeurr

def home(request):
    context = {
               'typeEquipe': TypeEquipe.objects.all()
              }
    return render(request , 'home.html',context)

def profil(request):
  context = {
               'typeEquipe': TypeEquipe.objects.all(),
               'tache':Tache.objects.all(),
               'equipements':Equipements.objects.all(),
              }
  return render(request , 'profil.html',context)

