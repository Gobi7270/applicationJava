print('Welcome to AskPython Quiz')
answer = input('Are you ready to play the Quiz? (yes/no): ')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = input('Question 1: What is your favorite programming language?')
    if answer.lower() == 'python':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    # Add more questions here...
    answer = input('Question 2: What is your favorite Sports?')
    if answer.lower() == 'cricket':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    print(f'Thank you for playing! You attempted {score} questions correctly!')
    mark = (score / total_questions) * 100
    print(f'Marks obtained: {mark}')
    print('BYE!')
