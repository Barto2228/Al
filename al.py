
import pyttsx3 

engine = pyttsx3.init()
words = input()
engine.say(words)
engine.runAndWait()
