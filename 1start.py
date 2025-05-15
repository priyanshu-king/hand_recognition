#print("enter 2 numbers")
#a=int(input())
#b=int(input())
#c=a+b
#print("the total number  " ,c)

# print("enter two number ")
# x=5
# y=6
# print(x)
# print(y)

# a = int(input("enter the number : "))
# b = int(input("enter 2nd number : "))
# c = a+b
# print("the sum of num1 and num2 is  "  , c)


# a,b = int(input("enter the number : ")) , int(input("enter the number : "))
# print("the sum is " , a*b)

# x = int(input("enter the number : "))
# if x>0 :
#     print("the no is positive ")
# elif x<0 :
#     print("the number is negative  ")
# else :
#     print(" zero" )

# x = int(input("enter the number "))

# if x%2 == 0:
#     print("its even number ")
# else :
#     print("its odd number ")

# a = int(input("enter the number :"))
# b = int(input("enter the 2nd number : "))
# c =  1/2* a* b

# print("the area of triangle is " , c)

# a = int(input("enter the number : "))
# b = int(input("enter the number of 2nd number "))
# x = int(input("enter the 3rd number "))
# SI = a*b*x/100

# print("the simple intrest are " , SI)

# x = int(input("enter the number "))
# i=1 
# while i<=x :
#     print("kohinoor")
#     i+=1
    
# x = int(input("enter the number "))
# i=1
# while i<= 10 :
#      print(x*i)
#      i+=1

# n = int(input("enter the number "))
# i=1
# fact =1
# while i<n :
#     print(i)
#     fact*= i
#     i+=1
#     print("the sum is " , fact) 


# ***** sum of natural numbers******

# num = 18
# if num < 0 :
#     print("enter the positive integer ")
# else :
#     sum = 0 
#     while (num>0) :
#       sum += num
#       num -= 1
#     print("the sum is " , sum)

# a = input("enter your name : ")
# a = int(a)
# print(type(a))
    
# a = 30
# b = 40 
# c = a+b
# print("the sum of a and b is " , c)    

# a = int(input())
# b = int(input())
# c = a+b 
# print("the sum of 2 is " , c)

# a = int(input("\nenter 1st number"))
# b = int(input("\nenter 2nd number"))
# c = (a+b)/2
# print("the average of two no is " , c)

# letter = '''dear <!name!>
# you are selected 
# <!date!>
# '''
# name = input("enter your name")
# date = input("enter your date")
# letter = letter.replace("<|name|" , name)
# letter = letter.replace("|date|>" , date)
# print(letter)

# f1 = input("enter fruit no 1")
# f2 = input("enter fruit no 2")
# f3 = input("enter fruit no 3")
# f4 = input("enter fruit no 4")
# f5 = input("enter fruit no 5")
# f6 = input("enter fruit no 6")
# f7 = input("enter fruit no 7")


# myfruitlist = [f1,f2,f3,f4,f5,f6,f7]
# print(myfruitlist)

# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("sky blue")

# # Create a turtle to draw the rainbow
# rainbow = turtle.Turtle()
# rainbow.speed(10)  # Set the speed of the turtle

# # Define the colors of the rainbow
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# # Draw the rainbow
# radius = 200
# for color in colors:
#     rainbow.color(color)
#     rainbow.begin_fill()
#     rainbow.circle(radius, 180)  # Draw a semi-circle
#     rainbow.left(90)
#     rainbow.forward(20)
#     rainbow.left(90)
#     rainbow.circle(radius + 20, -180)
#     rainbow.left(90)
#     rainbow.forward(20)
#     rainbow.left(90)
#     radius += 20
#     rainbow.end_fill()

# # Hide the turtle
# rainbow.hideturtle()

# Keep the window open until clicked
# screen.mainloop()
# a = int(input("enter 1st number : "))
# b = int(input("enter 2nd number : "))
# c = int(input("enter 3rd number :"))
# # alculate the semi perimeter
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("the area of triangle is %0.2f"%area) 

#  a = int(input("enter 1st no : "))
#  b = int(input("enter 2nd no :"))
#  c = int(input("enter 3d no :"))
#  # for semi p
#  s = (a+b+c)/2
#  # for  triangle
#  area = (s*(s-a)*(s-b)*(s-c))**0.5
#  print("the area of a triangle %0.2f"%area)
# add = lambda num:num + 4
# print(add(9))
# product = lambda x,y :x*y
# print(product)
# marks = {
#     "priyanshu": 100,
#     "yoyn": 50,
#     "ayush" : 30,
#     0: "priyanshu"
      
