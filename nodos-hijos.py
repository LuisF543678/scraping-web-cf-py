from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        div = soup.find('div', {'title': 'buyer-info'})

        #print(div)
        #print(div.contents) # lista nodos

        #div_item = div.contents[1]
        #span_item = div.contents[3]

        #print(div_item.text, span_item.text)

        for  child in div.children:
            print(child)
        
        print(div.contents)
        print(div.children)