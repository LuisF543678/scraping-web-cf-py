from bs4 import BeautifulSoup
if __name__ == "__main__":

    with open('econpy.html', 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        a = soup.new_tag('a', href='www.codigofacilito.com', target='_blank')
        a.string = 'Link a la plataforma'
        div = soup.new_tag('div', id='item01', title='item-data')
        #div['new-attrs'] = 'new_attrs'

        # Insertar al final de la lista
        div.append('\n')
        div.append(a)
        div.append('\n')
        
        #print(div)
        #print(div.contents)
        #print(a)

        # soup.body.append(div)

        # Insertar un nuevo nodo al principio
        soup.body.insert(1, div)    # contents
        print(soup.prettify())
