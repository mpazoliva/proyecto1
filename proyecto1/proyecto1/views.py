from django.http import HttpResponse
from datetime import datetime
from django.template import Template
from django.template.context import Context

def saludo(response):
    return HttpResponse("Hola Preciosa!")

def segunda_vista(response):
    return HttpResponse("TE AMO")

def dia(response):
    variable= datetime.now()
    return HttpResponse(f"Hoy es {variable} ")

def nombre(response, nombre):
    fecha= datetime.now()
    return HttpResponse(f" {nombre} es hermosa hoy ({fecha}) y siempre! ")

def probando_template(self):
    miHTML = open("C:/Users/marti/Documents/PHYTON/django1/proyecto1/proyecto1/plantillas/template1.html")
    plantilla = Template(miHTML.read())
    mi_contexto= Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)