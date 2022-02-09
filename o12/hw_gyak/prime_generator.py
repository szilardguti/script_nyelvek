#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
import json

def main():
    with open("primes.json", 'w') as file:
        data  = []
    
        n = 1_000_000
        lst = [True]*n                      
        for i in range(2,int(sqrt(n))+1):    
            if (lst[i]):                      
                for j in range(i*i, n, i):     
                    lst[j] = False
        for i in range(2,n):                
            if lst[i]:
                data.append(i)
                
        json.dump(data, file)
            
if __name__ == "__main__":
    main()
