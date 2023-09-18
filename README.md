# Random Quiz App for Sai I Lama Academy

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.x-green)](https://www.djangoproject.com/)

The Random Quiz App is designed to administer a preliminary quiz for students applying to Sai I Lama Academy in Cameroon. If a student fails the quiz, they will have the option to pay for a second chance.

## Features

- Preliminary quiz for Sai I Lama Academy applicants
- Randomly generated quiz questions
- Multiple-choice format
- Scoring and evaluation of quiz results
- Payment option for a second chance if the student fails

## Technology Stack Feature

- Django Templating Language for rendering HTML templates
- Django Forms for form handling
- Django ORM for database interactions
- Django authentication system for user management

## App Workflow

1. User Registration and Login
   - Students create an account on the app using their email and password.
   - Users can log in to access the quiz and their quiz history.

2. Quiz Questions
   - The app randomly selects a set of questions from a question bank for each quiz attempt.
   - Multiple-choice questions are presented one at a time to the student.
   - Students select an answer and move to the next question.

3. Quiz Evaluation
   - After completing the quiz, the app evaluates the student's answers.
   - The app calculates the score based on the number of correct answers.
   - The quiz result is stored in the database for further analysis.

4. Quiz Retake
   - If the student fails the quiz, they have the option to pay for a second chance.
   - Upon payment, the student can retake the quiz immediately.

## Security Measures

To ensure data security and user privacy, the following measures are implemented:

- User authentication and authorization to protect sensitive data.
- Encryption of user passwords using secure hashing algorithms.
- Input validation and sanitization to prevent common security vulnerabilities.
- Implementation of CSRF protection to prevent cross-site request forgery attacks.
- Proper handling of user sessions and cookies for secure user interactions.

## Installation

To run the Random Quiz App locally, you can follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Bl00dThirsty/Random_Quiz_v2.git
   ```
Navigate to the project directory:

```
cd Random_Quiz_v2
```
Create a virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

On macOS and Linux:

source venv/bin/activate
On Windows:
venv\Scripts\activate
Install the required dependencies:

```
pip install -r requirements.txt
```

Set up the database:

```
python manage.py migrate
```

Create a superuser (admin) account:

```
python manage.py createsuperuser
```

Start the development server:

```
python manage.py runserver
```
Access the app in your web browser at `http://localhost:8000`.

Feel free to reach out if you have any questions or need further information!
