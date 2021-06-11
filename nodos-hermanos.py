from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        #div = soup.find('div', {'title': 'buyer-name'})

        div = soup.find('div', string='Carson Busses')

        # next_sibling
        # previous _subling

        #print(div.previous_sibling.previous_sibling)

        # next_siblings
        # previous_siblings

        # for element in div.previous_siblings: 
        for element in div.next_siblings:
            print(element)

