#!/usr/bin/env python3

import requests
from PIL import Image
from io import BytesIO
import json


def main():
    #get a word from a random word API
    text_r = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    
    text = text_r.text.strip('[').strip(']').strip('"')
    
    url = f"https://cataas.com/cat/says/{text}"
    
    
    #get the image   
    r = requests.get(url)
    
    #display the image
    i = Image.open(BytesIO(r.content))
    i.show()    
    

if __name__ == "__main__":
    main()
