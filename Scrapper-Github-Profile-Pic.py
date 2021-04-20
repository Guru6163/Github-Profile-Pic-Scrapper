import requests
from bs4 import BeautifulSoup as bs
github_username=str(input("Enter the Github UserName: "))
url="http://github.com/"+github_username
r=requests.get(url)
soup=bs(r.content,"html.parser")
profile_image=soup.find("img",{"alt":"Avatar"})["src"]
print(profile_image)
