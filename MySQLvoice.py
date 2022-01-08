def query(voicenote):
    global mycursor, tablename1, tablename2 # Keywords made by us

    # To see all table details
    if (voicenote.find("show") != -1) and (voicenote.find("all") != -1) and (voicenote.find("details") != -1) or (voicenote.find("Meri") != -1) and (voicenote.find("sari") != -1):
        from main import tablename1,tablename2, mycursor
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1   # Displaying Table 1 details
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
        
        print("\n",tablename2,"\n")
        cmd = "SELECT * FROM " + tablename2   # Displaying Table 2 details
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
    
    # To see all table details in alphabetical order
    if (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by name") != -1):
        from main import tablename1, mycursor, t1c2
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1 + " ORDER BY "+t1c2
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
            
    # To see all table details in ascending orderby Salary
    if (voicenote.find("show") != -1) and (voicenote.find("details") != -1) and (voicenote.find("order by salary") != -1):
        from main import tablename1, mycursor, t1c3
        print("\n",tablename1,"\n")
        cmd = "SELECT * FROM " + tablename1 + " ORDER BY "+t1c3
        mycursor.execute(cmd)
        for i in mycursor:
            print(i)
