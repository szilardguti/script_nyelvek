#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


def main():
    with open("output.json", "w") as out, open("primes.json") as inp:
    
        result = []
        j = json.load(inp)
        
        for num in j:
            if str(num) == str(num)[::-1]:
                result.append(num)
                
        json.dump(result, out)
        
            
if __name__ == "__main__":
    main()
