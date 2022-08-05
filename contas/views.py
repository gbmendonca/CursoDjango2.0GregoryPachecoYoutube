from django.shortcuts import render
#from django.http import HttpResponse ###essa classe httpresponse cuida da criação de responses, que é devolvida pro navegador pelo retorno da função home, da linha 9
import datetime

# Criação de views

def home(request):          ###toda view é uma função que recebe request como parâmetro
    now = datetime.datetime.now()
    #html = "<html><body> It is now %s</body></html>" % now
    
    return render(request, 'contas/home.html')          # aqui a função home está retornando a request e o template chamado home.html localizado na pasta contas

    