#imports
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests

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
        print("user said: [query]")

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
            speak("the time is [strTime]")

        elif 'open code' in query:
            codepath = "C:\\Users\\varun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("opening code")

        elif 'open after effects' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe After Effects CC 2019\\Support Files\\AfterFX.exe"
            os.startfile(codepath)
            speak("opening after effects") 

        elif 'open illustrator' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2020\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(codepath)
            speak("opening illustrator")

        elif 'open photoshop' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codepath)
            speak("opening photoshop")

        elif 'open premiere pro' in query:
            codepath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2019\\Adobe Premiere Pro.exe"
            os.startfile(codepath)
            speak("opening premiere pro")

        elif 'open epic games' in query:
            codepath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codepath)
            speak("opening epic games")

        elif 'open excel' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codepath)
            speak("opening excel")

        elif 'open word' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codepath)
            speak("opening word")

        elif 'open chrome' in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)
            speak("opening chrome")

        elif 'open torrent' in query:
            codepath = "C:\\Users\\varun\\AppData\\Roaming\\BitTorrent\\BitTorrent.exe"
            os.startfile(codepath)
            speak("opening torrent")

        elif 'open windscribe' in query:
            codepath = "C:\\Program Files (x86)\\Windscribe\\WindscribeLauncher.exe"
            os.startfile(codepath)
            speak("opening windscribe")

        elif 'open popcorn time' in query:
            codepath = "C:\\Program Files (x86)\\Popcorn Time\\PopcornTimeDesktop.exe"
            os.startfile(codepath)
            speak("opening popcorn time") 

        elif 'open obs' in query:
            codepath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(codepath)
            speak("opening obs")

        elif 'open steam' in query:
            codepath = "C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(codepath)
            speak("opening steam")

        elif 'open battle' in query:
            codepath = "C:\\Program Files (x86)\\Battle.net\\Battle.net Launcher.exe"
            os.startfile(codepath)
            speak("opening battle")

        elif 'open origin' in query:
            codepath = "C:\\Program Files (x86)\\Origin\\Origin.exe"
            os.startfile(codepath)
            speak("opening origin")

        elif 'open valorant' in query:
            codepath = "E:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(codepath)
            speak("opening valorant")         

        elif 'open rockstar games' in query:
            codepath = "C:\\Program Files\\Rockstar Games\\Launcher\\LauncherPatcher.exe"
            os.startfile(codepath)
            speak("opening rockstar games")