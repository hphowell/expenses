def importFromCSV(path, table):
    import sqlite3
    #create connection to database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    #query database to find highest primary key
    result = c.execute('select max(ID) from chase')

    #put query results in maxID
    for line in result:
        maxID = line

    startIndex = maxID[0] + 1

    lineNumber = 0
    rowID = startIndex

    #open the CSV file
    file = open(path, 'r')

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

    for row in c.execute('select * from chase'):
        print(row)

    #commit database changes
    conn.commit()
    #close database connection
    conn.close()

def main():
    importFromCSV('test.CSV', 'chase')

main()