inp = input("Enter:\n")

val = "plus"
val1 = "+"

if val in inp:
    inp = inp.replace(val,"")
    if "what is" in inp:
        inp = inp.replace("what is","")
        inp = inp.split()
        pr1 = int(inp[0])
        pr2 = int(inp[1])
        print(f"{pr1} + {pr2} = {pr1+pr2}")

elif val1 in inp:
    inp = inp.replace(val1,"")
    if "what is" in inp:
        inp = inp.replace("what is","")
        inp = inp.split()
        pr1 = int(inp[0])
        pr2 = int(inp[1])
        print(f"{pr1} + {pr2} = {pr1+pr2}")

