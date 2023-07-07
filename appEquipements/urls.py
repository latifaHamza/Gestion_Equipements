from django.contrib import admin
from django.urls import include, path
from . import views 

urlpatterns = [

    path('home/',views.home,name='home'),
    path('TypeEquipe_form/',views.addequipements,name='addequipements'),
    path('addAttribue/<int:typeEquipe>/', views.addAttribue,name='addAttribue'),
    path('empEquipements/<int:typeEquipe>/', views.empEquipements,name='empEquipements'),
    path('Allequipements/<int:typeEquipe>/', views.Allequipements,name='Allequipements'),
    path('ShowEquipements/<int:idEquipe>/', views.ShowEquipements,name='ShowEquipements'),
    path('equepments_delete/<int:id>/', views.equepments_delete,name='equepments_delete'),
    path('/TypeEquipe_update/<int:id>/', views.addequipements,name='TypeEquipe_update'), 
    path('TypeEquipe_delete/<int:id>/',views.TypeEquipe_delete,name='TypeEquipe_delete'),
    path('attribue/<int:typeEquipe>/', views.attribue,name='attribue'),
    path('Attribue_update/<int:id>/',views.Attribue_update,name='Attribue_update'),
    path('attribue_edit/<int:id>/',views.attribue_edit,name='attribue_edit'),
    path('attribue_delete/<int:id>/',views.attribue_delete,name='attribue_delete'),
    path('equipements_update/<int:id>/',views.equipements_update,name='equipements_update'),
    path('equipements_edit/<int:id>/',views.equipements_edit,name='equipements_edit'),
    path('save/<int:id>/',views.pdf_equipements,name='pdf_equipements'),
    path('tache_delete/<int:id>/',views.tache_delete,name='tache_delete'),
    path('saveAll/<int:id>/',views.equipementsAll_PDF,name='equipementsAll_PDF'),




    ]