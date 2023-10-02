
const answerCheckboxes = document.querySelectorAll('.form-check input[type="checkbox"]');

  function checkAnswer(event, currentUid) {
    // Désactiver toutes les autres réponses
    answerCheckboxes.forEach((checkbox) => {
      if (checkbox.id !== currentUid) {
        checkbox.disabled = true;
      }
    });
  }

  //checkAnswer(event, uid) {
    //this.questions.forEach(question => {
      //if (question.uid === uid && !question.answered) {
        //question.answered = true;
        //const selectedAnswer = question.answers.find(answer => answer.answer === event.target.value);
        //if (selectedAnswer) {
          //if (selectedAnswer.is_correct) {
            //console.log('reponse juste');
            //alert('hurrrr correcte');
          //} else {
            //console.log('reponse fausse');
          //}
        //}
      //}
      //if (question.uid !== uid) {
        //  question.disabled = true;
          //console.log('desactiver');
      //}
    //});
  //},
