from django.shortcuts import render
from familiares.models import Hermelo_family

def family_mermbers(request):
    family_member1= Hermelo_family.objects.create(name= "olivia", age= 8, date_birth= "08/02/2014", email= "olita2014@gmail.com")
    context= {
        "family_member1" : family_member1
    }
    return render(request, "familymembers.html", context=context)

def lista_family(request):
    familiares= Hermelo_family.objects.all()
    context= {
        "familiares": familiares
    }
    return render(request, "family_list.html", context=context)
