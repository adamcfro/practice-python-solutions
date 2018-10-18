import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

for heading in soup.find_all(class_='story-heading'):
    if heading.a:
        print(heading.a.text.replace("\n", " ").strip())
    else:
        print(heading.contents[0].strip())