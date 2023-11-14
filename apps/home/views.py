from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from apps.accounts.models import Candidat
from . import views
import random
import json
import logging


#================================================================
@login_required
def home(request):

    context = {'categories': Category.objects.all()}
    

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home/home.html', context)




#================================================================
@login_required
def quiz(request):
    user_score = request.GET.get('userScore'),   
    context = {'category': request.GET.get('category')}

    return render(request,'quiz/quiz.html', context)

#================================================================
"""
def submit_quiz(request):
    if request.method == 'POST':
        
        submitted_answers = request.POST.getlist('answers')

        
        total_score = 0
        for answer_id in submitted_answers:
            answer = Answer.objects.get(pk=answer_id)
            if answer.is_correct:.
                total_score += answer.question.marks

        # Afficher le score à l'utilisateur
        return render(request, 'quiz/score.html', {'score': total_score})

    
    return redirect('quiz')
    """


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
  #Cette vue renverra un objet JSON contenant les questions correspondantes à la catégorie sélectionnée.    
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Quelque chose ne va pas!!!")

    





