from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # find

        # for element in soup.find_all('div'):
        for element in soup.find_all('div'):
            print(element, '\n')