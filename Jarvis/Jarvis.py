# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:53:38 2020

@author: KUNTAL
"""
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


#Speak Function for Jarvis:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Master Kuntal!")
        
    elif hour>=12 and hour<17:
        speak("Good Afternoon, Master Kuntal!")
        
    elif hour>=17 and hour<22:
        speak("Good Evening, Master Kuntal!")
    
    else:
        speak("Good Night, Master Kuntal! Have a nice sleep.")
        
    speak("I am Jarvis at your service, sir! Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from user & returns output as a String:
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        
        print("Say that again please..")
        speak("Please say that again, sir...")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kuntalzatchhindi@gmail.com', 'kuntal2014')
    server.sendmail('kuntalzatchhindi@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #takeCommand()
    if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searchiing Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opened Google for you.")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opened YouTube for you.")
        elif 'play music' in query:
            music_dir = 'D:\\INTEX\\Received'
            songs = os.listdir(music_dir)
           # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime} now.")
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "diveruzumaki@gmail.com"
                sendMail(to, content)
                speak("Mail has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry Kuntal, my bro, I could not connect to the mail.")
                
                
        elif 'open chrome' or 'open browser' in query:
            chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
            speak("Chrome opened for you, sir.")