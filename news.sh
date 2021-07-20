#! /bin/bash

# pwd
cd C:/Users/Userr/Desktop/pywscrp

source env/bin/activate

# ls
cd pywscrp/

python main.py

crontab -e 
    0 9 * * * /Users/Userr/Desktop/pywscrp

crontab -l
    0 9 * * * /Users/Userr/Desktop/pywscrp/news.sh
