from datetime import datetime

def morning():
    print("Good morning!")

def afternoon():
    print("Good afternoon!")

def evening():
    print("Good evening!")

def whattime():
    now = datetime.now()
    print("It is now",now.strftime("%H:%M:%S"))

