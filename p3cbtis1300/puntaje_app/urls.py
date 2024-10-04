from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleado/",views.empleados,name="empleado"),
    path("sucursal/",views.sucursal,name="sucursal"),
    path("cliente/",views.cliente,name="cliente"),
    path("cita/",views.cita,name="cita"),
    path("pagos/",views.pagos,name="pagos"),
]