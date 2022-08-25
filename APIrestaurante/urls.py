from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestioncategorias/',include('gestionCategorias.urls')),
    path('adminusuarios/',include('adminUsuarios.urls')),
    path('gestionplatos/',include('gestionPlatos.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
appname='mainapp'
