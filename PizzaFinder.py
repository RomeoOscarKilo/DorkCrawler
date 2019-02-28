try:
    from bs4 import BeautifulSoup
except:
    print("BS4 Not found")
try:
    import requests
except:
    print("Request not found")

try:
    import time
except:
    print("Time module not found")

try:
    import webbrowser
except:
    print("WehBrowser could not be imported")

def UserFinder(page):
    try:
        r = requests.get('https://www.google.com/search?q=frontpage+screenshot+pizza+site%3Aimgur.com%2Fuser&filter=0&start=' + str(page))
        print(r)
    except:
        print("Please update google get string, must include filter=0 , a query and start= for this to work")
    soup = BeautifulSoup(r.text , 'html.parser')
    results = soup.find_all('cite')
    for result in results:
        url = result.contents[0]
        print("here")
        print(url)
        webbrowser.open_new_tab(url)
    return


i = 0
while i < 10 :
    UserFinder(i * 10)
    i += 1
    time.sleep(15)


print("Done")
