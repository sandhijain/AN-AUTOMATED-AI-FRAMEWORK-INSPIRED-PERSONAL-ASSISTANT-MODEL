# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:44:06 2021

@author: Sandhi 
"""
import pyttsx3 #pip install pyttsx3 
import speech_recognition as sr #pip install speechRecognition
import datetime #installed in python by default
import wikipedia #pip install wikipedia
import webbrowser #installed in python by default
import os
import smtplib
import time
import pywhatkit 
import pyjokes
import PyPDF2
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mam!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mam!")   

    else:
        speak("Good Evening Mam!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print("Say that again please...")  
        #speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            time.sleep(5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            time.sleep(5)
            speak("I have opened youtube for you")
            
        elif 'find' in query: 
            query = query.replace("find","")
            speak("Searching on google..") 
            pywhatkit.search(query)
            time.sleep(5)
             
         
        elif 'date' in query:
           strYear = datetime.datetime.now().strftime("%d%B%A")
           speak(f" Today is {strYear}")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f" Well,the time is {strTime}")

        elif 'open code' in query:
            codePath = " "
            os.startfile(codePath)
            
        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail has opened")
            time.sleep(5)
        
        elif 'open my website' in query:
            webbrowser.open_new_tab("https://utmselfhelp.wordpress.com/")
            speak("I have opened your website") 
            time.sleep(5)
        
        elif 'play' in query:
            query = query.replace('play','')
            speak('Playing'+ query)
            pywhatkit.playonyt(query)
            
        elif 'ask' in query:
         speak('I can answer to computational and geographical questions  and what question do you want to ask now')
         question=takeCommand()
         app_id="4JTPV8-5G6XU5APPT"
         client = wolframalpha.Client('4JTPV8-5G6XU5APPT')
         res = client.query(question)
         answer = next(res.results).text
         speak(answer)
         print(answer)   
        
        
        elif 'message'in query:
          speak("Tell me the mobile number")
          mobile = takeCommand()
          speak("Noted the mobile Number")
          message = takeCommand()
          pywhatkit.sendwhatmsg_instantly("+91 mobile","message")
          pywhatkit.sendwhatmsg_to_group( 'https://chat.whatsapp.com/J6YQLqMXezn7NG61roCE0r','This is a test message of desktop ai assistant', time_hour, time_min)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'open book' in query:
             pdfReader = PyPDF2.PdfFileReader(open('Alice_in_Wonderland.pdf', 'rb'))
             for page in range(pdfReader.numPages ):
              text = pdfReader.getPage(page).extractText() 
              engine.say(text)
              engine.runAndWait()
              engine.stop()
                
    
        elif 'email' in query:
            query = query.replace('email',"")
            pywhatkit.send_mail('shachi2024ds@gmail.com', 'shachiwriter1324ds','Default', query,'sandhijain24.tundla@gmail.com')

           
        elif'goodbye' in query or 'ok bye' in query or 'stop'in query:
            speak('JARVIS is shutting down, have a nice day')
            print('JARVIS is shutting down, have a nice day')
            break
