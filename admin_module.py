def admin_pass():
    """Asks the user to enter password"""
    with open('TEXT_FILES(QUIZZES)/admin_pass.txt') as f:
        # Opens the file in which password is saved.

        data = f.read()
        # Reads the password and saves it in a variable.

    password = input('Enter password:')
    # Asks the user to input the password

    if password == data:
        # Checks if the password is correct.

        admin()
        # FUNCTION CALL(* runs the administrator code *)

    else:
        # If the password is incorrect prints the following statement.

        print('Incorrect Password :(')


def change_pass():
    while True:
        print("Password's length should be between 7 to 15 characters :)")
        password = input('Enter a new Password:')
        # Takes Password as input from the user.

        if 7 <= len(password) <= 15:
            # Checks if the Password length is correct.

            with open('TEXT_FILES(QUIZZES)/admin_pass.txt', 'w') as f:
                # Opens the file in write mode.

                f.write(password)
                # Writes the Password into the file.

                break
                # Terminates the current loop.


def admin():
    """Administrator part of the Quiz"""
    while True:
        print('You are logged in as ADMINISTRATOR')
        choice = input('''
Choose your desired subject:
Press (1) for PHYSICS
Press (2) for MATHS
Press (3) for COMPUTER SCIENCE
Press (4) to change Password
Press anything else to go back\n''')
        if choice == '1':
            file_name = 'TEXT_FILES(QUIZZES)\physics.txt'
            # Assigns the filename of desired subject to a variable.

        elif choice == '2':
            file_name = 'TEXT_FILES(QUIZZES)\maths.txt'
            # Assigns the filename of desired subject to a variable.

        elif choice == '3':
            file_name = 'TEXT_FILES(QUIZZES)\comp_sci.txt'
            # Assigns the filename of desired subject to a variable.

        elif choice == '4':
            change_pass()
            # FUNCTION CALL(* for changing the Password of the Administrator *)

            continue
            # Continue the loop from the start.

        else:
            break
            # Terminates the current loop.

        while True:
            choice_2 = input('''
Do you want to read or edit the quiz:
Press (1) to read questions
Press (2) to remove questions
Press (3) to add questions
Press anything else to go back\n''')
            if choice_2 == '1':
                read_func(file_name)
                # FUNCTION CALL(* for viewing the Questions, Options and the Answers *)

            elif choice_2 == '2':
                remove_func(file_name)
                # FUNCTION CALL(* for removing the Questions, Options and the Answers *)

            elif choice_2 == '3':
                add_func(file_name)
                # FUNCTION CALL(* for adding the Questions, Options and the Answers *)

            else:
                break
                # Terminates the current loop.


def read_func(file_name):
    """Views the content of the file.
    Takes name of the text file as an argument."""
    with open(file_name) as f:
        # Opens the file in which Questions are saved.

        questions = f.readlines()
        # Creates a list of the questions, options and answers.

    for i in range(0, len(questions), 5):
        # Iterates over the questions list indexes.

        print(str(int((i + 5) / 5)) + '.' + questions[i], end='')
        # Prints the Question number and Question from sub-list.

        print('', questions[i + 1], questions[i + 2], questions[i + 3], questions[i + 4])
        # Print Options and the answer from sub-list.


def remove_func(file_name):
    """Removes the desired content (Question, Options and Answer) of the file.
    Takes name of the text file as an argument.
    Removes the desired question bank."""
    with open(file_name) as f:
        # Opens the file in which Questions are saved.

        question_bank = f.readlines()
        # Creates a list of the questions, options and answers.

    a = str(int(len(question_bank) / 5))
    # Total number of questions

    question_index = (int(input('Which question do you want to remove?\n(1-' + a + ')')) - 1)
    # Index of Question in list.

    for i in range(0, 5):
        question_bank.pop(question_index * 5)
        # Pops or removes the Question, it's Options and Answer in list

    with open(file_name, 'w') as f:
        # Opens the file in write mode.

        for j in range(0, len(question_bank)):
            # Iterates over the question_bank list indexes.

            f.write(question_bank[j])
            # Writes the list element in file.


def add_func(file_name):
    """Adds (Question, Options and Answer) to the content of the file.
        Takes the name of the text file as argument.
        Appends the Question bank which is taken as input at the very last of the file."""
    with open(file_name, 'a') as f:
        # Opens the file in append mode in which Questions are saved.

        print('''
Format for adding questions:
<QUESTION>
<a)OPTION-1>
<b)OPTION-2>
<c)OPTION-3>
ANSWER = <a)OPTION-1>''')
        f.write(input('Enter the question:') + '\n')
        # Appends or adds Question in file at last.

        for i in range(1, 4):
            f.write(input('Enter option_' + str(i)) + '\n')
            # Appends or adds Options in file at last.

        f.write('ans:' + input('Enter the answer:') + '\n')
        # Appends or adds Answer in file at last.
