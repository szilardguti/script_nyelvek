#!/usr/bin/env python3


def palindrom(s):
    if (s == s[::-1]):
        return True
    else:
        return False
    
    
def main():
    teszt = input("Adjon meg egy szót: ")
    if(palindrom(teszt)):
        print("{0} egy palindróm".format(teszt))
    else:
        print("{0} nem egy palindróm".format(teszt))


if __name__ == "__main__":
    main()
