import keyboard as k

# k.press_and_release('alt+tab')
# k.write("Hello World")
if k.wait('esc') != None:
    print("Done!")
else:
    print('No!')