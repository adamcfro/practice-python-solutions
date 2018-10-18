import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

with open('write_to_file_output.txt', 'w') as file:
    for heading in soup.find_all(class_='story-heading'):
        if heading.a:
            file.write(heading.a.text.replace("\n", " ").strip())
        else:
            file.write(heading.contents[0].strip())