from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Neeraj',
                                             'st':5, 
                                             'languages':['python','JavaScript','Node','PHP']
                                            })

def index(req):
    return render(req,"index.html",{"name":"Neha",
                                    "city":"Bpl",
                                    "subject":["Python","Django","PHP"]})
