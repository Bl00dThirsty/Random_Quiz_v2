from django.shortcuts import render
from .models import Candidat
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def validate_phone_number(phone_number):
    # Supprimer les caractères non numériques du numéro de téléphone
    phone_number = ''.join(filter(str.isdigit, phone_number))

    # Vérifier si le numéro de téléphone est valide
    if len(phone_number) == 9:
        # Ajouter le préfixe "+237" et le formatage du numéro
        formatted_phone_number = "6" + phone_number[:2] + " " + phone_number[2:4] + " " + phone_number[4:6] + " " + phone_number[6:]
        return formatted_phone_number

    return None


def signup(request, *args, **kwargs):

    if request.method == 'POST':

        name = request.POST['name']
        forename = request.POST['forename']
        code = request.POST['code']
        date = request.POST['date']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        formatted_phone_number = validate_phone_number(phone_number)
    #.signup != .create
        saved_name = request.session.get('name')
        saved_forename = request.session.get('forename')
        saved_code = request.session.get('code')
        saved_date = request.session.get('date')
        saved_email = request.session.get('email')
        saved_phone = request.session.get('phone_number')
        saved_password = request.session.get('password')

        if date:
            if formatted_phone_number:
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
            else:
                return redirect('error')
        else:
            return redirect('error')
       
    return render(request, 'accounts/signup.html')#1

@login_required
def retour(request):
    try:
        id_user = request.user.id
        candidat = Candidat.objects.get(id=id_user)
        id_user = id_user
        candidat.delete()
    except Candidat.DoesNotExist:
        
        return redirect('error')  
    return render(request, 'accounts/retour.html', {'user_id': id_user})
# Create your views here.
