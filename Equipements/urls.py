
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('appEquipements/', include('appEquipements.urls')),
    path('Accounts/', include('Accounts.urls')),

    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('profil/',views.profil,name='profil'),

    # path('', include('equipements.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)