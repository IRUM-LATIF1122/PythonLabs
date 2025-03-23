# Displaying the initial message to the user
print('Press help if you need any help')

# Variable to track whether the car is started or not
start_status = False

# Taking user input and converting it to lowercase
choice = input('>').lower()

# Infinite loop to keep the game running until the user chooses to quit
while True:
    # If user enters 'start'
    if choice == 'start':
        if start_status:  # Checking if the car is already started
            print('Car is already started.')
        else:
            start_status = True  # Changing status to started
            print('Car started .... Ready to go')

    # If user enters 'stop'
    elif choice == 'stop':
        if not start_status:  # Checking if the car is already stopped
            print('Car is already stopped.')
        else:
            start_status = False  # Changing status to stopped
            print('Car stopped')

    # If user enters 'quit', exit the loop
    elif choice == 'quit':
        break  # Ends the game

    # If user enters 'help', display available commands
    elif choice == 'help':
        print('Start  -->  to start the car')
        print('Stop   -->  to stop the car')
        print("Quit   -->  to quit the game")

    # If the input is invalid, prompt the user
    else:
        print('Invalid input')

    # Asking for the next input inside the loop to continue the game
    choice = input('>').lower()
