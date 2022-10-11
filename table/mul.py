# inp = input("Enter:\n")

# val = "by"
# val1 = "x"

# if val in inp:
#     inp = inp.replace(val,"")
#     if "what is" in inp:
#         inp = inp.replace("what is","")
#         inp = inp.split()
#         pr1 = int(inp[0])
#         pr2 = int(inp[1])
#         print(f"{pr1} x {pr2} = {pr1*pr2}")

# elif val1 in inp:
#     inp = inp.replace(val1,"")
#     if "what is" in inp:
#         inp = inp.replace("what is","")
#         inp = inp.split()
#         pr1 = int(inp[0])
#         pr2 = int(inp[1])
#         print(f"{pr1} x {pr2} = {pr1*pr2}")


inp = input("Enter:\n")

if "cube" in inp:
    if "what is the cube of" in  inp:
        inp = inp.replace("what is the cube of","")
        inp = int(inp)
        print(f"The answer is {inp*inp*inp}")

    else:
        inp = inp.replace("cube of","")
        inp = int(inp)
        print(f"The answer is {inp*inp*inp}")



