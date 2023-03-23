import datetime
import time


inp = input("Enter Time in seconds Or type h for hours and m for minutes:\n")
inp = inp.lower()

if inp == "h":
    print("hours")
    inp = input("Enter Time in Hours Or type s for Seconds and m for minutes:\n")
    inp = inp.lower()


elif inp == 'm':
    print("Minutes")
    inp = input("Enter Time in Minutes Or type s for Seconds and h for Hours:\n")
    inp = inp.lower()
    inp = int(inp)
    inp = inp*60
    print(f"The time is now set for {inp} seconds")
    for i in range(inp+1):
        # time.sleep(i)
        print(i)


else:
    inp = int(inp)
    for i in range(inp+1):
        time.sleep(i)
        print(i)

    print("Now you're time is over")