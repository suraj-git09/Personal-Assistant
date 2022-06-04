
import pyttsx3
import webbrowser
import random
import smtplib
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
import emoji
from geopy.geocoders import Nominatim


def music_on_loop(file,):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('YourApp_Id')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print('Luis: ', end="")
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def speakonly(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak(emoji.emojize('Good Morning! :slightly_smiling_face:'))

    if currentH >= 12 and currentH < 18:
        speak(emoji.emojize('Good Afternoon! :slightly_smiling_face:'))

    if currentH >= 18 and currentH != 0:
        speak(emoji.emojize('Good Evening! :slightly_smiling_face:'))


greetMe()

speak('I am Luis! your digital voice Assistant!')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(emoji.emojize("Listening... :thinking_face:"))
        r.pause_threshold = 1
        r.energy_threshold = 1200
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('You: ' + query + '\n')

    except sr.UnknownValueError:
        speak(emoji.emojize(
            'Sorry! I didn\'t get that!:pensive_face: Try typing the command!'))
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speakonly('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speakonly('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speakonly('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query or 'how you doing' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!',
                      'Nice!', 'I am good and full of energy']
            speak(random.choice(stMsgs))
            print(emoji.emojize(":smiling_face_with_smiling_eyes:"))
        elif "i love you" in query or 'love you' in query:
            msg =['I can\'t feel romantic,but i think you are wonderful.',
                   'I love you too!', 'Its nice to hear that!']
            print(emoji.emojize(":smiling_face_with_heart-eyes:"))
            speak(random.choice(msg))

        elif 'kiss' in query:
            print(emoji.emojize(":face_blowing_a_kiss:"))
            music_on_loop('kiss.wav')
            time.sleep(1.2)

        elif 'propose' in query or 'romantic' in query:
            speakonly("I hope this song will help you")
            time.sleep(0.5)
            music_on_loop("PUBLIC.wav")

        elif 'weather' in query:
            loc = Nominatim(user_agent="GetLoc")
            speak("Where Are you?")
            locatn = myCommand()
            getLoc = loc.geocode(locatn)
            print(getLoc.address)

            # Enter your API key here
            api_key = "Api_Key"

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"


            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + locatn

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()

            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":
                try:

                    # store the value of "main"
                    # key in variable y
                    y = x["main"]

                    # store the value corresponding
                    # to the "temp" key of y
                    current_temperature = y["temp"]
                    celc=int(current_temperature-273.15)

                    # store the value corresponding
                    # to the "pressure" key of y
                    current_pressure = y["pressure"]

                    # store the value corresponding
                    # to the "humidity" key of y
                    current_humidity = y["humidity"]

                    # store the value of "weather"
                    # key in variable z
                    z = x["weather"]

                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]

                    speakonly("Its "+str(celc)+" Deegrees "+str(weather_description))
                    # print following values
                    print(" Temperature (in degrees) = " +
                        str(celc) +
                        "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
                        "\n humidity (in percentage) = " +
                        str(current_humidity) +
                        "\n description = " +
                        str(weather_description))
                except:
                    print(" City Not Found ")

                
        elif 'time' in query:
            current_time= datetime.datetime.now()
            speak(current_time.strftime('Its %H:%M'))
            


        elif 'date' in query:
            current_date= datetime.datetime.now()
            speak(current_date.strftime('Its %A,%dth %B-%Y'))

        elif 'email' in query or 'mail' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient or 'self' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("User_Id", 'Password')
                    server.sendmail('User_Id',"Recipient_Id",content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry! I am unable to send your message at this moment!')
        elif 'spotify' in query or 'play music' in query or 'song' in query:
            webbrowser.open("C:/Users/rajsu/OneDrive/Desktop/Spotify.lnk")
            speak("There you go")
            time.sleep(3)
            py.click(957, 949, clicks=1)
            break

        elif 'news' in query:
            url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=Api_key'
            data = requests.get(url).text
            lodedFile = json.loads(data)
            speak('News for today')
            articles = lodedFile["articles"]
            for art in articles:
                speak(art['title'])

                speak(art["description"])
                print(art['url'])
                speak('Now..... the next news')

        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'no' in query:
            speak('okay')
            speak(emoji.emojize('Bye, have a good day!:slightly_smiling_face:'))
            sys.exit()

        elif 'hello' in query:
            speak(emoji.emojize('Hello Buddy! :slightly_smiling_face:'))

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('https://www.google.co.in/')

        speak('Anything else Buddy?')
