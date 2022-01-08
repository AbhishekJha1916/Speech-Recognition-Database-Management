import speech_recognition as SR   #import prebuilt library Speech Recognition
import mysql.connector as mc      #import prebuilt library MySQL connector
import MySQLvoice                 #import our library MySQLvoice

mydb=mc.connect(
    host = "localhost",      #your Host name
    user = "root",           #Your root name
    password = "****",       #Write your database password
    database = "DotSlash5")  #Mention the database you want to work on

#Initialising cursor
mycursor = mydb.cursor()     

tablename1 = "voidion"       #First Table Name 
t1c1="RegNo"                 #Table 1 Column 1 name
t1c2="Name"                  #Table 1 Column 2 name
t1c3="Salary"                #Table 1 Column 3 name

tablename2 = "contacts"      #Seconnd Table Name 
t2c1="RegNo"                 #Table 2 Column 1 name
t2c2="Phone"                 #Table 2 Column 2 name

#Recognising function stored in r variable
r = SR.Recognizer() 

#Using system microphone for Input audio
with SR.Microphone() as source:
    
    #Adjusting energy threshold value
    r.adjust_for_ambient_noise(source) 
    
    #Listening and storing voice input
    print("Listening...")
    audio = r.listen(source)
    
    #Recognizing audio speech based on internet speed and storing it in voicenote variable
    print("Recognizing...")
    voicenote = r.recognize_google(audio) 

# Printing the input
print("User Said : ", voicenote)

#Passing voicenote in mySQLvoice Library
print (MySQLvoice.query(voicenote) )  
