from django.shortcuts import render
from .models import Candidat
from django.shortcuts import redirect



def signup(request, *args, **kwargs):

    if request.method == 'POST':

        name = request.POST['name']
        forename = request.POST['forename']
        code = request.POST['code']
        date = request.POST['date']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    #.signup != .create
        saved_name = request.session.get('name')
        saved_forename = request.session.get('forename')
        saved_code = request.session.get('code')
        saved_date = request.session.get('date')
        saved_email = request.session.get('email')
        saved_phone = request.session.get('phone_number')
        saved_password = request.session.get('password')

        if Candidat.objects.filter(name=name, forename=forename, date=date).exists():
            message_erreur = "Vous avez deja passer le test."
            #return render(request, 'accounts/signup.html', {'message_erreur': message_erreur})
            return redirect('error')

        else:
            newCandidat = Candidat(name=name, forename=forename, code=code,  date=date, phone_number=phone_number, password=password)
            newCandidat.save()
            return redirect('home')
            print(newCandidat.matricule)
    
       
    return render(request, 'accounts/signup.html')#1
# Create your views here.
