#!/usr/bin/env python3

import requests
import json


def main():
    url = "https://jsonip.com/"
    r = requests.get(url)
    
    d = json.loads(r.text)

    print(json.loads(requests.get(url).text)['ip'])

if __name__ == "__main__":
    main()
