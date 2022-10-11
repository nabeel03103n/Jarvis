from pickle import TRUE
from random import random
from winreg import QueryReflectionKey
from cv2 import VideoCapture, imshow, imwrite, waitKey
from django.http import QueryDict
from gtts import gTTS
from playsound import playsound
import pyttsx3
from regex import W #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from sympy import content
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui as p
from time import sleep
import gtts
import cv2
from googlesearch import search
import pyjokes
import random


brothers = {
    "brother0":"Umair R Khan",
    "brother1":"Uzair R Khan",
    "brother2":"Md. Ali Khan",
    "brother3":"Aman Ali Khan",
    "brother4":"Uroob Ali",
    "brother5":"Uwais Raza Khan",
    "brother6":"Ozam",
    "brother7":"Zydan Ali Khan",
    "brother8":"Yusuf Bhai"
    }

friends = {
    "best friend":"Juvira",
    "good friend":"Yusuf",
    "friend0":"Sanila",
    "friend1":"Hashir",
    "friend2":"Atif",
    "friend3":"Almas",
    "friend4":"Abdullah",
    "friend5":"Rahim",
    "friend6":"Aayan",
 
}

rela = {
    "mother":"Misses Lubna Aquil",
    "father":"Mister Shabbir Ali Khan",
    "brother":"Mister Aman Ali Khan",
    "dadu":"Mister Fareed Ullah Khan",
    "Dadi":"Misses Bilkis ara or Tameez bano",
    "baba":"Mister Viqar Ali Khan",
    "chachu":"Mister Amir Ali Khan",
    "chachi":"Misses Kishvar",
    "nanu":"Mister Abid Ali Khan",
    "nannan":"Misses Mujeeb Unnisa",
    "Mama":"Mister Kousar Ali",
    "mami":"Misses Nida",
    "amma":"Misses Naghma Aquil",
    "Samin Khalu":"Mister Sameen Khan",
    "Mem Mamma":"Misses Mehrunnisa",
    "Parvez Khalu":"Mister Parvez Raza Khan",
    "Rumi":"Rumana Saif",
    "Saif bhai":"Saif Umar Khan",
    "Rabiya":"Rabiya kousar",
    "Baria":"Baria Ameen"
}


questions = {"0":"What are two things you can never eat for breakfast?",
"1":"What is always coming but never arrives?",
"2":"What gets wetter the more it dries? ",}

answers = {"0":"Answer - Lunch and Dinner",
"1":"Answer - Tomorrow",
"2":"Answer - A towel",}

name = "nabeel"
master = "Master"
password = "hello world"

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
        speak(f"Good Morning! {master} {name}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon! {master} {name}")   

    else:
        speak(f"Good Evening! {master} {name}")  

    speak(f"I am Jarvis {master} {name}. Please tell me how may I help you")       

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarvisaipy@gmail.com', 'nabeel_ali_khan')
    server.sendmail('nabeel03103n@gmail.com', to, content)
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
            speak("According to Wikipedia")
            print(results)
            speak(results)

