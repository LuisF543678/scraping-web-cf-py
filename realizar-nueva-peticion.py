import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net'
URL = '/pokedex/all'
#URL = 'https://pokemondb.net/pokedex/all'

if __name__ == "__main__":
    response = requests.get(DOMAIN + URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        #print(soup.prettify())
        
        table = soup.find('table', {'id': 'pokedex'})

        #print(table)

        for row in table.tbody.find_all('tr', limit=5):
            
            columns = row.find_all('td', limit=3)

            # Nombre de pokemon
            name = columns[1].a.text

            # print(name)

            # tipos de pokemon
            type = [ a.text for a in columns[2].find_all('a')]
            
            #print(*type)

            link = DOMAIN + columns[1].a['href']

            # print(link)
            pokemon_response = requests.get(link)
            if pokemon_response.status_code == 200:
                pokemon_content = pokemon_response.text

                pokemon_soup = BeautifulSoup(pokemon_content, 'html.parser')

                pokemon_table = pokemon_soup.find('table',                  class_='vitals-table')

                species = pokemon_table.tbody.find_all('tr')[2].td.text

                # print(species)
                print(name, '-',  *type, '-', species)