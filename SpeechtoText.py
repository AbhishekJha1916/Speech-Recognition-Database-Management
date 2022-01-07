import speech_recognition as SR
r = SR.Recognizer()
with SR.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audi=r.listen(source)
print("Recognizing...")
print("User Said : " + r.recognize_google(audi))
