from shutil import which


from pyttsx3 import speak

while True:

    inp = input("Enter:\n")
    inp = int(inp)


    

    for i in range(11):

        i1 = inp*i
        form = f"{inp} x {i} = {i1}"
        form1 = f"{inp} {i}s are {i1}"
        print(form)
        speak(form1)