import requests
from bs4 import BeautifulSoup

URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrMVlLQUFQAQ?hl=es-419&gl=MX&ceid=MX%3Aes-419'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        #print(soup.prettify())
        for element in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=20):
            title = element.a.text
            print(title)
