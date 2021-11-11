#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self._stack = []
        
        
    def ures(self):
        return not bool(len(self._stack))
    
    
    def betesz(self, value):
        self._stack.append(value)
        
        
    def kivesz(self):
        if self.ures():
            return None
        else:
            return self._stack.pop()
            
        
    def meret(self):
        return len(self._stack)
    
    
    def __str__(self):
        result = "["
        for e in self._stack:
            result += str(e) + ' '
        return result


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

if __name__ == "__main__":
    main()
