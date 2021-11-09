#!/usr/bin/env python3


class Bag:
    def __init__(self):
        self._data = []
        
    
    def add(self, value):
        self._data.append(value)
    
    
    def add_twice(self, value):
        self.add(value)
        self.add(value)
        
    
    def __str__(self):
        return "Bag((" + str(self._data).strip('[').strip(']') +"))"
    
    
    def __bool__(self):
        return bool(len(self._data))
        

def main():
    b = Bag()
    if b:
        print("A bag nem üres!")
        
    b.add(5)
    b.add(3)
    b.add("string")
    print(b)
    
    b.add_twice(42)
    print(b)
    
    if b:
        print("A bag nem üres!")
    

if __name__ == "__main__":
    main()