# greeting section

        elif "how are you" in query:
            speak("I am fine thanks for asking and how are you")
            print("I am fine thanks for asking and how are you")

        elif "I need your help" in query:
            print("Yeah! Sir, I'm always here to help you.")
            speak("Yeah! Sir, I'm always here to help you.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "hello jarvis" in query:
            print("Hello")
            speak(f"Hello {master}")

        elif "thanks" in query:
            print(f"No {master} is my pleasure")
            speak(f"No {master} is my pleasure")

        elif "thanks jarvis" in query:
            print(f"No {master} is my pleasure")
            speak(f"No {master} is my pleasure")

        elif "thank you jarvis" in query:
            print(f"No {master} is my pleasure")
            speak(f"No {master} is my pleasure")

        elif "thanks for your help jarvis" in query:
            print(f"No {master} is my pleasure")
            speak(f"No {master} is my pleasure")

        elif "what are you doing" in query:
            speak("i am talking to you")
            print("i am talking to you")

        elif "what is your name" in query:
            speak("My name is jarvis, please tell me how may i help you")
            print("My name is jarvis, please tell me how may i help you")

        elif "I am fine" in query:
            speak(f"okay sounds good {master}")
            print(f"okay sounds good {master}")

        elif "I am also fine" in query:
            speak(f"okay sounds good {master}")
            print(f"okay sounds good {master}")

        elif "also fine" in query:
            speak(f"okay sounds good {master}")
            print(f"okay sounds good {master}")


#Jokes

        elif "me a joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            speak(My_joke)

        elif "me some jokes" in query:
            while TRUE:
                My_joke = pyjokes.get_joke(language="en", category="all")
                print(My_joke)
                speak(My_joke)


#Hindi
        elif "hindi" in query:
            ask = input("Enter:\n")
            if ask =="hindi":
                text = gTTS("मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")
                text.save("sound//text.mp3")
                playsound("sound//text.mp3")
                os.remove("sound//text.mp3")





#functions
        elif "click my photo" in query:
            speak(f"I am clicking you photo {master}")
            print(f"I am clicking you photo {master}")


            cam_port = 0
            cam = VideoCapture(0)

            result, image = cam.read()

            if result:
                imshow("Image",image)
                imwrite("Image.png",image)
                waitKey(0)
            else:
                speak(f"Sorry {master} i'm not able to click your photo")

        elif "my photo" in query:
            speak(f"I am clicking you photo {master}")
            print(f"I am clicking you photo {master}")


            cam_port = 0
            cam = VideoCapture(0)

            result, image = cam.read()

            if result:
                imshow("Image",image)
                imwrite("Image.png",image)
                waitKey(0)
            else:
                speak(f"Sorry {master} i'm not able to click your photo")


# friends section

        elif "who is my best friend" in query:
            best_friend = friends["best friend"]
            speak(f"{best_friend} is your bestest friend")
            print(f"{best_friend} is your bestest friend")

        elif "who is juvira" in query:
            best_friend = friends["best friend"]
            speak(f"{best_friend} is your bestest friend {master}")
            print(f"{best_friend} is your bestest friend {master}")

        elif "who is my good friend" in query:
            good_friend = friends["good friend"]
            speak(f"{good_friend} is your good friend {master}")
            print(f"{good_friend} is your good friend {master}")

        elif "who is yusuf" in query:
            good_friend = friends["good friend"]
            speak(f"{good_friend} is your good friend {master}")
            print(f"{good_friend} is your good friend {master}")


        elif "who is kriti" in query:
            friend = friends["friend7"]
            speak(f"{friend} Kriti is one of your friend {master}")
            print(f"{friend} Kriti is one of your friend {master}")

        elif "who is sunny le" in query:
            friend = friends["friend0"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is hashir" in query:
            friend = friends["friend1"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is atif" in query:
            friend = friends["friend2"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is almas" in query:
            friend = friends["friend3"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is abdullah" in query:
            friend = friends["friend4"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is rahim" in query:
            friend = friends["friend5"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "who is ayaan" in query:
            friend = friends["friend6"]
            speak(f"{friend} is one of your friend {master}")
            print(f"{friend} is one of your friend {master}")

        elif "all friends" in query:
            speak(f"{friends}")
            print(f"{friends}")

        elif "all my friends" in query:
            speak(f"{friends}")
            print(f"{friends}")



#Me
        elif "who is your master" in query:
            speak(f"My {master} {name} is one of the greatest man on earth")
            print(f"My {master} {name} is one of the greatest man on earth")

        elif "who is nabeel" in query:
            speak(f"My {master} {name} is one of the greatest man on earth")
            print(f"My {master} {name} is one of the greatest man on earth")

        elif "I am nabeel" in query:
            speak(f"oh! always good to see you {master}")
            print(f"oh! always good to see you {master}")

        elif "I am Nabeel" in query:
            speak(f"oh! always good to see you {master}")
            print(f"oh! always good to see you {master}")
   
        elif "I am your master" in query:
            speak(f"oh! always good to see you {master}")
            print(f"oh! always good to see you {master}")


# relativies sections
# fahter
        elif "who is my fahter" in query:
            father = "Mr.Shabbir Ali Khan"
            speak(f"{father} is your father {master}")
            print(f"{father} is your father {master}")

        elif "my fahter" in query:
            father = "Mr.Shabbir Ali Khan"
            speak(f"{father} is your father {master}")
            print(f"{father} is your father {master}")

        elif "who is shabbir ali khan" in query:
            father = "Mr.Shabbir Ali Khan"
            speak(f"{father} is your father {master}")
            print(f"{father} is your father {master}")

#Baria
        elif "who is baria" in query:
            baria = "Baria Ameen"
            speak(f"{baria} is the doughter of sameen khalu and amma")


# brothers
        elif "who is my brother" in query:
            brother = "Aman Ali Khan"
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")
            
        elif "my brother" in query:
            brother = "Aman Ali Khan"
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")
            
        elif "who is aman ali khan" in query:
            brother = "Aman Ali Khan"
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")

        elif "who is brother0" in query:
            brother = brothers["brother0"]
            speak(f"{brother} is your brother {master}")

        elif "who is umair" in query:
            brother = brothers["brother0"]
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")

        elif "who is uzair" in query:
            brother = brothers["brother1"]
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")


        elif "who is my elder brother" in query:
            brother = brothers["brother1"]
            speak(f"{brother} is your brother {master}")
            print(f"{brother} is your brother {master}")
  
        elif "all brothers" in query:
            speak(brothers)
            print(brothers)

        elif "brothers" in query:
            speak(brothers)
            print(brothers)

        elif "all my homies" in query:
            speak(rela)
            print(rela)


# mother
        elif "who is my mother" in query:
            mother = "Mrs.Lubna Aquil"
            speak(f"{mother} is your mother {master}")
            print(f"{mother} is your mother {master}")

        elif "my mother" in query:
            mother = "Mrs.Lubna Aquil"
            speak(f"{mother} is your mother {master}")
            print(f"{mother} is your mother {master}")

        elif "who is Lubna" in query:
            mother = "Lubna Aquil"
            speak(f"{mother} is your mother {master}")
            print(f"{mother} is your mother {master}")






# nanu

        elif "who is my grandfather" in query:
            grandfather = "Mr.Abid Aquil"
            speak(f"{grandfather} is your grandfather {master}")
            print(f"{grandfather} is your grandfather {master}")
            
        elif "who is Abid Aquil" in query:
            grandfather = "Mr.Abid Aquil"
            speak(f"{grandfather} is your grandfather {master}")
            print(f"{grandfather} is your grandfather {master}")

# nannan
        elif "who is my grandmother" in query:
            grandmother = "Mrs.Mujeeb unnisa"
            speak(f"{grandmother} is your grandmother {master}")
            print(f"{grandmother} is your grandmother {master}")

# mem mamma
        elif "who is name" in query:
            mem = "Mrs.Meher unnisa"
            speak(f"{mem} is your mem mamma")
            print(f"{mem} is your mem mamma")

#Messaging 

        # elif "message rose on whatsapp":
        #     print("Roger That")
        #     speak("Roger That")

        #     os.startfile("C:\\Users\\Metro\\OneDrive\\Desktop\T\WhatsApp.lnk")


        elif "yusuf on instagram" in query:
            speak("What should i say")
            print("What should i say")

            content = takeCommand()


            webbrowser.open("https://www.instagram.com/__yusuf_zaid__/")
            sleep(7)
            p.click(1067,323)
            sleep(5)
            p.typewrite(content)
            p.press('enter')

        elif "mass on instagram" in query:
            speak("What should i say")
            print("What should i say")

            content = takeCommand()


            webbrowser.open("https://www.instagram.com/maazkhan_147/")
            sleep(7)
            p.click(1067,323)
            sleep(5)
            p.typewrite(content)
            p.press('enter')


        elif "message faisal on instagram" in query:
            speak("Roger That")
            print("Roger That")

            webbrowser.open("https://www.instagram.com/faisal_8005/")
            sleep(4)
            p.click(1067,322)
            sleep(4)
            
            p.click(1012,932)
            p.typewrite("Hello Yusus I am Jarvis")
            p.press('enter')

        elif "message aryan on instagram" in query:
            speak("Roger That")
            print("Roger That")

            webbrowser.open("https://www.instagram.com/aryan_banna_001/")
            sleep(4)
            p.click(1067,323)
            sleep(4)
            
            p.click(1012,932)
            p.typewrite("Hello Aryan I am Jarvis")
            p.press('enter')

        elif "search on instagram" in query:
            speak("Enter Username")
            inp = input("Enter Username:\n")
            webbrowser.open(f"https://www.instagram.com/{inp}")

#Meetup

        elif "meet him he is my friend" in query:
            print(f"It's sounds good {master}, What is his name?")
            speak(f"It's sounds good {master}, What is his name?")

            content = takeCommand()

            if "he is" in content:
                def Convert(string):
                    li = list(string.split("he is"))
                    return li
  
                # Driver code    
                list = (Convert(content))
                print(f"So! Hello{list} ")
                speak(f"So! Hello{list} ")

        elif "meet her she is my friend" in query:
            print(f"It's sounds good {master}, What is her name?")
            speak(f"It's sounds good {master}, What is her name?")

            content = takeCommand()

            if "she is" in content:
                def Convert(string):
                    li = list(string.split("she is"))
                    return li
  
                # Driver code    
                list = (Convert(content))
                print(f"So! Hello{list} ")
                speak(f"So! Hello{list} ")

#Creating Files

        elif "create a python file" in query:
            with open("D:\\TEST\\PYTHON\\Files\\untittled.py",'w')as f:
                f.write("")
                os.startfile("D:\\TEST\\PYTHON\\Files\\untittled.py")


        elif "create a text file" in query:
            with open("D:\\TEST\\PYTHON\\Files\\untittled.txt",'w')as f:
                f.write("")
                os.startfile("D:\\TEST\\PYTHON\\Files\\untittled.txt")

#Country Code

        elif "country code" in query:
            os.startfile("country\\country.py")




#fun mode

        elif "repeat after me" in query:
            query1 = query.replace("repeat after me","")
            print(query1)
            speak(query1)


        elif "draw a car" in query:
            from drawing import car,car1,car2,car3
            list = [car,car1,car2,car3]
            car = random.choice(list)
            print("Roger That")
            speak("Roger That")
            car.draw()
#Math

        elif "table of" in query:
            inp = query.replace("table of","")
            inp = int(inp)          

            for i in range(11):

                i1 = inp*i
                form = f"{inp} x {i} = {i1}"
                form1 = f"{inp} {i}s are {i1}"
                print(form)
                speak(form1)


        elif "by" in query:
            try: 
                def test():
                    inp = query

                    val = "by"

                    if val in inp:
                        inp = inp.replace(val,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} x {pr2} = {pr1*pr2}")
                            speak(f"{pr1} x {pr2} = {pr1*pr2}")


                test()
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")


        elif "what is my phone number" in query:
            print("+917424810385")
            speak("your phone number is 7424810385")
 



        elif "cube" in query:
            try:
                inp = query
                if "cube" in inp:
                    if "what is the cube of" in  inp:
                        inp = inp.replace("what is the cube of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp*inp}")
                        speak(f"The answer is {inp*inp*inp}")
                        

                    else:
                        inp = inp.replace("cube of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp*inp}")
                        speak(f"The answer is {inp*inp*inp}")
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")
            

        elif "plus"or"+" in query:
            try: 
                def test():
                    inp = query

                    val = "plus"
                    val1 = "+"

                    if val in inp:
                        inp = inp.replace(val,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} + {pr2} = {pr1+pr2}")
                            speak(f"{pr1} + {pr2} = {pr1+pr2}")

                    elif val1 in inp:
                        inp = inp.replace(val1,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} + {pr2} = {pr1+pr2}")
                            speak(f"{pr1} + {pr2} = {pr1+pr2}")
                test()
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")


        elif "square" in query:
            try:
                inp = query
                if "square" in inp:
                    if "what is the square of" in  inp:
                        inp = inp.replace("what is the square of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp}")
                        speak(f"The answer is {inp*inp}")
                        

                    else:
                        inp = inp.replace("square of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp}")
                        speak(f"The answer is {inp*inp}")
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")
            
 


# opening section


        elif 'open facebook' in query:
            speak("opening facebook")
            print("opening facebook")
            webbrowser.open("https://www.facebook.com/")


        elif 'open instagram' in query:
            speak("opening instagram")
            print("opening instagram")
            os.startfile("C:\\Users\\Metro\\OneDrive\\Desktop\\Instagram.lnk")

        elif 'youtube' in query:
            speak('Searching Youtube...')
            print('Searching Youtube...')
            query = query.replace("youtube", "")

            os.startfile("C:\\Users\\Metro\\OneDrive\\Desktop\\YouTube.lnk")
            sleep(7)
            p.click(688,78)
            sleep(1)
            p.typewrite(query)
            p.press('enter')

            # speak("Do you want to search it manually")
            # ask = input("Do you want to search it manually:\n")
            # if "no" in ask:
            #     say = speak("What you want to search on youtube")
            #     asking = input("What you want to search on youtube:\n")

            #     speak("opening youtube")
            #     print("opening youtube")




        elif 'open google' in query:
            speak("Do you want to search it manually")
            ask = input("Do you want to search it manually:\n")
            if "no" in ask:
                say = speak("What you want to search on Google")
                asking = input("What you want to search on Google:\n")

                speak("opening Google")
                print("opening Google")
                webbrowser.open("https://www.google.com/")
                sleep(3)
                p.click(693,461)
                sleep(1)
                p.typewrite(asking)
                sleep(1)
                p.click(1460,456)
                sleep(1)
                p.click(839,555)




            webbrowser.open("https://www.google.com/")
            speak("opening Google")
            print("opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")   
            speak("openiing stackoverflow")
            print("openiing stackoverflow")


        elif 'play music' in query:

            p.press("win")
            sleep(2)
            p.typewrite("spotify")
            sleep(2)
            p.press("enter")
            sleep(2)
            p.press("space")


            

        elif "ask me" in query:
            q = random.choices(questions)
            print(q)
            speak(q)

            q = random.choices(answers)
            print(q)
            speak(q)

        elif "show me your face" in query:
            os.startfile("D:\\TEST\\PYTHON\\tkinter\\jarvis1\\videos\\intro.MP4")

        elif "animals name" in query:
            with open("list-animals-world-611j.csv")as f:
                speak1 = f.read()

                print(speak1)
                speak(speak1)

        elif 'open code' in query:
            codePath = "C:\\Users\\Metro\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'mail to Nabeel' in query:
            print("What should i say")
            speak("What should i say")
            content1 = takeCommand()
            p.click(849,1042)
            sleep(3)
            p.click(830,439)
            sleep(2)
            p.typewrite("gmail.com")
            p.press("enter")
            sleep(8)
            p.click(130,254)
            sleep(1)
            p.typewrite("nabeel.ali.private@gmail.com")
            sleep(1)
            p.click(1389,456)
            p.click(1389,456)
            sleep(1)
            p.typewrite("Hello I am Jarvis")
            sleep(1)
            p.click(1269,555)
            sleep(1)
            p.typewrite(content1)
            sleep(1)
            p.click(1136,970)




        # elif("I am not your master"):
        #     speak("So who are you and where is my master")
        #     print("So who are you and where is my master")
        #     speak("Enter the Password")
        #     inp = input("Enter the password:\n")
        #     if inp == password:
        #         speak("Enter your name")
        #         asking_name = input("Enter your name:\n")
        #         if asking_name == name:
        #             speak("Oh master here you are, i am looking for you,because i think someone else is using me without your permission. oh sorry master i didn't recognize its you i am such a fool")
                    
        #             print("Oh master here you are, i am looking for you,because i think someone else is using me without your permission. oh sorry master i didn't recognize its you i am such a fool")



        #         name = asking_name

        #         hour = int(datetime.datetime.now().hour)
        #         if hour>=0 and hour<12:
        #             speak("Good Morning!")

        #         elif hour>=12 and hour<18:
        #             speak(f"Good Afternoon! {name}")   

        #         else:
        #             speak(f"Good Evening! {name}")  


                    

        #     else:
        #         speak("The password is wrong")
        #         print("The password is wrong")
        #         speak("Don't use me again fool")
        #         print("Don't use me again fool")


        else:
            speak("Done")
            webbrowser.open("https://google.com")
            sleep(3)
            p.typewrite(query)
            p.press("enter")


        with open("user_said.txt",'a')as f:
          f.write(query)
          f.write("\n")

