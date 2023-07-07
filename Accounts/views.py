from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout 
from appEquipements.forms import TypeEquipeForms,AttribueForms
from appEquipements.models import TypeEquipe,Attribue,Equipements,Tache,TypeAttribue,Valeurr

# Create your views here.



def register(request):
    msg = None
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'login.html')

def employee(request):
    return render(request,'login.html')

def deconnexion (request):
    logout(request)
    return redirect('login_view')

def home(request):
    context = {
               'typeEquipe': TypeEquipe.objects.all()
              }
    return render(request , 'home.html',context)
