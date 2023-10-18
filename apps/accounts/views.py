from django.shortcuts import render
from .models import Candidat
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
            newCandidat = User.objects.create_user(name, code, password)
            if newCandidat:
                login(request, newCandidat)
                return redirect('home')
            else:
                print('error')
    
       
    return render(request, 'accounts/signup.html')#1

@login_required
def retour(request):
    try:
        id_user = request.user.id
        candidat = Candidat.objects.get(id=id_user)
        id_user = id_user
        candidat.delete()
    except Candidat.DoesNotExist:
        
        print('page_not_found')  
    return render(request, 'accounts/retour.html', {'user_id': id_user})
# Create your views here.
