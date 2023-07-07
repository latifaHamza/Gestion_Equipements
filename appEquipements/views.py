from django.shortcuts import render,redirect
from appEquipements.forms import TypeEquipeForms,AttribueForms
from .models import TypeEquipe,Attribue,Equipements,Tache,TypeAttribue,Valeurr
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa


def home(request):
    context = {
               'typeEquipe': TypeEquipe.objects.all()
              }
    return render(request , 'home.html',context)

@login_required
def addequipements(request, id=0):
    if request.method == "GET":
        tache="Modifier un Type d'Équipements"
        if id == 0:
            form = TypeEquipeForms()
            tache="Modifier un Type d'Équipements"
        else:
            typeEquipe = TypeEquipe.objects.get(pk=id)
            form = TypeEquipeForms(instance=typeEquipe)
            tache="Modifier un Type d'Équipements"
        return render(request, "TypeEquipe_form.html", {'form': form})
    else:
        if id == 0:
            form = TypeEquipeForms(request.POST,request.FILES)
            tache="Ajoute un Type d'Équipements"
        else:
            typeEquipe = TypeEquipe.objects.get(pk=id)
            form = TypeEquipeForms(request.POST,request.FILES,instance=typeEquipe)
            tache="Modifier un Type d'Équipements"
            

        if form.is_valid():
            form.save()
            instance = form.save()
            idd = instance.id
             # tache
            current_user = request.user
            username=current_user.username
            id_TypeEquipe=idd
            tach=Tache(nom=tache,id_TypeEquipe=id_TypeEquipe,username=username)
            tach.save()
        return redirect('/appEquipements/addAttribue/{}/'.format(idd))

def addAttribue(request,typeEquipe):
    if request.method=="POST":
        name=request.POST.get('name')
        typeAttribue=request.POST.get('typeAttribue')
        typeEquipe=typeEquipe
        query=Attribue(nom=name,typeAttribue=typeAttribue,typeEquipe_id=typeEquipe)
        query.save()
    context = {'typeAttribue': TypeAttribue.objects.all(),
               'attribue': Attribue.objects.all(),
               'typeEquipe': TypeEquipe.objects.all(),
               'typeEquipee': TypeEquipe.objects.get(pk=typeEquipe)}
    return render(request,"addAttribue.html",context)
    # return redirect('addAttribue',)


def Attribue_update(request,id):
    attribue= Attribue.objects.get(pk=id)
    context = {'typeAttribue': TypeAttribue.objects.all(),
               'attribue':  Attribue.objects.get(pk=id),
               }
    return render(request,"editAttribue.html",context)
    # return redirect('addAttribue',)

def attribue_edit(request,id):
    attribue= Attribue.objects.get(pk=id)
    name=request.POST.get('name')
    typeAttribue=request.POST.get('typeAttribue')
    attribue.nom=name
    attribue.typeAttribue=typeAttribue
    attribue.save()
    return redirect('home')



@login_required
def empEquipements(request,typeEquipe):
   
    if request.method=="POST":
        name=request.POST.get('name')
        photo=request.FILES.get('photo')
        query=Equipements(nom=name,photo=photo,typeEquipe_id=typeEquipe)
        query.save()
        attribue=Attribue.objects.all()
        equipements=Equipements.objects.all()
        for c in equipements:
            Equipementsu_id=c.id

        for c in attribue:
            if c.typeEquipe_id == typeEquipe:
                valeur=request.POST.get(c.nom)
                attribue=c.nom
                equipements=Equipementsu_id
                query1=Valeurr(valeur=valeur,attribue=attribue,equipements_id=equipements)
                query1.save()
                 # tache
                typeEquipeT=Equipementsu_id
        
        current_user = request.user
        tache="Ajoute un Équipements"
        username=current_user.username
        tach=Tache(nom=tache,id_Equipe_id=typeEquipeT,username=username)       
        tach.save()
     # ff
    
    context = {
               'equipements':Equipements.objects.all(),
            #    'equipement':Equipements.objects.get(dernier_pk),
               'valuer':Valeurr.objects.all(),
               'attribue': Attribue.objects.all(),
               'typeEquipe': TypeEquipe.objects.get(pk=typeEquipe),
              }
    return render(request,"emtEquipements.html",context)
    # return redirect('addAttribue',)

def equipements_update(request,id):
   
    context = { 
                'equipements': Equipements.objects.get(pk=id),
                'valeur': Valeurr.objects.all(),
               'typeEquipe': TypeEquipe.objects.all(),
               }
    return render(request,"editEquipements.html",context)
    # return redirect('addAttribue',)

def equipements_edit(request,id):
    equipements= Equipements.objects.get(pk=id)
    name=request.POST.get('name')
    photo=request.FILES.get('photo')
    equipements.nom=name
    equipements.photo=photo
    equipements.save()
    valeur =Valeurr.objects.all()
    for c in valeur:
            if c.equipements_id == id:
                val=request.POST.get(c.attribue)
                c.valeur=val
                c.save()
    # tache
    current_user = request.user
    tache="Modifier un Équipements"
    username=current_user.username
    typeEquipeT=id
    tach=Tache(nom=tache,id_Equipe_id=typeEquipeT,username=username)
    tach.save()
    return redirect('home')






def Allequipements(request,typeEquipe):
    context = {
               'equipements':Equipements.objects.all(),
               'valuer':Valeurr.objects.all(),
               'typeEquipe':TypeEquipe.objects.all(),
               'attribue': Attribue.objects.all(),
               'typeEquip': TypeEquipe.objects.get(pk=typeEquipe),
              }
    return render(request,"equipements.html",context)

def ShowEquipements(request,idEquipe):
    context = {
               'equipement':Equipements.objects.get(pk=idEquipe),
               'valuer':Valeurr.objects.all(),
               'typeEquipe':TypeEquipe.objects.all(),
               'tache':Tache.objects.all(),
              }
    return render(request,"ShowEquipements.html",context)


def equepments_delete(request,id):
    valuer=Valeurr.objects.all()
    for v in  valuer:
        if v.equipements_id==id:
             v.delete()

    equipements = Equipements.objects.get(pk=id)
    equipements.delete()
   
    
    return redirect('home')

def TypeEquipe_delete(request,id):
    typeEquipe = TypeEquipe.objects.get(pk=id)
    typeEquipe.delete()

    return redirect('home')

def attribue_delete(request,id):
    attribue = Attribue.objects.get(pk=id)
    attribue.delete()
    return redirect('home')

def attribue(request,typeEquipe):
    context = {'typeAttribue': TypeAttribue.objects.all(),
               'attribue': Attribue.objects.all(),
               'typeEquipee': TypeEquipe.objects.get(pk=typeEquipe),
               'typeEquipe': TypeEquipe.objects.all(),}
    return render(request,"attribue.html",context)


def pdf_equipements(request,id=0):
    equipements= Equipements.objects.get(pk=id)
    # valuer= Valeurr.objects.all()
    template_path = 'equipementsPDF.html'

    context = {'equipements': equipements,'valuer':Valeurr.objects.all()}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="equipements_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def tache_delete(request,id):
    tache = Tache.objects.get(pk=id)
    tache.delete()
    return redirect('profil')

def equipementsAll_PDF(request,id):
    equipements = Equipements.objects.all()
    valuer = Valeurr.objects.all()
    typeEquipe = TypeEquipe.objects.get(pk=id)
    template_path = 'equipementAll_PDF.html'

    context = {'equipements': equipements,
               'valuer':valuer,
               'typeEquipe':typeEquipe,
               }

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="equipements_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

