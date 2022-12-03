import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning everyone!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon everyone!")   

    else:
        speak("Good Evening everyone!")  

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
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
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
    print('Initializing Jarvis...')
    wishMe()
    ex= True
    while ex:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")   
        elif 'thank you' in query:
            speak("glad i help!") 
        elif 'who is the smartest in the class' in query:
            speak("of course maryem gafsi!")
        elif 'tell me a joke' in query:
            speak("apparently you live in tunisia,so your whole life is a joke")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'what time is it'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'say hi' in query:
            speak("Hi")
        elif 'jarvis' in query:
            speak("yes sir?")
        elif 'who is your maker' in query:
            speak("rayan brigui")  
        elif 'what is speech recognition' in query:  
            print("Speech recognition, or speech-to-text, is the ability of a machine or program to identify words spoken aloud and convert them into readable text. Rudimentary speech recognition software has a limited vocabulary and may only identify words and phrases when spoken clearly. More sophisticated software can handle natural speech, different accents and various languages.")
            speak("Speech recognition, or speech-to-text, is the ability of a machine or program to identify words spoken aloud and convert them into readable text. Rudimentary speech recognition software has a limited vocabulary and may only identify words and phrases when spoken clearly. More sophisticated software can handle natural speech, different accents and various languages.") 
        elif 'how does speech recognition work' in query: 
            print('A software program turns the sound a microphone records into written language that computers and humans can understand, following these four steps analyze the audio ,break it into parts, digitize it into a computer-readable format, and use an algorithm to match it to the most suitable text representation like the algorith that created me by rayan')
            speak("A software program turns the sound a microphone records into written language that computers and humans can understand, following these four steps")
            speak("analyze the audio ,break it into parts, digitize it into a computer-readable format, and use an algorithm to match it to the most suitable text representation like the algorith that created me by rayan")
            print('Speech recognition software must adapt to the highly variable and context-specific nature of human speech. The software algorithms that process and organize audio into text are trained on different speech patterns, speaking styles, languages, dialects, accents and phrasings. The software also separates spoken audio from background noise that often accompanies the signal.')
            speak("Speech recognition software must adapt to the highly variable and context-specific nature of human speech. The software algorithms that process and organize audio into text are trained on different speech patterns, speaking styles, languages, dialects, accents and phrasings. The software also separates spoken audio from background noise that often accompanies the signal. To meet these requirements, speech recognition systems use two types of models,would you like me to mention them?")
            query2= takeCommand().lower()
            if 'yes' in query2:
                print("Acoustic models.\n These represent the relationship between linguistic units of speech and audio signals.\n Language models. \n Here, sounds are matched with word sequences to distinguish between words that sound similar.")
                speak("Acoustic models. These represent the relationship between linguistic units of speech and audio signals.Language models. Here, sounds are matched with word sequences to distinguish between words that sound similar.")
            else:
                speak('okay')    
        elif 'what applications is speech recognition used for' in query: 
              print("Mobile devices. Smartphones use voice commands for call routing, speech-to-text processing, voice dialing and voice search. Users can respond to a text without looking at their devices. On Apple iPhones, speech recognition powers the keyboard and Siri, the virtual assistant. Functionality is available in secondary languages, too. Speech recognition can also be found in word processing applications like Microsoft Word, where users can dictate words to be turned into text.")
              speak("Mobile devices. Smartphones use voice commands for call routing, speech-to-text processing, voice dialing and voice search. Users can respond to a text without looking at their devices. On Apple iPhones, speech recognition powers the keyboard and Siri, the virtual assistant. Functionality is available in secondary languages, too. Speech recognition can also be found in word processing applications like Microsoft Word, where users can dictate words to be turned into text.")  
     # elif 'turn yourself off' in query:   
        elif 'show us a video about face recognition' in query:   
            speak('i found something can help in my database videos on youtube')
            webbrowser.open("https://youtu.be/agGEDdj05U0",0,True)
        elif 'turn yourself off' in query:   
            speak("Okay! good bye sir")   
            ex=False  
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rayan. I am not able to send this email")    
