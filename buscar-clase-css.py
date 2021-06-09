from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # opcion 1 atributo class
        #for element in soup.find_all(attrs = {'class': 'item-price'}):
            #if element.name == 'span':
                #print(element.text)

        # opcion 2 
            # for element in soup.find_all(class_= 'item-price price'):
        for element in soup.find_all(class_= 'item-price '):
            if element.name == 'span':
                print(element.text)