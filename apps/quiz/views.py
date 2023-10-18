from django.shortcuts import render


#from django.http import HttpResponse
def index(request):


    
    return render(request, 'quiz/index.html')

def error(request):
    return render(request, 'quiz/error.html')
 
def paiement(request):
    return render(request, 'quiz/paiement.html')