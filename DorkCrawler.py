import os
os.system("mode con cols=127 lines=30")

print(r"""
_______   ______   .______       __  ___      ______ .______          ___   ____    __    ____  __       _______ .______      
|       \ /  __  \  |   _  \     |  |/  /     /      ||   _  \        /   \  \   \  /  \  /   / |  |     |   ____||   _  \     
|  .--.  |  |  |  | |  |_)  |    |  '  /     |  ,----'|  |_)  |      /  ^  \  \   \/    \/   /  |  |     |  |__   |  |_)  |    
|  |  |  |  |  |  | |      /     |    <      |  |     |      /      /  /_\  \  \            /   |  |     |   __|  |      /     
|  '--'  |  `--'  | |  |\  \----.|  .  \     |  `----.|  |\  \----./  _____  \  \    /\    /    |  `----.|  |____ |  |\  \----.
|_______/ \______/  | _| `._____||__|\__\     \______|| _| `._____/__/     \__\  \__/  \__/     |_______||_______|| _| `._____|""")
print(r"""###############################################################################################################################""")
print()
print("Checking dependencies")
print("Initialising")
try:
    from bs4 import BeautifulSoup
    print("Initialising.")
except:
    print("BS4 Not found")
try:
    import requests
    print("Initialising..")
except:
    print("Request not found")

try:
    import time
    print("Initialising...")
except:
    print("Time module not found")

try:
    import webbrowser
    print("Initialising....")
except:
    print("WebbBrowser could not be imported")

def UserFinder(page):
    try:
        r = requests.get('https://www.google.com/search?q=frontpage+screenshot+pizza+site%3Aimgur.com%2Fuser&filter=0&start=' + str(page))
        #print(r.text)
    except:
        print("Please update google get string, must include filter=0 , a query and start= for this to work")
    soup = BeautifulSoup(r.text , 'html.parser')
    
    results = soup.find_all("div" , class_="BNeawe vvjwJb AP7Wnd")
    
#    print("Test2")
    for result in results:
        url = result.contents[0]
        print(url)
        #webbrowser.open_new_tab(url+ "/about")
    return

print()
print("-----------------------")                                                                                                                             
print("Crawler is now running!")
print("-----------------------")
print()
print("Output:")

print()

i = 0
while i < 10 :
    UserFinder(i)
#    print("Debug")
    i += 1
    time.sleep(15)


print("Done")
