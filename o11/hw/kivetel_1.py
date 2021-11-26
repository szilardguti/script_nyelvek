#!/usr/bin/env python3

# mycat.py
# a sima cat parancs ha nem találja a kapott argumentumot nem terminál
#   simán kiírja, hogy nincs olyan

import sys


def cat(fname):
    try:
        f = open(fname, 'r')
        text = f.read()
        print('---', fname)
        print(text)
        f.close()
    except FileNotFoundError:
        print(f"Warning: {fname} not found!\n")
    
#####

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        cat(arg)
