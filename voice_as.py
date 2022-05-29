
from asyncio.windows_events import NULL
from logging import exception
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import sys
import pyautogui as py
import time
import json
import requests
from pygame import mixer


def music_on_loop(file,):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
 

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('Computer: ',end="")
    print(audio)
    engine.say(audio)
    engine.runAndWait()

    
    
    
        
    

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello !')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.energy_threshold=1500
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif "i love you" in query or 'love you' in query:
            msg=['I cant feel romantic,but i think you are wonderful','I love you too','its nice to hear that']
            speak(random.choice(msg))

        elif 'kiss' in  query:
            music_on_loop('kiss.wav')
            time.sleep(1.2)
            pass
            

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
        

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
        elif 'spotify'  in query or 'play music' in  query or 'song' in query:
            webbrowser.open("C:/Users/rajsu/OneDrive/Desktop/Spotify.lnk")
            time.sleep(3)
            py.click(957,949,clicks=1)

        elif 'news' in query:
            url='http://newsapi.org/v2/top-headlines?country=in&apiKey=9f3055c70100489ba9a795eb7944fc08'
            data=requests.get(url).text
            lodedFile=json.loads(data)
            speak('News for today')
            articles=lodedFile["articles"]
            for art in articles:
                speak(art['title'])
               
                speak(art["description"])
                print(art['url'])
                speak('Now..... the next news')


            

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        # elif 'play music' in query:
        #     music_folder = 'E:\MUSIC'
        #     music = ["E:\MUSIC\KGF 2 Theme Remake.mp3"]
        #     random_music = music_folder + random.choice(music) + '.mp3'
        #     os.system(random_music)
                  
        #     speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        
