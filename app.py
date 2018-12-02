from time import sleep
import os

#-------------------------------------------------------------------------------------------------
# Credits: I would like to give credit to Mike Dane as I build this app from one of his videos. 
# Original Author: Mike Dane - Youtube Channel for training videos 
# Link: https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=190s
#-------------------------------------------------------------------------------------------------


def question_key_gen(data_bank):
    with open(data_bank, 'r') as f:
        bank = {}
        question: str = f.readline().rstrip()
        question = question.replace('\\n', '\n')
        answer: str = f.readline().rstrip()
        while question != 'EOF':
            bank[question] = answer
            question = f.readline().rstrip()
            question = question.replace('\\n', '\n')
            answer = f.readline().rstrip()
        f.close()
        return bank


def intro():
    print("\n\n")
    print("Welcome to Computer Networking Quiz!\n\n")
    sleep(2)
    print("Let's Start! \n")

def test_select():
    chapter = input('Enter Chapter: ')
    filename_bank = 'Chapter_'+str(chapter)+'_questions'
    question_key = question_key_gen(filename_bank)
    return question_key

def run_test(question_key):
    score = 0
    for question, answer in question_key.items():
        if os.name == 'nt':
            os.system("cls") # clears the screen must use import os
        else:
            os.system('clear')
        sleep(1)
        print(str(question))
        user_answer = input('\n :: ')
        if os.name == 'nt':
            os.system("cls") # clears the screen must use import os
        else:
            os.system('clear')
        if user_answer == answer or user_answer == answer.lower():
            score += 1
            print("\nThe Answer: " + answer + " Correct\n\n-----------------------------------------------------\n\n")
            sleep(3)
        else:
            print("\nThe Answer: " + answer + " Incorrect\n\n-----------------------------------------------------\n\n")
            sleep(3)
    
    print("\n\n\n\n")
    if os.name == 'nt':
        os.system("cls") # clears the screen must use import os
    else:
        os.system('clear')
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


intro()
question_key = test_select()
run_test(question_key)
