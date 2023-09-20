from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from . import views
import random
import json
import logging



#{
#   'status' : True
#   'data' : [
#       {},
#    
#    ]
#}

def home(request):

    context = {'categories': Category.objects.all()}
    

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home/home.html', context)
def quiz(request):

    return render(request,'quiz/quiz.html')
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
    return HttpResponse("Quelque chose va pas!!!")

    



#Cela vous permettra de vous assurer que la catégorie est valide avant de continuer.675457214
"""def getQuestions(request):
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
def getQuestions(request):
    category_id = request.GET.get('category')
    questions = Question.objects.filter(category_id=category_id)
    serialized_questions = [{'question': q.question, 'marks': q.marks} for q in questions]
    return JsonResponse({'questions': serialized_questions})"""


#Cette vue renverra un objet JSON contenant les questions correspondantes à la catégorie sélectionnée.