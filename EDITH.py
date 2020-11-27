#imports
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

#audios
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0],id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wishme
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Edith. what can i do for you?")

#speech recognition
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #  print(e)

        print("say that again please...")
        return "none"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        
#wikipedia   
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

#commands
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'launch code' in query:
            codepath = "C:\\Users\\varun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("launching code")

        elif 'launch after effects' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe After Effects CC 2019\\Support Files\\AfterFX.exe"
            os.startfile(codepath)
            speak("launching after effects") 

        elif 'launch illustrator' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2020\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(codepath)
            speak("launching illustrator")

        elif 'launch photoshop' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codepath)
            speak("launching photoshop")

        elif 'launch premiere pro' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2019\\Adobe Premiere Pro.exe"
            os.startfile(codepath)
            speak("launching premiere pro")

        elif 'launch epic games' in query:
            codepath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codepath)
            speak("launching epic games")

        elif 'launch excel' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codepath)
            speak("leanching excel")

        elif 'launch word' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codepath)
            speak("launching word")

        elif 'launch chrome' in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)
            speak("launching chrome")

        elif 'launch torrent' in query:
            codepath = "C:\\Users\\varun\\AppData\\Roaming\\BitTorrent\\BitTorrent.exe"
            os.startfile(codepath)
            speak("launching torrent")

        elif 'launch windscribe' in query:
            codepath = "C:\\Program Files (x86)\\Windscribe\\WindscribeLauncher.exe"
            os.startfile(codepath)
            speak("launching windscribe")

        elif 'launch popcorn time' in query:
            codepath = "C:\\Users\\varun\\AppData\\Local\\Popcorn-Time\\Popcorn-Time.exe"
            os.startfile(codepath)
            speak("launching popcorn time")