import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import smtplib
import pyjokes
import random
import json
import wolframalpha
import winshell
import time
from urllib.request import urlopen
import requests
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install pustil
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from DebisUI import Ui_DebisUI 
import sys
from sys import exit

# import required modules
from selenium import webdriver
from time import sleep

#voice configuration
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_MARK_11.0"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", en_voice_id)
engine.setProperty("rate",178)
engine.setProperty("volume",5)#volume range 0-1


#funtions for task performance
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current Time is")
    speak(Time)


def date():
    Date = datetime.date.today()
    speak("The current Date is")
    speak(Date)

def convoHey():
    speak("Hello there, what's up...?")

def convoHello():
    speak("Hi, need assistance...?")

def about():
    speak("")

def wishme():
    speak("Welcome to Koforidua Technical University")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour < 12):
        speak("Good morning...")
    elif(hour >= 12 and hour < 18):
        speak("Good afternoon...")
    elif(hour >= 18 and hour < 24):
        speak("Good evening...")
    else:
        speak("Good night...")
    speak("Debis at your service. How may i assist you")    

def aid():
    speak("I hope that was helpful, Do you want help with anything else?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("path to save image")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())

class MainThread(QThread):
    def __init__ (self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def take_command(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")

            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)

            try:
                print("Recognizing")

                Query = r.recognize_google(audio, language='en-in')
                print(Query)
            
            except Exception as e:
                print(e)
                print("Say that again Please")
                return 'None'
            return Query

        speak(pyjokes.get_joke())



#if __name__ == "__main__":
    def TaskExecution(self):

        wishme()
        while True:
            self.Query = self.take_command().lower()
            if "hey" in self.Query or "Hey" in self.Query:
                convoHey()
            elif "hello" in self.Query or "Hello" in self.Query:
                convoHello()         
            elif "tell me about yourself" in self.Query:
                about()
            elif "time" in self.Query:
                time_()
            elif "date" in self.Query:
                date()
            elif "wikipedia" in self.Query:
                speak("Searching...")
                self.Query = self.Query.replace("wikipedia","")
                result = wikipedia.summary(self.Query, sentences=2)
                print(result)
                speak(result)
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()
            elif 'open youtube' in self.Query:
                speak("What should I search?")
                Search_term = self.take_command().lower()
                speak("Here we go to Youtube\n")
                wb.open("https://www.youtube.com/results?search_query="+Search_term)
                time.sleep(5)
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()
            elif 'search google' in self.Query:
                speak("What should I search?")
                Search_term = self.take_command().lower()
                wb.open('https://www.google.com/search?q='+Search_term)
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'search' in self.Query: 
                self.Query = self.Query.replace("self.Query","")
                wb.open(self.Query)
                sleep(5)
                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif "who am i" in self.Query:
                speak("If you can talk, then definitely you are a human")
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'send email' in self.Query:
                try:
                    speak("What should I say?")
                    content = self.take_command()
                    speak("Who is the Reciever?")
                    reciept = input("Enter recieptant's name: ")
                    to = (reciept)
                    sendEmail(to,content)
                    speak(content)
                    speak("Email has been sent.")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email.")
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'open chrome' in self.Query:
                speak("What website do you want to visit ?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = self.take_command().lower()
                wb.get(chromepath).open_new_tab(search+'.com')
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'log out' in self.Query:
                os.system("shutdown -l")
            elif 'restart' in self.Query:
                os.system("shutdown /r /t 1")
            elif 'shutdown' in self.Query:
                os.system("shutdown /s /t 1")

            elif 'remember that' in self.Query:
                speak("What should I remember ?")
                memory = self.take_command()
                speak("You asked me to remember that"+memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'do you remember' in self.Query:
                remember =open('memory.txt', 'r')
                speak("You asked me to remeber that"+remember.read())
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()            
            
            elif "write a note" in self.Query:
                speak("What should i write, sir")
                note = self.take_command()
                file = open('note.txt', 'w')
                speak("Sir, Should i include date and time")
                dt = self.take_command()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak('done')
                else:
                    file.write(note)
                    
            elif "show note" in self.Query:
                speak("Showing Notes")
                file = open("note.txt", "r")
                print(file.read())
                speak(file.read()) 
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif "weather" in self.Query:
                wb.open("https://weather.com/weather/today/l/6.06,-0.26?par=google")              
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif 'news' in self.Query:
                wb.open("https://www.ktu.edu.gh/category/news-announcements/")
                sleep(5)

                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()                
            
            elif 'take screenshot' in self.Query:
                screenshot()
                speak("Done!")    
            elif 'cpu' in self.Query:
                cpu()
            elif 'joke' in self.Query:
                jokes()
                sleep(5)
                
                aid()
                answer = self.take_command()
                if "yes" in answer or "sure" in answer:
                    speak("Alright, what else can I assist you with?")
                else:
                    speak("thank you for using Debis, Enjoy your stay on campus")
                    sleep(10)
                    quit()

            elif "where is" in self.Query:
                self.Query = self.Query.replace("where is","".lower())
                location = self.Query
                speak("Location to")
                speak(location)

                    # search locations
                def searchplace():
                    Place = driver.find_element_by_class_name("tactile-searchbox-input")
                    Place.send_keys("Koforidua Technical University")
                    Submit = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
                    Submit.click()

                    # get directions
                def directions():
                    sleep(15)
                    directions = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button")
                    directions.click()

                def satelite():
                    #satelite
                    sleep(7)
                    view = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[22]/div[5]/div/div[2]/button")
                    view.click()

                def zoom():

                    #zoom
                    sleep (2)
                    enlarge = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[22]/div[1]/div[2]/div[6]/div/div[1]/button")
                    enlarge.click()
                    sleep(1)
                 
                            
                        
                if  "central classroom" in self.Query or "ccb" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Central Classroom Block(CCB)")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    zoom()
                    sleep(5)
                    
                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit() 

                                
                if  "hospitality kitchen" in self.Query or "Hospitality Kitchen" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Hospitality Kitchen, 3P8P+3F4, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "basketball" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Basket Ball Court, 3P8P+567, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "built and natural" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.065178, -0.265958")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "ADB" in self.Query or "adb" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("ADB - KOFORIDUA POLYTECHNIC ATM")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "engineering" in self.Query or "FOE" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Faculty Of Engineering. (ktu)")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "societe" in self.Query or "sgb" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Societe Generale Ghana-KTU CAMPUS")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "old" in self.Query or "ad block" in self.Query or "old administration" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("AD Block (Old Administratiion Block), 3P7P+Q2C, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "radio" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("KTU Radio 87.7Mhz, 3P7P+P39, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "computer science" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.064832, -0.264537")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "administration" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.063759732231506, -0.2631470942182951")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()
                    

                if  "get fund" in self.Query or "getfund" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("GET Fund Hostel, 3P6M+QVM, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()                                                                                                                                                                                                   

                if  "applied science" in self.Query or "Applied Science" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("Applied Science (AS), Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite() 
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "business management" in self.Query or "fbms" in self.Query or "Fbms" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.065121, -0.264090")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite() 
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()              

                if  "football" in self.Query or "park" in self.Query or "field" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.061624, -0.263359")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "tennis" in self.Query or "tennis court" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.060979, -0.264105")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "ceremonial" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.064836, -0.264609")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()


                if  "clinic" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("KOFORIDUA TECHNICAL UNIVERSITY CLINIC, 3P7M+RXJ, Koforidua")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()


                if  "ad library" in self.Query or "Ed library" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.064499, -0.265111")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()

                if  "electronic library" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    searchplace()
                    directions()
                    
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.064870, -0.263558")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    
                    satelite()
                    zoom()
                    zoom()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()


                if  "thin client" in self.Query:
                        
                    # assign url in the webdriver object
                    driver = webdriver.Chrome('chromedriver')
                    driver.maximize_window()
                    driver.get("https://www.google.com.gh/maps/@5.636096,-0.196608,12z")
                    sleep(2)
                
                    satelite()
                    searchplace()
                    directions()
                                        
                    # find place            
                    sleep(6)
                    find = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                    find.send_keys("6.064417, -0.264780")
                    sleep(2)
                    search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                    search.click()
                    zoom()
                    sleep(5)

                    aid()
                    answer = self.take_command()
                    if "yes" in answer or "sure" in answer:
                        speak("Alright, what else can I assist you with?")
                    else:
                        speak("thank you for using Debis, Enjoy your stay on campus")
                        sleep(10)
                        quit()
                

            elif "offline" in self.Query:
                quit()
            else:
                speak("the command you gave is not recognized")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DebisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("giffyvoiceassis.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        #self.ui.movie = QtGui.QMovie("giffyvoiceassis.gif")
        #self.ui.label_2.setMovie(self.ui.movie)
        #self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
Debis = Main()
Debis.show()
exit(app.exec_())