import databaseInterface

def main():
    userInput = 0
    while userInput != 3:
        userInput = int(input('Select an option:\n1) View transactions\n2) Monthly savings approximation\n3) Quit\n'))
        if userInput == 1:
            databaseInterface.allTransactions()
        elif userInput == 2:
            print(savings())
        elif userInput == 3:
            print('Exiting')
        else:
            print('Input a valid number.\n')

def savings():
    salaryChoice = 0
    while salaryChoice == 0:
        salaryChoice = int(input('How would you like to enter your after tax salary?\n1) Yearly\n2) Monthly\n3) Biweekly\n'))
        validChoices = [1, 2, 3]
        if not salaryChoice in validChoices:
            print('Input a valid number.\n')
            salaryChoice = 0
        else:
            salary = int(input('Please enter your salary: '))
            if salaryChoice == 1:
                salary /= 12
            elif salaryChoice == 3:
                salary = salary * 26 / 12

            monthlySavings = str(round(databaseInterface.calculateSavings(salary), 2))
            savingsString = 'Your average monthly savings after all expenses is $' + monthlySavings
            return savingsString


if __name__ == '__main__':
    main()
