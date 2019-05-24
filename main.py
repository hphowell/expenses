'''
Author: Hayden Howell

This tool allows the user to view transactions from their bank statements (imported from CSV files) and calculate their
average monthly savings.
'''

import databaseInterface
import sqlite3

def main():
    userInput = 0
    while userInput != 4:
        userInput = int(input('Select an option:\n1) View transactions\n2) Monthly savings approximation\n3) Import CSV\n4) Quit\n'))
        if userInput == 1:
            databaseInterface.allTransactions('data.db', ['chase'])
            print('\n')
        elif userInput == 2:
            print(savings())
        elif userInput == 3:
            importCSVInputs()
        elif userInput == 4:
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

            monthlySavings = str(round(databaseInterface.calculateSavings('data.db', salary), 2))
            savingsString = 'Your average monthly savings after all expenses is $' + monthlySavings
            return savingsString

def importCSVInputs():
    import os

    csvPath = input('Please enter the path of the CSV file that you would like to import: ')
    exists = os.path.isfile(csvPath)
    while not (exists and (csvPath[-4:] == '.csv')):
        csvPath = input('Please input a valid path ending with ".csv": ')
        exists = os.path.isfile(csvPath)
    table = input('Please enter the table into which you would like to import the CSV file: ')
    tables = []
    while not tables:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "' + table + '";')
        tables = c.fetchall()
        conn.close()
        if not tables:
            table = input(
                'The table does not exist. Please enter an existing table or press return to return to the menu: ')
            if table == '':
                break
    if tables:
        databaseInterface.importFromCSV(csvPath, 'data.db', table)
        print('Import succeeded')


if __name__ == '__main__':
    main()
