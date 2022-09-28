from datetime import datetime
import smtplib
import webbrowser
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as pykit
import os
import random
import cv2
from requests import get
import time
import string
import pyjokes
from playsound import playsound
import pyautogui as dp
from Movie.main import recommend
import pandas as pd
from knock_jokes import knock_jokes

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("Koro sukee robot at your service sir")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=None,phrase_time_limit=None)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    with open('Password.txt') as f:
        password=f.read()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('subscriptionnetflix9@gmail.com',password)
    server.sendmail('subscriptionnetflix9@gmail.com',to,content)
    server.close()

def newEmail(user,password,to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(user,password)
    server.sendmail(user,to,content)
    server.close()

def weather_data(_query_):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+_query_+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
    return res.json

def print_weather(result,city):
    print("{}'s temperature: {}°C".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    speak("Wind speed: {} m/s".format(result['wind']['speed']))
    speak("Description: {}".format(result['weather'][0]['description']))
    speak("Weather: {}".format(result['weather'][0]['main']))

def check_birthday():
    file_name=open('Birthdays.txt')
    today=time.strftime('%m%d')
    count=0
    for line in file_name:
        if today in line:
            line=line.split(' ')
            count=1
            speak("Birthdays Today! "+line[1]+' '+line[2])
    if count==0:
        speak("No Birthdays Today")

def add_birthday():
    speak("Enter the birthday details in the shown format")
    print("MMDD Name Surname")
    file_name=open('Birthdays.txt','a+')
    birthday_details=input("Enter birthday details in the shown formay: ")
    file_name.write(str(birthday_details))
    file_name.close()

def random_password(password_length):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    possible_combinations=[]
    possible_combinations.extend[list(lower)]
    possible_combinations.extend[list(upper)]
    possible_combinations.extend[list(digits)]
    possible_combinations.extend[list(symbols)]
    random.shuffle(possible_combinations)
    speak("You can use the password: ")
    print("".join(possible_combinations[0:password_length]))

        
def take_screenshot(time_gap):
    time.sleep(time_gap)
    im1=dp.screenshot()
    speak("You need to rename it to save for a longer time")
    speak("Do you want to rename it?")
    answer=takeCommand().lower()
    if answer=='yes':
        speak("Please enter the new name of the file")
        name=input("Enter the new name of the file: ")
        if os.path.exists("D:\\Aqua\\Screenshot\\Screenshot.png"):
            os.rename("D:\\Aqua\\Screenshot\\Screenshot.png",f"D:\\Aqua\\Screenshot\\{name}.png")
        else:
            im1.save(r"D:\\Aqua\\Screenshot\\Screenshot.png")
            os.rename("D:\\Aqua\\Screenshot\\Screenshot.png",f"D:\\Aqua\\Screenshot\\{name}.png")
        speak("Screenshot saved successfully!")
    elif answer=='no':
        im1.save(r"D:\\Aqua\\Screenshot\\Screenshot.png")
        speak("Screenshot saved successfully!")
    else:
        speak("Invalid answer")

def takeCommand_short_notes(time_lapse):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=time_lapse)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        file_name=open('Notepad_Short.txt')
        file_name.write(f"{query}\n")
        speak("Text to speech successful!")
    except Exception as e:
        print("Say that again please...")
        return None
    return query

def recommend_aqua():
    speak("What do you want me to recommend")
    recommend_query=takeCommand().lower()
    movies=pd.read_csv('D:/Aqua/Movie/tmdb_5000_credits.csv')
    movie_name=movies['title']
    if 'movie' in recommend_query:
        try:
            movie_list=[]
            for i in range(5):
                random_movie=movie_name[random.randint(0,4802)]
                movie_list.append(random_movie)
        except:
            speak("Movie not in dataset")
        else:
            print(f"Based on these movies: {str(movie_list).lstrip('[').rstrip(']')} here are your recommendations")
            speak(f"Based on these movies: {str(movie_list).lstrip('[').rstrip(']')} here are your recommendations")
            for i in range(5):
                print(recommend(movie_list[i]))
                speak(recommend(movie_list[i]))
    elif 'song' in recommend_query:
        speak("Not ready yet") # Working on it

def main():
    wishMe()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentence=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'play song on youtube' in query:
            speak("Which song would you like to hear?")
            youtube_query=takeCommand().lower()
            pykit.playonyt(f"{youtube_query}")
        elif 'open google' in query:
            speak("What should I search on google?")
            google_query=takeCommand().lower()
            webbrowser.open(f"{google_query}")
        elif 'open website' in query:
            speak("Which website would you like to opne?")
            web_query=takeCommand().lower()
            webbrowser.open(f"{web_query}.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\HP\\Music'
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("Would you like to send email to one of your existing contacts?")
                answer=takeCommand().lower()
                if answer=='yes':
                    speak("Whom would you like to send email?")
                    person=takeCommand().lower()
                    infile=open("Email_reference.txt")
                    for line in infile:
                        if person in line:
                            to=next(infile)
                    infile.close()
                    speak("Do you want to write or speak the content of email?")
                    speak_write=takeCommand().lower()
                    if 'speak' in speak_write:
                        speak("What should I say?")
                        content=takeCommand()
                    elif 'write' in speak_write:
                        speak("Please input the contents below")
                        content=input("Content: ")
                    speak("Please enter the passcode")
                    passcode=input("Passcode: ")
                    if passcode=='anmol123':
                        sendEmail(to,content)
                        speak("Email has been sent!")
                    else:
                        speak("Wrong passcode")
                elif answer=='no':
                    speak("Enter the email address of the person you would like to send email")
                    to=input("Enter receiver's email address: ")
                    speak("Do you want to write or speak the content of email?")
                    speak_write=takeCommand().lower()
                    if 'speak' in query:
                        speak("What should I say?")
                        content=takeCommand()
                    elif 'write' in query:
                        speak("Please input the contents below")
                        content=input("Content: ")
                    speak("Please enter the passcode")
                    passcode=input("Passcode: ")
                    if passcode=='anmol123':
                        sendEmail(to,content)
                        speak("Email has been sent!")
                    else:
                        speak("Wrong passcode")
            except Exception as e:
                print(e)
                speak("Sorry Email not sent")
        elif 'new email' in query:
            try:
                speak("Please type in your email address")
                user=input("Email address: ")
                speak("Please type in your password")
                password=input("Password: ")
                speak("Enter the email address of the personyou would like to send email to")
                to=input("Enter reciever's email address: ")
                speak("Do you want to write or speak the content of email?")
                speak_write=takeCommand().lower()
                if 'speak' in query:
                    speak("What should I say?")
                    content=takeCommand()
                elif 'write' in query:
                    speak("Please input the contents below")
                    content=input("Content: ")
                newEmail(user,password,to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Email not sent")
        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            speak("Press escape key to close the webcam")
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
            print(f"Your ip address is {ip}")
        elif 'weather' in query:
            speak("Which place's weather condition you would like to know?")
            weather_city=takeCommand().lower()
            try:
                _query_='q='+weather_city
                w_data=weather_data(_query_)
                print_weather(w_data,weather_city)
            except:
                print("City name not found")
                speak("City name not found")
        elif 'check birthday' in query:
            check_birthday()
        elif 'add birthday' in query:
            add_birthday()
        elif 'suggest password' in query:
            speak("What should be the length of the password?")
            password_length=int(takeCommand())
            random_password(password_length)
        elif 'joke' in query:
            speak("What type of joke would you like to listen?")
            speak("Knock Knock joke? Or, Programmer joke")
            jokes_answer=takeCommand().lower()
            if jokes_answer=="programmer joke":
                joke=pyjokes.get_joke()
                speak(joke)
            elif jokes_answer=="knock knock":
                for r in range(1):
                    r=random.randint(1,100)
                knock_jokes(r)
            else:
                speak("Sorry I didn't get that")
        elif 'refresh computer' in query:
            dp.hotkey('win','d')
        elif 'screenshot' in query:
            speak("After how many seconds you want to take the screenshot?")
            time_gap=int(takeCommand())
            take_screenshot(time_gap)
        elif 'short notes' in query:
            speak("For how much seconds would you like to speak?")
            time_lapse=takeCommand()
            print(time_lapse)
            takeCommand_short_notes(int(time_lapse))
        elif 'recommend' in query:
            recommend_aqua()
        elif 'sleep' in query:
            speak("Thanks for using me")
            exit()

if __name__=="__main__":
    while True:
        main()