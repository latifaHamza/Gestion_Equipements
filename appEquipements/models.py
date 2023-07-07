from django.db import models
import datetime
import os

def filepath(request,filename):
    old_filename =filename
    timeNew = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename = '%s%s'%(timeNew,old_filename)
    return os.path.join('uploads/',filename)

class Position(models.Model):
    title = models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class TypeAttribue(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=1000)
    def __str__(self):
        return self.nom

class TypeEquipe(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=1000)
    # position = models.CharField(max_length=1000)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    nbColumn = models.IntegerField()
    fichier = models.FileField(upload_to='uploads/', null=True, blank=True)
    def __str__(self):
        return self.id

class Attribue(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=1000)
    typeAttribue = models.CharField(max_length=1000)
    typeEquipe = models.ForeignKey(TypeEquipe,on_delete=models.CASCADE)
    def __str__(self):
        return self.id


class Equipements(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to=filepath,null=True,blank=True)
    typeEquipe = models.ForeignKey(TypeEquipe,on_delete=models.CASCADE)
    def __str__(self):
        return self.id



class Valeurr(models.Model):
    id = models.AutoField(primary_key=True)
    attribue = models.CharField(max_length=1000)
    valeur = models.CharField(max_length=1000)
    equipements = models.ForeignKey(Equipements,on_delete=models.CASCADE)
    def __str__(self):
        return self.valeur


class Tache(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=10000)
    id_Equipe = models.ForeignKey(Equipements,on_delete=models.CASCADE)
    id_TypeEquipe = models.IntegerField(null=True)
    username = models.CharField(max_length=1000)
    def __str__(self):
        return self.nom




