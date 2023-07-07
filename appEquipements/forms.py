from django import forms
from .models import TypeEquipe,Attribue,Equipements,Tache,TypeAttribue

# # TypeEquipe 4
class TypeEquipeForms(forms.ModelForm):
    class Meta:
        model = TypeEquipe
        fields = ('nom','fichier','nbColumn','position')
        labels = {
            'nom': 'Le nom d’équipements',
            'fichier': 'Documentation d’équipements',
            'position': 'La position d’équipements',
            'nbColumn': 'nombre de colonne',
        }

    def __init__(self, *args, **kwargs):
        super(TypeEquipeForms,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"


#  Attribue 3
class AttribueForms(forms.ModelForm):
    class Meta:
        model = Attribue
        fields = ('nom','typeAttribue','typeEquipe')
        labels = {
            'nom': 'Le nom d’Attribue',
            'typeAttribue': 'Le type d’Attribue',
            'typeEquipe': 'type d’équipements',
        }

    def __init__(self, *args, **kwargs):
        super(AttribueForms,self).__init__(*args, **kwargs)
        self.fields['typeAttribue'].empty_label = "Select"
        self.fields['typeEquipe'].empty_label = "Select"
        #   self.fields['position'].required = False
