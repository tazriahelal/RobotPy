import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
import bs4
import requests
from bs4 import BeautifulSoup
Assistant = pyttsx3.init('sapi5')
voices= Assistant.getProperty('voices')
#print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    print("  ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognizing........")
            query = command.recognize_google(audio,language='én-US')
            print(f"You Said: {query}")
        except Exception as Error:
            return "none"
        return query.lower()

def TaskExe():
    def Music():
        Speak("Tell me the name of the song")
        musicName = takecommand()
        if 'ABC' in musicName:
            os.startfile('E:\\ABC.mp3')
        else:
            pywhatkit.playonyt(musicName)
        Speak("Enjoy Sir.")
    def Whatsapp():
        Speak("Tell me The Name Of The Person!")
        name = takecommand()

        if 'karan' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("Time in Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+8801647666942",msg,hour,min,20)
            Speak("Ok sir, Sending Whatsapp Message!")
        elif 'ria' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("Time in Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+8801552925142", msg, hour, min, 20)
            Speak("Ok sir, Sending Whatsapp Message!")
        else:
            Speak("Tell me the number=")
            phone= int(takecommand())
            ph = '+88'+phone
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("Time in Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
            Speak("Ok sir, Sending Whatsapp Message!")
    def OpenApps():
        Speak("OK Sir, wait a second")
        if 'pycharm' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains")
        elif 'word' in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/?hl=en")
        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps/@23.7748025,90.3487934,15z")
        elif 'download' in query:
            os.startfile("E:\\Downloads")
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        Speak("Open Successfully!")
    def CloseApps():
        Speak("Ok SIr, wait a second!")
        if 'youtube' in query:
            os.system("taskkill /im chrome.exe /f")
        if 'instagram' in query:
            os.system("taskkill /im chrome.exe /f")
        if 'pycharm' in query:
            os.system("taskkill /im pycharm.exe /f")
        if 'word' in query:
            os.system("taskkill /im word.exe /f")
        if 'maps' in query:
            os.system("taskkill /im chrome.exe /f")
        if 'chrome' in query:
            os.system("taskkill /im chrome.exe /f")
    def YoutubeAuto():
        Speak("What Your Command?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('1')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        elif 'miniplayer' in comm:
            keyboard.press('i')
        Speak("Done Sir")
    def ChromeAuto():
        Speak("Chrome Automation Started")
    def CoronaVirus(Country):

        countries = str(Country).replace(" ", "")

        url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

        result = requests.get(url)

        soups = bs4.BeautifulSoup(result.text, 'lxml')

        corona = soups.find_all('div', class_='maincounter-number')

        Data = []

        for case in corona:
            span = case.find('span')

            Data.append(span.string)

        cases, Death, recovored = Data

        Speak(f"Cases : {cases}")
        Speak(f"Deaths : {Death}")
        Speak(f"Recovered : {recovored}")



    while True:
        query = takecommand()
        if 'hello' in query:
            Speak("Hello Sir, I am Taz.")
        elif 'how are you' in query:
            Speak('I am fine.How may I Help you?')
        elif 'you need a break' in query:
            Speak('Ok sir, you can call me!')
            break
        elif 'youtube search' in query:
            Speak("Ok Sir.")
            query = query.replace("Taz", "")
            query= query.replace("youtube serach","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir")
        elif 'google search' in query:
            Speak("This is what I found for your search Sir-")
            query= query.replace("Taz","")
            query= query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir")
        elif 'website' in query:
            Speak("Ok Sir, Launching.....")
            query= query.replace("Taz","")
            query= query.replace("website","")
            query=query.replace(" ","")
            web1= query.replace("open","")
            web2='https://www.' + web1 +'.com'
            webbrowser.open(web2)
            Speak("Launched!")
        elif 'launch' in query:
            Speak("Tell Me The Name of The Website ")
            name = takecommand()
            web = 'https://www.' + web1 + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'music' in query:
            Music()
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia....")
            query = query.replace("Taz","")
            query = query.replace("wikipedia","")
            wiki= wikipedia.summary(query,2)
            Speak(f"According to Wikipedia: {wiki}")

        elif 'message' in query:
             from game import msg
             msg()

        elif 'screenshot' in query:
            Speak("Ok SIr")
            path=takecommand()
            path1name= path + ".png"
            path1 = "E:\\Downloads\\"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("E:\\Downloads\\")
            Speak("Here is your screeshot")
        elif 'open facebook' in query:
            OpenApps()
        elif 'open instagram' in query:
            OpenApps()
        elif 'open maps' in query:
            OpenApps()
        elif 'open youtube' in query:
            OpenApps()
        elif 'open word' in query:
            OpenApps()
        elif 'open google chrome' in query:
             OpenApps()
        elif 'open download' in query:
            OpenApps()
        elif  'open pycharm' in query:
            OpenApps()
        elif 'close chrome' in query:
            CloseApps()
        elif 'close youtube' in query:
            CloseApps()
        elif 'close google maps' in query:
            CloseApps()
        elif 'close facebook' in query:
            CloseApps()
        elif 'close word' in query:
            CloseApps()
        elif 'close instagram' in query:
            CloseApps()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('1')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'miniplayer' in query:
            keyboard.press('i')


        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj= takecommand()
            Speak(f"You said: {jj}")
        elif 'corona' in query:
            kk=CoronaVirus("bangladesh")
            print(kk)
        elif 'calender' in query:
            from game import showCalender

            Speak("Okay sir")
        elif 'alarm' in query:
            from MyAlarm import alarm

        else:
            from ChatBot import ChatterBot
            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

TaskExe()