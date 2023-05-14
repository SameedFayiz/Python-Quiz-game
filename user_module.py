def user_login():
    while True:
        choice_1 = input('''
Do you want to take Quiz as:
Press (1) for Anonymous
Press (2) for User
For existing Users:
Press (3) to checks scores
Press anything else to go back\n''')
        if choice_1 == '1':
            quiz_select()
            # FUNCTION CALL(* Contains the code for the quiz filename selection *)

        elif choice_1 == '2':
            user_name = 'SCORES/' + input('Enter your username:') + '.txt'
            # Takes username and saves it in a variable.

            data = quiz_select()
            # FUNCTION CALL(* Contains the code for the quiz filename selection *)
            # quiz_select returns list of quiz_name and score.

            with open(user_name, 'a') as file:
                # Opens file in append mode.

                file.write(data[0] + ' score: ' + str(data[1]) + '\n')
                # Writes the quiz_name and score in file returned by quiz_select.

        elif choice_1 == '3':
            user_name = 'SCORES/' + input('Enter your username:') + '.txt'
            with open(user_name) as file:
                # Opens file and takes username as filename.

                scores = file.readlines()
                # Creates a list of the file.

                scores.sort(reverse=True)
                # Sorts the list in descending order.

            for i in range(len(scores)):
                # Iterates over list indexes.

                print(scores[i])
                # Prints each element of the list.

        else:
            break
            # Terminates the current loop.


def quiz_select():
    """chooses the subject and runs the quiz game"""
    while True:
        print('Which QUIZ do you want to take?')
        choice_2 = input('''
Choose your desired subject:
Press (1) for PHYSICS
Press (2) for MATHS
Press (3) for COMPUTER SCIENCE
Press anything else to go back\n''')
        if choice_2 == '1':
            file_name = 'TEXT_FILES(QUIZZES)\physics.txt'
            # Assigns the filename of desired subject to a variable.

            quiz_name = 'PHYSICS'
        elif choice_2 == '2':
            file_name = 'TEXT_FILES(QUIZZES)\maths.txt'  #
            # Assigns the filename of desired subject to a variable.

            quiz_name = 'MATHEMATICS'
        elif choice_2 == '3':
            file_name = 'TEXT_FILES(QUIZZES)\comp_sci.txt'
            # Assigns the filename of desired subject to a variable.

            quiz_name = 'COMPUTER SCIENCE'
        else:
            break
            # Terminates the current loop.

        print('******WELCOME TO THE', quiz_name, 'QUIZ******')
        print('''
1.There will be 10 questions in the quiz
2.Please only put the MCQ letter in the answer box
3.Try to do the quiz in minimum time\n''')
        with open(file_name) as f:
            # Opens the file in which questions are saved.

            question_bank = f.readlines()
            # Creates a list of the questions, options and answers.

        questions = []
        # Initializes an empty mega-list.

        for i in range(0, len(question_bank), 5):
            # Iterates over the question_bank list indexes.

            question_part = []
            # Initializes an empty sub-list.

            for j in range(0, 5):
                question_part.append(question_bank[j + i])
                # Appends the question, options and answer to sub-list.

            questions.append(question_part)
            # Sub-list is appended to the mega-list.

        display_questions = quiz_game(questions)
        # FUNCTION CALL(* Contains the code for the quiz game *)
        #  Saves the list of questions list and score in a variable returned by quiz_game.

        display_quiz(display_questions[0])
        # FUNCTION CALL(* Contains the code for displaying answers for the quiz *)
        #  Takes the same shuffled list of questions and displays their answers

        return [quiz_name, display_questions[1]]
        # Returns the list of quiz_name and score.


def quiz_game(questions):
    """Code for the Quiz Game"""
    while True:
        import random
        # Imports random build-in module.

        random.shuffle(questions)
        # Shuffle() randomizes the sub-lists inside the mega-list.

        score = 0
        # Initializes the score to 0.

        for i in range(0, 10):
            print(str(i + 1) + '.' + questions[i][0], end='')
            # Prints the Question number and Question from sub-list.

            print('', questions[i][1], questions[i][2], questions[i][3], end='')
            # Prints the Options from sub-list.

            answer = questions[i][4][4]
            # Saves the Answer's options letter from the sub-list into a variable.

            choice = input('enter your ans:')
            # Asks the user to enter his choice.

            if choice == answer:
                score += 1
                # Increases the score count by 1 if Answer matches the User's choice.

        print('Your final score is:', str(score) + '/' + str(len(questions)))
        if score >= 8:
            print('EXCELLENT JOB ;)')
        elif score >= 5:
            print('GOOD JOB')
        else:
            print('TRY HARD NEXT TIME :(')
        retake = input('Do you want to retake the quiz?(Y/N)\n')
        if retake == 'Y' or retake == 'y':
            continue
            # Continues the loop from the start if the user wants to take the quiz again.

        else:
            break
            # Terminates the current loop.

    return [questions, score]
    # Returns the list of shuffled mega-list and scores.


def display_quiz(display_questions):
    """displays question and it's answers"""
    display = input('Do you want to display answers? (Y/N)\n')
    if display == 'Y' or display == 'y':
        for j in range(0, len(display_questions)):
            # Iterates over the mega-list indexes.

            print(display_questions[j][0], display_questions[j][4])
            # Print the Question and it's Answer.
