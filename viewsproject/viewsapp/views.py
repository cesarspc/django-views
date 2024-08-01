from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Little Lemon Restaurant")

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    return render(request, "form.html")

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def drinks(request, drink_name):
    dic = {
        "mocha" : "type of coffee",
        "tea" : "type of beverage",
        "lemonade" : "type of refreshment"
    }

    choice_of_drink = dic.get(drink_name)
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)