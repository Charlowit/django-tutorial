# urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')), # main es el nombre de tu aplicacion principal y desde donde se ejecutarán el resto de apps
    path('admin/', admin.site.urls),
]
