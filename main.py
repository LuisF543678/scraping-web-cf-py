import requests

URL ="https://econpy.pythonanywhere.com/ex/001.html"

if __name__ == '__main__':

    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text 
        #print(content)
        #with open('econpy.html', 'w+') as file:
        #    file.write(content)

      
        regexa = '<div title="buyer-name">'
        regexb = '</div>'
        for line in content.split('\n'):
            
            if regexa in line:
                #print(line)

                start = line.find(regexa) + len(regexa)
                end = line.find(regexb)
                title = line[start:end]
                print(title)

