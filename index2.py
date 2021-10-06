
# PYTHON VOICE ASISTANCE

import subprocess
import wolframalpha
import pyttsx3
import tkinter
from playsound import playsound
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from tkinter import *

from twilio.rest import Client
from clint.textui import progress

# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wish Method
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18 :
        speak("Good AfterNoon")
    else:
        speak("Good Evening")

#Taking Input
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        speak("Unable to Recognize your voice.")
        return "None"
     
    return query

#Main Method
if __name__ == '__main__':
    WishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open Wikipedia' in query:
            speak("Opening Wikipedia")
            webbrowser.open("Wikipedia.com")

        elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                music_dir ="A:\Music"
                songs = os.listdir(music_dir)
                print(songs)   
                random=os.startfile(os.path.join(music_dir, songs[1]))
                playsound(random)

        elif 'the time' in query or 'whats time' in query or 'tell me the time' in query or 'What time is it' in query:
            strTime = "The time is "+datetime.datetime.now()
            print(strTime)
            speak(strTime)

        

        
     
