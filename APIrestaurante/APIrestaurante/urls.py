from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestioncategorias/',include('gestionCategorias.urls')),
    path('adminusuarios/',include('adminUsuarios.urls')),
    path('gestionplatos/',include('gestionPlatos.urls'))
]
