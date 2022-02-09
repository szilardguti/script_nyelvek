#!/usr/bin/env python3

import os


def main():
    url = "https://cataas.com/cat/says/hello%20world!"
    cmd = f"wget {url} -O kot.jpeg"
    print(cmd)
    
    os.system(cmd)
    
    

if __name__ == "__main__":
    main()
