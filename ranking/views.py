from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hola Mundo")
    context_dict = {
        'boldmessage':"Este es el mensaje que viene de views!!"
    }
    return render(request, 'ranking/index.html', context=context_dict)
    