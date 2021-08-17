import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good morning Martin")
    elif 12 < hour < 18:
        speak("Good afternoon Martin")
    else:
        speak("Good Evening martin")
    speak("How can i help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        speak("you didn't respond")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Accordint to wikipedia")
            print(result)
            speak(result)

        elif "google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "music" in query:
            my_dir = "d:\\mymusic\\"
            start = os.listdir(my_dir)
            play = os.path.join(my_dir, start[0])
            os.startfile(play)

        elif "code" in query:
            code = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif "who made you" in query:
            speak("Mr.sandeep yadav my owner")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif "vlc" in query:
            path = "C:\\Program Files\\VideoLAN\\VLC\\uninstall.exe"
            os.startfile(path)

        elif "exit" in query:
            speak("Thank you sir for using me")
            exit(1)