# }
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("priyanshu"))  
# marks.update({"priyanshu" : 88})
# print(marks)

# thisistuple = ("apple","mango", "banana")
# print(len(thisistuple))
# n = int(input("enter the number :"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
    
# n = int(input("enter the number :"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
# l = ["rohan" , "suhani", "ashreen", "ansh"]
# for name in l :
#     if(name.startswith("a")):
#         print(f"hello {name}")
    
#     n = int(input("enter the number :"))
#     i  = 1
#     while(i<11):
#         print(f"{n}*{i}={n*i}")    
#         i +=1

# n = int(input("enter the number  :"))
# for i in range(2,n):
#     if n%i == 0:
#         print("the number is not prime :")
#         break 
#     else:
#         print("the number is prime :")
        
# n = int(input("enter the number :"))
# i = 1
# sum = 0
# while (i <= n):
#  sum += i
#  i+=1
# print(sum)

# n = int(input("enter the number :" ))
# factorial = 1
# for i in range (1,n+1):
#     factorial = factorial*i
#     print(f"factorial of {n} is {factorial}")
# def goodday(name, ending) :
#     print("good day" + name)
#     print(ending)
    
    
# goodday("priyanshu","thank you")
# goodday("sanskar", "thank you")
# goodday("dhiraj sir", "thank you")
# def goodday(name ,ending = "honey singh"):
#     print(f"goodday,{name}")
#     print(ending)

# goodday("dhiraj sir", "thanks")
# goodday("priyanshu")
# def factorial(n):
#     if (n==0 or n==1):
#      return 1
#     return  n*factorial(n-1)
# n = int(input("enter the number :"))
# print(f"the factorial of the number is {factorial(n)}")

#def get(self):
    
    #return self
#ability to form diffrant form
#operator overload 
#c1+2
#data hiding
#concept of encaptulation
#every class wwl    l

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)
    
# n = int(input("enter  the number :"))
# print(f"the fa torial of the number {factorial(n)}")
# def greatest(a,b,c):
#  a = int(input("enter the first number :"))
#  b = int(input("enter the second number :"))
#  c = int(input("enter the third number :"))
#  if a>b and a>c :
#      return (f"the a({a}) is greater")
#  elif b>a and b>c:
#      return (f"the b ({b}) is greater")
#  else:
#      return (f"the c({c}) is greater")

# def greater(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = 5
# b = 20
# c = 15
# print(greater(a,b,c))
# def ftoc():
#    return  5*(f-32)/9


# f = int(input("convert celsius to farranite: "))
# c = ftoc(f)
# print(f"{round(c,2)}°C")

# print("a")
# print("a")
# print("c", end= " ")
# print("d", end= " ")
# def sum(n):
#  if(n==1):
#      return 1
#  return sum(n-1)+n

# print(sum(5))
# def pattern(m):
#     if(m==0):
#       return
#     print("*"* m)
#     pattern(m-1)
      
# pattern(6)     
# def inch_to_cm(inch):
#     return inch*2.54
# n = int(input("convert inch i9nto centimeters: "))
# print(f"the correponding value of this {inch_to_cm(n)}")

# def rem(l,word):
#     n=[]  
#     for item in l:
#         if not(item==word):
#           n.append(item.strip(word))
#         return n
# l = ["priyanshu ", "rohan","shivam","h"]
# # print(rem(l,"h"))
# def multiply(n):
#     for i in range(1,11):
#         print(f"{n}*{i}={n*i}")
        
# multiply(3)        
# num = int(input("enter the number :"))
# if num > 1:
#     for i in range(2,num):
#         if (num%i == 0):
#             print(num,"is not a prime number :")
#             break
#         else:
#             print(num, "is not a prime number :")
#     else : 
#         print(num, "is not a prime number :")
# num = int(input("enter the number :"))
# sum = 0
# temp = num
# while temp>0:
#     digit =  temp %10
#     sum += digit**3
#     temp//=10
#     if num == sum :
#         print(num, "is an amstrong number :")
#     else:
#         print(num," is not an amstrong nnummber :")

import speech_recognition as sr
import webbrowser
import musicLibrary
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5') 
newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))