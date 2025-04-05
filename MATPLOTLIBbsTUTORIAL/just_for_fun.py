from win32com.client import Dispatch
a = input("enter the string")
str = f" {a}"

a = Dispatch("SAPI.SpVoice")
while(1):
    s = a.speak(str)
    print(s)
    ex = input()
    if ex.isalpha():
        exit()

