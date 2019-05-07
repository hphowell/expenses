import databaseInterface

def main():
    userInput = 0
    while userInput != 3:
        userInput = int(input('Select an option:\n1) View transactions\n2) Monthly savings approximation\n3) Quit\n'))
        if userInput == 1:
            databaseInterface.allTransactions()
        elif userInput == 2:
            print('To be implemented')
        elif userInput == 3:
            print('Exiting')
        else:
            print('Input a valid number.')

if __name__ == '__main__':
    main()