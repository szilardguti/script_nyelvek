#!/usr/bin/env python3

from typing import List

def list_pages(input_pages: str) -> List[int]:
    result: List[int] = []
    
    for elem in input_pages.split(','):
        if '-' in elem:
            for i in range(int(elem[:elem.index('-')]), int(elem[-elem.index('-'):])+1):
                result.append(i)
        else:
            result.append(int(elem))
    return result
    
            
def main() -> None:
    inp: str = input("Adja meg a nyomtatni kívánt oldalakat: ")
    if inp and ' ' not in inp: 
        print(list_pages(inp))
    else:
        print("Rosszul adta meg az oldalakat!")


if __name__ == "__main__":
    main()
