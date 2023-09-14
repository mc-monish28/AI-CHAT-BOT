import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import requests
import cv2 
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np 

listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_maxi():
    command = input("Enter text:")
    print(command)
    if 'sing' in command:
        song = command.replace('play','')
        talk('ok playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is: '+time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'date ku polama' in command:
        talk('sorry I have headache')
   
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play a movie' in command:
        talk("opening a movie")
        os.startfile("D:\Movies\Engaeyum Eppothum [2011] Tamil 720p DVDRIp 1.3GB.mp4")
    elif 'open eye control mode' in command:
        talk("open eye control mode")
        os.startfile("D:\Movies\chat bot project\main.py")
    elif 'open funny program' in command:
        talk("adjust volume ")
        os.startfile("D:\Movies\chat bot project\Volumn_fun.py")
    elif 'record a screen' in command:
        talk("Screen has been recording")
        os.startfile("D:\Movies\chat bot project\screen recorder.py")
    
    elif 'given details of a phone number' in command:
        talk("enter a phone number")
        os.startfile("D:\Movies\chat bot project\phone_numbers_tracker.py")
    elif 'turn on the light' in command:
        talk("turning on the light")
        val = requests.get("http://192.168.76.36/5/on")
        print(val.status_code)         
    elif 'turn off the light' in command:
        talk("turning off the light")
        val = requests.get("http://192.168.76.36/5/off")
        print(val.status_code)
    elif 'turn on the fan' in command:
        talk("turning on the fan")
        val = requests.get("http://192.168.76.36/4/on")
        print(val.status_code)
        
    elif 'turn off the fan' in command:
        talk("turning off the fan")
        val = requests.get("http://192.168.76.36/4/off")
        print(val.status_code)
    elif 'Message to srinath' in command:
        talk("Ok, Message sent to  srinath ")
        os.startfile("D:\Movies\chat bot project\whatsapp.py")
    
    
    else:
        talk("maxi can't listen, say it again")

while True:
    run_maxi()
