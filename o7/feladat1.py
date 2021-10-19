#!/usr/bin/env python3


def main():
    f = open("teszt", "r")
    w = open("output.txt", "w")
    
    for lines in f:
        w.write(lines)
    
    f.close()
    w.close()
    

if __name__ == "__main__":
    main()
