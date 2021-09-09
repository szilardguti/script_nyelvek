#!/usr/bin/env python3

#A szkript az első két megadott parancssori argumentumot összekapcsolja egy, csupa kisbetűből álló, emaillé.


import sys


def make_email():
    s = (sys.argv[1], sys.argv[2])
    temp = '-'.join(s)
    return temp.lower() + "@testmail.com"
    

def main():
    email = make_email()
    print(email)

    
if __name__ == "__main__":
    main()
