from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, guild!")

def guildDetails(request, guild_id):
    return HttpResponse("Détail de la guilde %i" % guild_id)

def implantationDetails(request, implantation_id):
    return HttpResponse("Détail de l'implantation " % implantation_id)
