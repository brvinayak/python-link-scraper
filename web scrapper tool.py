import requests
from bs4 import BeautifulSoup

url=input("Enter the website URL:")
if not url.startswith(("http://","https://")):
    url="https://"+url

links=set()

try:
    response=requests.get(url)

    if response.status_code==200:
        print("Page successfully fetched...\n")
        soup=BeautifulSoup(response.text,"html.parser")
        print(f"Website Title:{soup.title.text}\n")
        print(response.text[:200])
        
        for link in soup.find_all("a"):
            href=link.get("href")
            if href:
                links.add(href)

    elif response.status_code==404:
        print("Page not found!!")

    else:
        print(f"Error {response.status_code}")


except:
    print("Error ocurred while fetching the page...")

print(links)

with open ("links.txt","w") as f:
    for link in links:
        f.write(link+"\n")
    f.write(f"Total links :{len(links)}")