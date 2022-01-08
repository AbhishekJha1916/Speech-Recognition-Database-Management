def query(voicenote):
    global mycursor, tablename1, tablename2# OUR MADE KEYWORDS

    #To see all table details
    if (voicenote.find("show") != -1) and (voicenote.find("all") != -1) and (voicenote.find("details") != -1) or (voicenote.find("Meri") != -1) and (voicenote.find("sari") != -1):
        from main import tablename1,tablename2, mycursor
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1   #Displaying Table 1 details
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
        
        print("\n",tablename2,"\n")
        cmd = "SELECT * FROM " + tablename2   #Displaying Table 2 details
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    
    #To see all table details in alphabetical order
    elif (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by name") != -1):
        from main import tablename1, mycursor, t1c2
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1 + " ORDER BY "+t1c2
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)

    #To see all table details in ascending orderby Salary
    elif (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by salary") != -1):
        from main import tablename1, mycursor, t1c3
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1 + " ORDER BY "+t1c3
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)

    # To see only Names
    elif (voicenote.find("show only") != -1) and (voicenote.find("names") != -1):
        from main import tablename1, mycursor,t1c2
        cmd = "SELECT " + t1c2 + " FROM " + tablename1
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    elif (voicenote.find("show ") != -1) and (voicenote.find("all names") != -1):
        from main import tablename1, mycursor,t1c2
        cmd = "SELECT " + t1c2 + " FROM " + tablename1
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)

    #To see only Names and Salaries
    elif (voicenote.find("show only name and salaries") != -1) or (voicenote.find("Display only name and salaries") != -1) or (voicenote.find("show all name and salaries")!= -1): 
        from main import tablename1, mycursor,t1c2 ,t1c3
        cmd = "SELECT " + t1c2 +","+" " + t1c3 + " FROM "+ tablename1
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)

    #To show details from two different tables
    elif (voicenote.find("show name and phone number") != -1) or (voicenote.find("display name and phone number") != -1):
        from main import tablename1,tablename2, mycursor,t1c2 ,t2c2, t1c1, t2c1, t2c2
        cmd = "SELECT "+tablename1+"."+t1c2+","+tablename2+"."+t2c2+" FROM " +tablename1+ " INNER JOIN " + tablename2 + " ON " +tablename1+"."+t1c1+" = " +tablename2+ "." + t2c1
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)

