from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from . import views
import random
import json
import logging


#================================================================
def home(request):

    context = {'categories': Category.objects.all()}
    

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,'home/home.html', context)




#================================================================
def quiz(request):

    return render(request,'quiz/quiz.html')



#================================================================
def submit_quiz(request):
    if request.method == 'POST':
        
        submitted_answers = request.POST.getlist('answers')

        
        total_score = 0
        for answer_id in submitted_answers:
            answer = Answer.objects.get(pk=answer_id)
            if answer.is_correct:
                total_score += answer.question.marks

        # Afficher le score à l'utilisateur
        return render(request, 'quiz/score.html', {'score': total_score})

    
    return redirect('quiz')


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
  #Cela vous permettra de vous assurer que la catégorie est valide avant de continuer.    
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Quelque chose va pas!!!")

    





