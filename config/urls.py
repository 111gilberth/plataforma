"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls', namespace='core')),
    #luego cambias este nombre es solo par que funcione deberia funcionar ejecutalo, voy
    #path('author-polls/', include('polls.urls', namespace='author-polls')),
    #ajajajaja si esta bien asi pero yo lo que quiero es que cuando le de un click aqui, me mande a este archivo html, esa es mi duda perdon por no darme a entender
    #a cual, hat mel squieres que te mande ?a este archivo,
]
