from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # find

        # for element in soup.find_all('div'):
        for element in soup.find_all('div', {'title': 'buyer-info'}):
            #print(element, '\n')
            #div = element.find('div')

            div = element.find('div', {'title': 'buyer-name'})
            span = element.find('span')
            #print(div, span)
            print(div.text, span.get_text())