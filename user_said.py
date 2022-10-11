db_google = [
    "open google",
]

count_google = db_google.count("open google")

db_fb = [
"open facebook",
]

count_fb = db_fb.count("open facebook")

db_insta = [
"open instagram",
]

count_insta = db_insta.count("open instagram")



db_youtube = [
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
"open youtube",
    
]


db = [
    "hello world",
    "jarvis",       
    "how are you"
]


with open("user_said.txt")as f:
    read = f.read()
    word = read.split()

with open("db.txt",'a')as f:
    num = word.count("youtube")
    code = f"youtube = {num}:\n"
    f.write(code)
    
    num1 = word.count("instagram")
    code1 = f"instagram = {num1}:\n"
    f.write(code1)

    num2 = word.count("facebook")
    code2 = f"facebook = {num2}:\n"
    f.write(code2)

    num3 = word.count("google")
    code3 = f"google = {num3}:\n "
    f.write(code3)
    
    num4 = word.count("music")
    code4 = f"spotify = {num4}:\n \n"
    f.write(code4)