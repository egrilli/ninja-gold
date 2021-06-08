from django.shortcuts import render, HttpResponse,redirect
from time import localtime, strftime
from django.http import JsonResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if "consola" not in request.session:
        request.session["consola"]=[]

    return render(request,"index.html")

def processMoney(request):
    
    if request.method == "POST":

        oro_calcular = 0
        opcion=''

        if request.POST["juego"] == "farm":
            oro_calcular=random.randint(10,20)
            opcion=request.POST["juego"]
            

        if request.POST["juego"] == "cave":
            oro_calcular=random.randint(5,10)
            opcion=request.POST["juego"]
            

        if request.POST["juego"] == "house":
            oro_calcular=random.randint(2,5)
            opcion=request.POST["juego"]
            

        if request.POST["juego"] == "casino":
            oro_calcular=random.randint(-50,50)
            opcion=request.POST["juego"]
        
        
        if oro_calcular >=0: 
            request.session["actividad"]=f"Por trabajar en {opcion} Ganaste {oro_calcular} de Oro! => ({strftime('%d/%m/%Y. %H:%M:%S ',localtime())})"
        else:
            request.session["actividad"]=f"Por trabajar en {opcion} Perdiste {oro_calcular} de Oro! => ({strftime('%d/%m/%Y. %H:%M:%S ',localtime())})"
        
        print(opcion)
        print(oro_calcular)
        request.session['gold'] +=oro_calcular
        request.session["consola"].append(request.session["actividad"])
    return redirect("/app_v2")


def withdraw(request):
    del request.session['gold']
    del request.session["consola"]
    return redirect("/app_v2")

def oroData(request):
    responseData = {
        'oro_data': request.session['gold']
    }
    return JsonResponse(responseData)

