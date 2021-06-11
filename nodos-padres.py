from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        span = soup.find('span', class_='item-price')

        # print(span.parent.parent.parent.parent.parent.name) result ->none
        # print(span.parent.parent.parent.parent.name)

        # parents 

        for parent in span.parents:
            print(parent.name)

