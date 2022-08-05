from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse ###essa classe httpresponse cuida da criação de responses, que é devolvida pro navegador pelo retorno da função home, da linha 9
import datetime

def home(request):          ###toda view é uma função que recebe request como parâmetro
    now = datetime.datetime.now()
    html = "<html><body> It is now %s</body></html>" % now
    return HttpResponse(html)

    