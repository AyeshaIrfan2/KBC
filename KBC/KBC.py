import os 

print("-------------- Welcome To KBC: Kon Banega Crorepati --------------")
print("="*60)
print("               Here are the rules for the competition:")
print("="*60)
print("\n1. you will be given questions and 4 option to select from")
print("\n2. you will have to select the correct option")
print("\n3. you will be given points for each correct answer")
print("\n4. you will be given only one life, if you select the wrong answer you will lose the game")
print("\n5. you can use the lifeline to get a hint for the question")
print("\n6. you can use the skip option to skip the question")
print("\n7. you can use the 50-50 option to eliminate two wrong options")
print("\n8. if you lose then you will only get the money till the correct questions")
print("\n9. if you win then you will get the grand prize")
print("\n10. you can quit the game at any time and take the money you have earned so far")
print("\nIf you don't have any problem with the rules then let's start the game!")
input("\nPress Enter to continue...")
os.system('cls')

print("Let's Start The Game!")

print("Please Select The Dataset You Want To Use:")
print("1. comp")
print("2. history")
while True:
    dataset_choice = input("Enter the number corresponding to your choice: ")
    if dataset_choice == '1':
        dataset_name = 'comp'
        break
    elif dataset_choice == '2':
        dataset_name = 'history'
        break
    else:
            print("Invalid choice. Please select either 1 or 2.")

comp_question=[
     ["Which of the following is not a programming language?",
     "A.Python",
     "B.Java",
     "C. HTML",
     "D.C++", 
     "C"],
     ["which language is used for AI/ML?",
     "A. C++",
     "B. HTML",
     "C. COBOL",
     "D. PYTHON",
     "D"],
     ["Which data structure uses FIFO?",
     "A. Stack",
     "B. Queue",
     "C. Tree",
     "D. Graph",
     "B"],
     ["Which of the following is not a database management system?",
      "A. MySQL",
      "B. Oracle",
      "C. MongoDB",
      "D. Microsoft Excel",
      "D"],
     ["Which company created windows?",
     "A. Apple",
     "B. Google",
     "C. Microsoft",
     "D. IBM",
     "C"]]

history_questions = [

    ["Who was the founder of Pakistan?",
     "A. Allama Iqbal",
     "B. Liaquat Ali Khan",
     "C. Quaid-e-Azam Muhammad Ali Jinnah",
     "D. Sir Syed Ahmed Khan",
     "C"],

    ["In which year did Pakistan gain independence?",
     "A. 1945",
     "B. 1947",
     "C. 1950",
     "D. 1930",
     "B"],

    ["Who was the first Prime Minister of Pakistan?",
     "A. Liaquat Ali Khan",
     "B. Ayub Khan",
     "C. Zulfiqar Ali Bhutto",
     "D. Benazir Bhutto",
     "A"],

    ["World War II ended in which year?",
     "A. 1944",
     "B. 1945",
     "C. 1946",
     "D. 1948",
     "B"],

    ["The Great Wall is located in which country?",
     "A. India",
     "B. Japan",
     "C. China",
     "D. Korea",
     "C"]
]

prizes=[1000, 5000, 10000, 50000, 100000]

print("You have selected the", dataset_name, "dataset. Let's start the game!")
if dataset_name == 'comp':
    questions = comp_question
else:
    questions = history_questions

score = 0

for i in range(len(questions)):

    os.system('cls')

    print("="*60)
    print("               KON BANEGA CROREPATI")
    print("="*60)

    print("\nQuestion", i+1)
    print("-"*60)
    print(questions[i][0])
    print("-"*60)

    # Printing options nicely
    for j in range(1, 5):
        print("   ", questions[i][j])

    print("\n" + "-"*60)
    print("Prize for this question: Rs.", prizes[i])
    print("Your current winnings: Rs.", score)
    print("-"*60)

    answer = input("Enter your answer (A/B/C/D): ")

    if answer.upper() == questions[i][5].upper():
        score = prizes[i]
        print("\nCORRECT ANSWER!")
        print("You have won Rs.", score)
        input("Press Enter to continue...")
    else:
        print("\n WRONG ANSWER!")
        print("Correct answer was:", questions[i][5])
        print("You are taking home Rs.", score)
        print("="*60)
        print("               GAME OVER")
        print("="*60)
        break


