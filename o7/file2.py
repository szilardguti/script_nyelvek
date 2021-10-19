#!/usr/bin/env python3


def main():
    f = open("output.txt", "w")
    
    print("teszt", file = f)
    
    
    f.write("cc")
    f.write("dd\n")
        
    f.close()
    

if __name__ == "__main__":
    main()
