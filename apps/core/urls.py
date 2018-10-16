from django.urls import path, include
from .views import IndexView, CreatePost
from . import views

app_name = 'core'
formulario_patterns = ([
    path('', IndexView.as_view(), name='indexpage'),
    path('formulario/success/',views.congrats,name="congrats"),
    path('formulario/', CreatePost.as_view(), name='test'),
    ], 'formulario')
 #es ahi donde dice registrate me mande a la de register.html dentro de la carpeta core
