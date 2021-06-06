import requests
import re

URL ="https://econpy.pythonanywhere.com/ex/001.html"

if __name__ == '__main__':

    #response = requests.get(URL)

    #if response.status_code == 200:
        #content = response.text 
    with open('econpy.html', 'r') as file:
        content = file.read()

        regex = '<div title="buyer-name">(.+?)</div>'

        for title in re.findall(regex, content):
            print(title)