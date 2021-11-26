#!/usr/bin/env python3

from typing import List
import urllib.request   


def find_planet_names(url_to_read: str) -> List[str]:
    searched_chars = [ "j", "s", "u", "n" ]

    result = []
    
    for line in urllib.request.urlopen(url_to_read):
        word = line.decode('utf-8').strip().split(',')[0].lower()
            
        corr_chars = []
            
        for i in range(len(word)):
            if  word[i] in searched_chars:
                  corr_chars.append((word[i], i))
                      
        if len(corr_chars) == len(searched_chars):
            if [tup[0] for tup in sorted(corr_chars, key= lambda t : t[1])] == searched_chars:
                result.append(word)
    return result
        

def main() -> None:
    for word in find_planet_names("https://raw.githubusercontent.com/jabbalaci/Programozas_1/main/datasets/DT2.csv"):
        print(word.replace("j", "J").replace("s", "S").replace("u", "U").replace("n", "N"))


if __name__ == "__main__":
    main()
