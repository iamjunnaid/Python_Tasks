# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, 
# use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, 
# just make up a name for the file you are saving to.

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
req = requests.get(url)
soup = BeautifulSoup(req.text,features="html.parser")

filename = input('Enter the file name: ')

with open(filename, 'w') as f:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            f.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            f.write(story_heading.contents[0].strip())