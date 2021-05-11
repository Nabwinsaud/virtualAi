import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def Alaram():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning br.....')
    elif hour>=12 and hour<18:
        speak('Good afternoon....')    
    else:
        speak('Good night!')

def Command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening .......')
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print('Recongnizing......')
        query=r.recognize_google(audio,language='en-uk')
        print(f'You said {query} ' )

    except Exception as e:
        print('please say again...')
        return "None"  
    return query      
    





# speak('i am jarvis your virtual assistant.....How can i help your sir....')
    
if __name__ == '__main__':
     Alaram()
     
     while True:
         query=Command().lower()
         if 'wikipedia' in query:
             speak('searching wikipedia.....')
             query=query.replace('wikipedia'," ")
             results=wikipedia.summary(query,sentences=1)          
             speak('According to wikipedia..') 
             speak(results)
             print(results)
             
         elif 'open youtube' in query:
            #  webbrowser.open('chrome/youtube.com')   
               webbrowser.open('https://www.youtube.com')
               
               
         elif 'open instagram' in query:
             webbrowser.open('https://instagram.com/')
             
         elif  'play music' in query:
             music_dir='C:\\Users\\RATAN\Music\\MEmu_Music'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,random.choice(songs)))
             
         elif 'tell me the  time' in query:
             time=datetime.datetime.now().strftime("%H:%M:%S")  
             speak(f'Your current time is {time} ')    
             print(time)
             
         else:
             speak('please  sir say something clearly....')
         
                 
             
        #  elif  'check email' in query:
        #      try:
        #          speak('')      

             
                 
             
               
                   
     