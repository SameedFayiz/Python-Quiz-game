print('****** WELCOME TO THE QUIZ GAME ******')
while True:
    user_choice = input('''Do want to login as:
Press (1) for User
Press (2) for Admin
Press anything else to exit\n''')
    if user_choice == '1':
        import user_module
        # Imports module.

        user_module.user_login()
        # FUNCTION CALL (* function for User part of quiz *)

    elif user_choice == '2':
        import admin_module
        # Imports module.

        admin_module.admin_pass()
        # FUNCTION CALL (* function for Admin part of quiz *)

    else:
        break
        # Terminates the current loop.

print('SEE YOU NEXT TIME\nHAVE A GREAT DAY :)')
