from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleados(request):
    return render(request,"empleado.html")

def sucursal(request):
    return render(request,"sucursal.html")

def cliente(request):
    return render(request,"cliente.html")

def cita(request):
    return render(request,"cita.html")

def pagos(request):
    return render(request,"pagos.html")