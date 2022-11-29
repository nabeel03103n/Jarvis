from googlesearch import search
import webbrowser

query = input("Enter:\n")
result = search(query)

j = ""
for j in search(query, tld="co.in", num=1, stop=1, pause=1):
    print(j)
    webbrowser.open(j)
    if "www" in j:
        print("YES!")
    