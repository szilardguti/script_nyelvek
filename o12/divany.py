#!/usr/bin/env python3

import requests
from time import sleep


def main():
    url = "https://divany.hu/offline/2016/03/07/dontsuk_el_meno_vagy_ciki_az_ovtaska/?p=&meno=1&posztbol=1"
    
    for i in range(10):
        r = requests.get(url)
        html = r.text
        
        sleep(1)
        print('.', end='', flush = True)
    print()
    

if __name__ == "__main__":
    main()
