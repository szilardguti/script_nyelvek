#!/usr/bin/env python3


import urllib.request
import json


def main():
    r = urllib.request.urlopen("https://www.reddit.com/r/earthporn/.json").read().decode()
    js = json.loads(r)
    
    kepek = js["data"]["children"]
    for kep in kepek:
        print(kep["data"]["title"], ':', kep["data"]["url"])


if __name__ == "__main__":
    main()
