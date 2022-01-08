import speech_recognition as SR
r = SR.Recognizer()
with SR.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source)
    print("Recognizing...")
    voicenote = r.recognize_google(audio)
print("User Said : ", voicenote)
