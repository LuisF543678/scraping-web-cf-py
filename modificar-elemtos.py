from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})
        
        #print(div['title'])

        #print(div.get('titles', 'default'))

        div['id'] = 'item01'
        div['title'] = 'nuevo-titulo'

        div.div.string = 'CodigoFacilito'

        div.span.string = '$39.95'
        #print(div)
        print(soup.prettify())

