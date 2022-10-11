from pyttsx3 import speak


speak("Enter Country Name or Dailing Code or Short Name")
while True:


    inp = input("Enter Country Name or Dailing Code or Short Name:\n")

    with open("country\\db.txt")as f:
        for i in range(281):
            f1 = f.readline(i)
            if inp in f1:
                print(f1)
                speak(f1)

