#!/usr/bin/env python3


def binary_convert(s):
    return ''.join([ chr(int(word, 2)) for word in s.split()])
    

def main():
    with open("ocr1.txt", "r") as f, open("ocr2.txt", "r") as h:
    
        ocr1 = f.read()
        print("első szöveg:", binary_convert(ocr1))
        
        ocr2 = h.read()
        print("második szöveg:", binary_convert(ocr2))


if __name__ == "__main__":
    main()
