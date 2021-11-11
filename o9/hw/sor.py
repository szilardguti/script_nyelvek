#!/usr/bin/env python3


class Sor:
    def __init__(self):
        self._queue = []
        
    def ures(self):
        return not bool(len(self._queue))
    
    
    def betesz(self, value):
        self._queue.append(value)
        
        
    def kivesz(self):
        if self.ures():
            return None
        else:
            return self._queue.pop(0)
            
        
    def meret(self):
        return len(self._queue)
    
    
    def __str__(self):
        result = ""
        for e in self._queue:
            result += str(e) + ' '
        return result + ']'


def main():
    s = Sor()      # üres sor létrehozása
    print(s)         # ]
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # 1 4 5]
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # 4 5]
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None (jelezzük pl. így, hogy üres sorból akarunk kivenni)


if __name__ == "__main__":
    main()
