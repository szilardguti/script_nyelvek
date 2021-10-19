#!/usr/bin/env python3


def main():
    f = open("string1.py", "r")
    w = open("string1_clean.py", "w")
    
    for lines in f:
        if '#' not in lines:
            w.write(lines)
            
    f.close()
    w.close()
    

if __name__ == "__main__":
    main()
