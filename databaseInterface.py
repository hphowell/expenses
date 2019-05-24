def importFromCSV(csvPath, datbasePath, table):
    import sqlite3
    #create connection to database
    conn = sqlite3.connect(datbasePath)
    c = conn.cursor()

    #query database to find highest existing primary key
    result = c.execute('select max(ID) from ' + table)

    #put query results in maxID
    for line in result:
        maxID = line
    if maxID[0] == None:
        startIndex = 1
    else:
        startIndex = maxID[0] + 1

    lineNumber = 0
    rowID = startIndex

    #open the CSV file
    file = open(csvPath, 'r')

    #loop through the lines in the file
    for line in file:
        #omit first line that has header information
        if lineNumber != 0:
            #remove newline
            line = line.strip('\n')
            #split line into list
            itemList = line.split(',')
            line = ''
            #for items in the list, add quotes around them if they are not the last item (which is a float)
            for i in range(len(itemList)):
                if i != len(itemList) - 1:
                    itemList[i] = '"' + itemList[i] + '"'
                #add items to a string
                line = line + ',' + itemList[i]
            #create SQL statement to insert line
            sqlString = "insert into " + table + " values(" + str(rowID) + line + ");"
            #execute SQL statement
            c.execute(sqlString)
            rowID += 1
        lineNumber += 1
    file.close()

    #commit database changes
    #conn.commit()
    #close database connection
    conn.close()

def allTransactions(databasePath, tables):
    import sqlite3
    # create connection to database
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()

    for table in tables:
        #loop through rows in table to return all transactions
        for row in c.execute('select * from ' + table):
            print(row)

        conn.close()

def calculateSavings(databasePath, salary):
    import sqlite3
    # create connection to database
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()

    #pull out the latest transaction date
    for row in c.execute('select max(transDate) from chase'):
        maxDate = row[0]

    #determine the month and year of latest transaction date
    maxMonth = int(maxDate[:2])
    maxYear = int(maxDate[6:])

    #pull out the earliest transaction date
    for row in c.execute('select min(transDate) from chase'):
        minDate = row[0]

    # determine the month and year of earliest transaction date
    minMonth = int(minDate[:2])
    minYear = int(minDate[6:])

    months = 0
    #count number of months for which there is data
    for i in range(minYear, maxYear + 1):
        for j in range(minMonth, maxMonth + 1):
            #TODO will use later when implementing only pulling full months
            #if len(str(j)) == 1:
                #j = '0' + str(j)
            months += 1

    #sum up total expenses
    for row in c.execute('select sum(amount) from chase'):
        totalExpenses = row[0]
    #calculate average expenses per month
    averageExpenses = totalExpenses / months

    #close database connection
    conn.close()

    #calculate and return savings
    savings = salary - averageExpenses
    return savings