from django.urls import path, include
from .views import IndexView, CreatePost
from . import views

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='indexpage'),
    path('app1/', CreatePost.add_formulario, name='test'),
    ]
 #es ahi donde dice registrate me mande a la de register.html dentro de la carpeta core