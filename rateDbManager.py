import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'ratedb')
mycursor = mydb.cursor(buffered = True)
# print(mydb)

# ==================================================
#               Test rate stuff
# ==================================================

def createTestRate() :
    mycursor.execute("CREATE TABLE testRate (artist VARCHAR(255), song VARCHAR(255), score DECIMAL(3, 1), id INT AUTO_INCREMENT PRIMARY KEY)")
    sql = "INSERT INTO testRate (artist, song, score) VALUES (%s, %s, 1)"
    val = [
        ("Jimi Hendrix", "Little Wing"),
        ("Beyonce", "Love On Top"),
        ("Itzy", "Wannabe"),
        ("Kasabian", "Shoot The Runner"),
        ("Chaz and Dave", "Rabbit"),
        ("Nelly Furtado", "Say It Right"),
        ("The Clash", "London Calling"),
        ("J Hus", "Spirit"),
        ("Eagles", "Hotel California"),
        ("Blackpink", "Don''t Know What To Do"),
        ("Olamide", "Wo!"),
        ("JLS", "Kickstart"),
        ("frederic", "Oddloop"),
        ("EXID", "DDD"),
        ("The White Stripes", "Ball And Biscuit"),
        ("The Wanted", "Glad You Came"),
        ("Headie One", "Orf Course"),
        ("The Corals", "Dreaming Of You"),
        ("Kwon Eunbi", "The Flash")
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    
    print("Test rate created.")

#createTestDb()

def deleteTestRate() :

    deleteConfirmation = input("Type 'confirm' only if you are sure you want to delete the test rate. Otherwise type 'cancel'. ")

    if deleteConfirmation == "confirm" :
        mycursor.execute("DROP TABLE testRate")
        print("Test rate deleted.")

    elif deleteConfirmation == "cancel" :
        print("Test rate was not deleted.")

    else :
        print("Input invalid.")

#deleteTestRate()

# ==================================================
#                   Create rate
# ==================================================

def createRate() :
    rateName = input("Please enter the rate name. ")
    mycursor.execute(f"CREATE TABLE {rateName} (artist VARCHAR(255), song VARCHAR(255), score DECIMAL(3, 1), id INT AUTO_INCREMENT PRIMARY KEY)")
    print(f"{rateName} was created.")

# ==================================================
#                   Show rates
# ==================================================

rateList = []

def showRate() :
    mycursor.execute("SHOW TABLES")
    for x in mycursor :
        rateList.append(x)

    for i in rateList :
        print(f"{rateList.index(i)} {i}")
    
    print(f"There are {len(rateList)} rate(s) available.")
    print(30 * '=')

rateSelected = []

def selectRate() :

    if rateList != [] :
        #rateSelectionInput = input("Please select the number of the database you wish to select. ")
        rateSelection = input("Please type out the name of the database you wish to use. ")
        rateSelected.append(rateSelection)
        print(rateSelection)

        #mycursor.execute(f"USE {rateSelection}")
        print(f"You are currently using {rateSelection}.")
        print(30 * '-')
        #print("".join(str(x) for x in rateSelected))
    

    else :
        print("Please run the show databases option first.")

def rateColumns() :
    
    if rateSelected != [] :
        mycursor.execute(f"SELECT * FROM {"".join(str(x) for x in rateSelected)}")
        for x in mycursor :
            print(x)
        print(30 * '=')

    else :
        print("Please select a database.")

rateScores = []

def editScores() :
    
    rateScores = []

    if rateSelected != [] :
        mycursor.execute(f"SELECT * FROM {"".join(str(x) for x in rateSelected)}")
        for x in mycursor :
            score = float(input(f"{", ".join(str(i) for i in x)}: "))

            if 1 <= score <= 10 :
                #print(x)
                #print(x[0])
                song = x[1]
                artist = x[0]
                #print(artist)
                #rateScores.append(score)
                rateScores.append([score, artist, song])
            
            else :
                score = input(f"Please enter a score between 1 and 10.\n{", ".join(str(i) for i in x)}: ")

        #print(rateScores)
        for x in rateScores :
            sql = f"UPDATE testrate SET score = '{x[0]}' WHERE artist = '{x[1]}' AND song = '{x[2]}'"
            #print(sql)
            # AND song = '{x[1]}'
            mycursor.execute(sql)
            mydb.commit()
        print(30 * '=')
        #print(rateScores)
        #rateColumns()

    else :
        print("Please select a database.")

# ==================================================
#               Ballot printing
# ==================================================

def ballotPrint() :
    #sAndA = mycursor.execute(f"SELECT artist, song FROM {"".join(str(x) for x in rateSelected)}")
    #score = mycursor.execute(f"SELECT score FROM {"".join(str(x) for x in rateSelected)}")
    #songDetails = []
    #songScores = []
    mycursor.execute(f"SELECT artist, song, score FROM {"".join(str(x) for x in rateSelected)}")
    for x in mycursor :
        #songDetails.append([x[0], x[1]])
        #songScores.append(x[2])
        print(f"{x[0]} - {x[1]}: {x[2]}")

    '''for x in songDetails :
        songString = f"{" - ".join(str(i) for i in x)}: "
        print(f"{songString}{songScores}")
        #songAndArtistAndScore = (f"{songAndArtist}{score}")
        #print(songAndArtistAndScore)'''

    print(30 * "-")

# ==================================================
#                 Menu options
# ==================================================

# ==================================================
#               Rate management
# ==================================================

dbOption = ()
dbFunctions = ["Return", "Create test rate", "Delete test rate", "Show rates", "Select rate", "Edit ballot", "Print ballot"]

def dbManage() :
    for i in range(len(dbFunctions)) :
        print(i, dbFunctions[i])
    #print(30 * "-")
    return

def manageFunction() :

    dbOption = ()
    
    while dbOption != 0 :

        dbManage()
        dbOption = int(input(f"{30 * '-'}\nChoose option: "))

        if dbOption == 0 :
            selectFunction()

        elif dbOption == 1 :
            createTestRate()

        elif dbOption == 2 :
            deleteTestRate()
        
        elif dbOption == 3 :
            showRate()

        elif dbOption == 4 :
            selectRate()

        elif dbOption == 5 :
            #rateColumns()
            #print("".join(str(x) for x in rateSelected))
            editScores()
            #ballotPrint()

        elif dbOption == 6 :
            ballotPrint()

        else :
            dbOption = int(input(f"{30 * '-'}\nPlease select a valid option: "))

    dbOption = ()

# ==================================================
#               Submitter management
# ==================================================

# ==================================================
#               Ballot management
# ==================================================

dbEditing = ()
editOptions = ["Return", ""]

# ==================================================
#               Initial menu options
# ==================================================

initFunctionality = ()
functionalityOptions = ["Exit", "Manage rates", "Manage submitters", "Manage ballots"]

def showFunctions() :
    for i in range(len(functionalityOptions)) :
        print(i, functionalityOptions[i])

def selectFunction() :

    initFunctionality = ()

    while initFunctionality != 0 :

        showFunctions()
        initFunctionality = int(input(f"{30 * '-'}\nChoose option: "))

        if initFunctionality == 0 :
            print("Exit")
        
        elif initFunctionality == 1 :
            manageFunction()

        elif initFunctionality == 2 :
            showRate()
            selectRate()

        elif initFunctionality == 3 :
            print("editing")

        else :
            initFunctionality = int(input(f"{30 * '-'}\nPlease select a valid option: "))

    initFunctionality = ()


'''while initFunctionality != 0 :
    showFunctions()'''

selectFunction()