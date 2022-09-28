from re_aqua import speak, playsound
def knock_jokes(i):
    speak("Knock Knock!")
    speak("Who's there?")
    if i>=0 and i<10:
        speak("Chickens!")
        speak("Chickens who?")
        speak("Wrong! Owls hoo, chickens cluck")
        playsound('jokes.wav')
    elif i>=10 and i<20:
        speak("Broken pencil!")
        speak("Broken pencil who?")
        speak("Nevermind it's pointless!")
        playsound('jokes.wav')
    elif i>=20 and i<30:
        speak("Tank!")
        speak("Tank who?")
        speak("You're welcome!")
        playsound('jokes.wav')
    elif i>=30 and i<40:
        speak("Nobel!")
        speak("Nobel who?")
        speak("Nobel, that's why I knocked!")
        playsound('jokes.wav')
    elif i>=40 and i<50:
        speak("Luke!")
        speak("Luke who?")
        speak("Luke through the peephole and find out!")
        playsound('jokes.wav')
    elif i>=50 and i<60:
        speak("Cow says!")
        speak("Cow says who?")
        speak("No, a cow says mooo!")
        playsound('jokes.wav')
    elif i>=60 and i<70:
        speak("Says!")
        speak("Says who?")
        speak("Says me!")
        playsound('jokes.wav')
    elif i>=70 and i<80:
        speak("Snow!")
        speak("Snow who?")
        speak("Snow use. The joke is over!")
        playsound('jokes.wav')
    elif i>=80 and i<90:
        speak("Woo!")
        speak("Woo who?")
        speak("Glad you're excited too!")
        playsound('jokes.wav')
    elif i>=90 and i<100:
        speak("Annie!")
        speak("Annie who?")
        speak("Annie way you can let me in!")
        playsound('jokes.wav')