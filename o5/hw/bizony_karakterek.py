#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    returns a string that contains the characters, which can be found in the
    second parameter of the function
    can return empty string as well
    """
    
    return ''.join([c for c in text if c in chars])


def main():
    print(valid("Barking"))                               #-> "B"
    print(valid("KL754", "0123456789"))                   #-> "754"
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))    #-> ""
    print(valid("Teszt Elek vagyOK, Jó éjszakát"))
    print(valid("Null", ""))
    

if __name__ == "__main__":
    main()
