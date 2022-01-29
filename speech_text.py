import speech_recognition as sr

# r will be used as a recognizer for forward referencing
r = sr.Recognizer()

# Now we provide a audio for converting to text
with sr.AudioFile("Hello.wav") as source:
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Audio to text")
        print(text)

    except:
        print("Sorry,Unable to recognise")
