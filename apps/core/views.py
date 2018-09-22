from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from django.template import context
from .models import Post, Contacto
from .forms import FormularioContacto

class IndexView(TemplateView):
	template_name = "index.html"
	model = Post

class CreatePost(CreateView): # aqui deberia ir el metodo CreateView pero para usarlo te falta el atributo model_form para que 
    template_name = "app1/formulario.html"
    form_class = FormularioContacto
    model_form = Contacto

    def add_formulario(request):
       template_name = "app1/formulario.html"
       form  = FormularioContacto()
       if request.method == 'POST':
           form = FormularioContacto(request.POST)
           if f.is_valid():
              Formulario_item = form.save(commit=False)
              Formulario_item.save()
           return render(template_name,{'form':form})
          
       return render(template_name,{'form':form}, context)

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
