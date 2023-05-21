from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = f"Bienvenido {request.user}"
    form = RegModelForm(request.POST or None)
    context = {
        "el_titulo": titulo,
        "el_form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo": f"Gracias {nombre}" 

        }

        print(instance)
        print(instance.timestamp)
        #form_data = (form.cleaned_data)
        #abc = form_data.get("email")
        #abc2 = form_data.get("nombre")
        #obj = Registrado.objects.create(email=abc, nombre=abc2)

    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        mensaje = form.cleaned_data.get("mensaje")
        nombre = form.cleaned_data.get("nombre")
        print(email,mensaje,nombre)
    context = {
        "el_form":form
    }

    return render(request, "forms.html", context)
