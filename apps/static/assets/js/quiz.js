"use strict";
const quizBox = document.querySelector('.quiz-box');
const nextBtn = document.querySelector('.next-btn');
var app = new Vue({
      el: '#app',
      delimiters: ['[[', ']]'],
      data() {
        return {
          category: '{{category}}',
          questions: [],
          currentQuestion: null,
          userScore: 0,
        };
      },
      methods: {
        getQuestions() {
            var _this = this;
            return fetch(`/api/get-quiz/?category=${this.category}`)
                .then(response => response.json())
                .then(result => {
                console.log(result);
                _this.questions = result.data;
                if (_this.questions.length > 0) {
                    _this.currentQuestion = _this.questions[0];
                }
                });
            },
        
        checkAnswer(event, uid, selectedAnswer) {
          this.questions.forEach(question => {
          if (question.uid === uid && !question.answered) {
            question.answered = true;
              if (selectedAnswer) {
                if (selectedAnswer.is_correct) {
                  console.log('reponse juste');
                  alert('hurrrr correcte');
                  userScore += 1;
                } else {
                  console.log('reponse fausse');
                }
              }
          }
          if (question.uid !== uid) {
            question.disabled = true;
            console.log('desactiver');
          }
          });
        },
        showResultBox() {
          quizBox.classList.remove('active');
          result_box.classList.add('active');

          const score_text = document.querySelector('.score-text');
          score_text.textContent = `Votre score est de ${userScore} sur ${questions.length}`;

          if(userScore < 5){
              TryAgain.classList.add('active');
          }
          else{
              TryAgain.classList.remove('active');
          }



          const circularProgress = document.querySelector('.cicular-progress');
          const progressValue = document.querySelector('.progress-value');

          let progressStartValue = -1;
          let progressEndValue = (userScore / questions.length) * 100;
          let speed = 20;

          let progress = setInterval(() => {
              progressStartValue++;
              //console.log(progressStartValue);
              progressValue.textContent = `${progressStartValue}%`;
              circularProgress.style.background = `conic-gradient(#c40094 ${progressStartValue * 3.6}deg, rgba(255, 255, 255, .1) 0deg)`;


              if (progressStartValue == progressEndValue) {

                  clearInterval(progress);

              }

          }, speed);
        },
        nextQuestion() {
            const currentIndex = this.questions.indexOf(this.currentQuestion);
            const nextIndex = currentIndex + 1;
            if (nextIndex < this.questions.length) {
            this.currentQuestion = this.questions[nextIndex];
            }
            else {
            this.showResultBox();
            }
        },
        
      },
      created() {
        this.getQuestions();
      }
    });