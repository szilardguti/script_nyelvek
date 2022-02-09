#!/usr/bin/env python3

import json

def main():
    filename = "person.json"
    f = open(filename) #alapból olvasás módban
    
    d = json.load(f)
    print(d)
    
    f.close()
    

if __name__ == "__main__":
    main()
