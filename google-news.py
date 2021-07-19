import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrMVlLQUFQAQ?hl=es-419&gl=MX&ceid=MX%3Aes-419'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        now = datetime.now().strftime('%d_%m_%Y')
        print(now)
        # newa_dia_mes_ano.txt
        with open(f'news/news_{now}.text', 'w+') as file:
        #print(soup.prettify())
            for element in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb',   limit=20):

                title = element.a.text
                #print(title)
                file.write(title + '\n')
    
    print('Archivo generado de manera exitosa')

