from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.template import context
from .models import Post, Contacto
from .forms import FormularioContacto
#### SOLO USUARIOS CON PERMISIONES PODRAN CREAR
from django.contrib.auth.mixins import PermissionRequiredMixin

class IndexView(TemplateView):
	template_name = "index.html"
	model = Post
class CreatePost(PermissionRequiredMixin, CreateView):
    model = Contacto
    form_class = FormularioContacto
    success_url = reverse_lazy('formulario:congrats')
    permission_required = 'catalog.can_mark_returned'
def congrats(request):
    return render(request,'core/congrats.html')


class ListPost(ListView):
	template_name = "core/"

	def test(request):
		return render(request, "core/register.html")

     #permiteme, core es mi aplicacion, el problema es que no recuerdo bien de donde salieron los import de listView 
     #no entiendo bine tu prgunta, me refiero a que si hago una clase nueva con el metodo donde voy a meter mi pagina
     #a redireccionar pues tendria que meter en medio de los () lo que estoy importando de views.generic, mi pregunta
     # es que debo poner en la parte del import para asignarselo a () de mi clase RegisterView
     # si tu metodo registra debs usar el metodo CreateView entonces solo hago dentro de createView puedo hacer esto no?
     #ok pero dentro de mi urls.py como quedaria si le pongo asi??
