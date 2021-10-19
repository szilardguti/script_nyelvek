#!/usr/bin/env python3


def main():
    f = open("teszt", "r")
    
    sorok = f.readlines()
    print(sorok)
        
    f.close()
    

if __name__ == "__main__":
    main()
