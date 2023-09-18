from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from . import views
import random
import json
import logging



#{
#'status' : True
#'data' : [
#    {},
#    
#    ]
#}

def home(request):

    context = {'categories': Category.objects.all()}
    

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home.html', context)

"""
def quiz(request):
    current_question = None  
    context = {'category' : request.GET.get('category'),
                #'current_question_index': current_question_index,
            #'current_question': current_question,
     }

    return render(request, 'quiz.html', context)




"""
def quiz(request):
    if request.method == 'GET':
        category = request.GET.get('category')

        try:
            category_obj = Category.objects.get(category_name=category)
            questions = Question.objects.filter(category=category_obj)
            questions = list(questions)

            if questions:
                current_question_index = 0
                current_question = questions[current_question_index]
                context = {
                    'category': category,
                    'current_question_index': current_question_index,
                    'current_question': current_question,
                }
                return render(request, 'quiz.html', context)
            else:
                return HttpResponse("Aucune question trouvée pour cette catégorie.")

        except Category.DoesNotExist:
            return HttpResponse(f"La catégorie '{category}' n'existe pas.")

        except Exception as e:
            logging.exception("Une erreur s'est produite dans la vue quiz.")
            return HttpResponse("Quelque chose va mal!!!")

    elif request.method == 'POST':
        # Logique pour gérer les requêtes POST (passage à la question suivante)
        pass

    # Renvoyer une réponse HTTP appropriée pour toutes les autres conditions
    return HttpResponse("Méthode HTTP non prise en charge.")
    
#==========================================
    """


    current_question_index = 0
    category = request.GET.get('category')
    
    try:
        category_obj = Category.objects.get(category_name=category)
        questions = Question.objects.filter(category=category_obj)
        questions = list(questions)
        
        if current_question_index >= 0 and current_question_index < len(questions):
            current_question = questions[current_question_index]
        else:
            current_question = None  
        
        context = {
            'category': category,
            'current_question_index': current_question_index,
            'current_question': current_question,
        }
    
        return render(request, 'quiz.html', context)
    
    except Category.DoesNotExist:
        return HttpResponse(f"La catégorie '{category}' n'existe pas.")
    
    except Exception as e:
        return HttpResponse("Quelque chose va mal!!!")"""


#================================================================
    

def get_quiz(request):
    try:
        question_objs = Question.objects.all()



        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        question_objs = list(question_objs)

        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs: 
            data.append({
                "uid" : question_obj.uid,
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
            })

        payload = {'status' : True, 'data' : data}
        
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Quelque chose va mal!!!")

    
def getQuestions(request):
    try:
        category_id = request.GET.get('category')
        category = Category.objects.get(id=category_id)
        questions = Question.objects.filter(category=category)
        if not questions:
            return JsonResponse({'message': 'Aucune question disponible pour cette catégorie.'})
        serialized_questions = [{'question': q.question, 'marks': q.marks} for q in questions]
        return JsonResponse({'questions': serialized_questions})
    except Category.DoesNotExist:
        return JsonResponse({'message': 'La catégorie spécifiée n''existe pas.'})
    except Exception as e:
        return JsonResponse({'message': 'Une erreur sest produite lors de la récupération des questions.'})


#Cela vous permettra de vous assurer que la catégorie est valide avant de continuer.675457214
"""def getQuestions(request):
    category_id = request.GET.get('category')
    questions = Question.objects.filter(category_id=category_id)
    serialized_questions = [{'question': q.question, 'marks': q.marks} for q in questions]
    return JsonResponse({'questions': serialized_questions})"""


#Cette vue renverra un objet JSON contenant les questions correspondantes à la catégorie sélectionnée.