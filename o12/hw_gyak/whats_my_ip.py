#!/usr/bin/env python3

import json
import urllib.request

def main():
    r = urllib.request.urlopen("https://jsonip.com/").read().decode('utf-8')
    js = json.loads(r)
    
    print(js['ip'])
            
if __name__ == "__main__":
    main()
