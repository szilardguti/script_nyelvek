#!/usr/bin/env python3

from pygyak import get_page


def main():
    url = "https://www.python.org/"
    print(get_page(url))
    

if __name__ == "__main__":
    main()
