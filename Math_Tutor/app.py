# Math Tutor
# Create an application to practice multiplication tables.
# User specifies number of random practice questions.
# User is presented with a prompt e.g. 5 X 5 = and inputs the answer for each question.
# When all questions are answered: print out the following info:
#   a.  Some form of "Thanks for playing greeting".
#   b.  Number of correct answers/total answers.
#   c.  % correct.

#  Bonus 1:  Measure/present the time it took to answer questions: in total and per question.
#  Bonus 2:  Let user specify how high the numbers used should be.
#  Bonus 3:  Show all questions and answers at end.


import random
import time


print('                    _  ________  ___  ___  ')
print('   /\     /\       / \ |__   __| | |__| |  ')
print('  /  \   /  \     /   \   | |    |  __  |  ')
print(' / /\ \ / /\ \   / / \ \  | |    | |  | |  ')
print('/ /   \  /  \ \ / /   \ \ | |    | |  |    ')
print('______  __   __  ______   _____  _______   ')
print('|_   _| | |  | | |_   _| |  _  | |  ___|   ')
print('  | |   | |  | |   | |   | |_| | | |\ \    ')
print('  | |   | |__| |   | |   |     | | |  \ \  ')

input('\nPress enter to begin!')


while True:
    qa_dict = {}
    question_number = 0
    num_of_questions = str(input('How many questions would you like for your quiz?: '))

    try:
        num_of_questions = int(num_of_questions)
    except ValueError:
        print('Please enter a number')
    else:
        while True:
            highest_num = str(input('What is the highest number you would like to use in this quiz?'))
            try:
                highest_num = int(highest_num)
            except ValueError:
                print('Please enter a number')
            else:
                correct = 0
                incorrect = 0
                total_time = 0
                print('Great! Let\'s get started')

                for x in range(num_of_questions):
                    num1 = random.randint(1, highest_num)
                    num2 = random.randint(1, highest_num)
                    start = time.time()
                    answer = input((str(num1) + ' x ' + str(num2) + ' = '))

                    try:
                        answer = int(answer)
                    except ValueError:
                        print('Please enter a number!  That counts as an incorrect answer!')
                        continue

                    end = time.time()
                    question_time = end - start
                    total_time += question_time
                    question_number += 1
                    qa_dict[str(question_number) + ': ' + str(num1) + ' x ' + str(num2) + ' = '
                            + str(answer)] = num1 * num2

                    if num1 * num2 == int(answer):
                        correct += 1
                    else:
                        incorrect += 1

                print('Thank you for playing!')
                print('You got ' + str(correct) + ' out of ' + str(num_of_questions))
                print('That is ' + str(round(((correct / num_of_questions) * 100), 2)) + '%')
                print('It took you a total of ' + str(round(total_time, 2)) + ' seconds! With an average of ' +
                      str(round((total_time / num_of_questions), 2)) + ' seconds per question!')
                print('Here are your questions and answers: ')

                for key, value in qa_dict.items():
                    print(str(key) + ': The correct answer was ' + str(value))

                exit()
