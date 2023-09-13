import webbrowser

print  ("Hello, What is your name?")
name = input()
print ("Hello \n" + name)

options = ["Microsoft", "Ubuntu"]
url1 = "https://www.microsoft.com/en-us/?ql=2"
url2 = "https://ubuntu.com/"

choice = input(options)

if choice == ("Microsoft"):
   webbrowser.open(url1)
else: webbrowser.open(url2) 


    