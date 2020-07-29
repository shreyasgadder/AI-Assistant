import pyttsx3 #pip3 install pyttsx3 && espeak && alsa-utils
import datetime
import speech_recognition as sr #pip3 install SpeechRecognition && PyAudio
import wikipedia #pip3 install wikipedia
import smtplib
import webbrowser as wb 
import os
import subprocess, sys #linux os only
import pyautogui #pip3 install pyautogui && sudo apt-get install scrot
import psutil #pip3 install psutil
import pyjokes #pip3 install pyjokes

engine = pyttsx3.init()
engine.setProperty('rate', 150)
'''voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir!")
    elif hour >=18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("good night sir!")
    speak("Welcome back")
    speak("jarvis at your service. how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('automadhacker@gmail.com', 'emperors99')
    server.sendmail('automadhacker@gmail.com',to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('/home/eagle/Courses/Jarvis/ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("The battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_jokes())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "automadhacker@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in browser' in query:
            speak("What should i search?")
            browsepath = "/usr/bin/firefox-esr %s"
            search = takeCommand().lower()
            wb.get(browsepath).open_new_tab(search + '.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown -h now")

        elif 'restart' in query:
            os.system("shutdown -r")

        elif 'play songs' in query:
            songs_dir = "/home/eagle/Music"
            songs = os.listdir(songs_dir)
            #os.startfile(os.path.join(songs_dir, songs[0]))
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, os.path.join(songs_dir, songs[0])])

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember " + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said to remember that" +remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done...")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Going Offline...")
            quit()
