from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('welcome/',views.home,name="home"),
    path('exit/',views.chao,name="chao"),
]
