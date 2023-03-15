from django.shortcuts import render

# Create your views here.

def MI(request):
    d={'Name':'Manohar','Location':'Kurnool'}
    return render(request,'MI.html',context=d)