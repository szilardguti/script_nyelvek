#!/usr/bin/env python3


class MyQueue:
    def __init__(self):
        self._bemenet_stack = Verem() #verem.py-ban található verem
        self._kimenet_stack = Verem()
        
        
    def append(self, value):
        if self._bemenet_stack.ures() and not self._kimenet_stack.ures():
            for i in range(self._kimenet_stack.meret()):
                self._bemenet_stack.betesz(self._kimenet_stack.kivesz())
                
        self._bemenet_stack.betesz(value)
    
    
    def popleft(self):
        if self._kimenet_stack.ures() and not self._bemenet_stack.ures():
            for i in range(self._bemenet_stack.meret()):
                self._kimenet_stack.betesz(self._bemenet_stack.kivesz())

        return self._kimenet_stack.kivesz()
        
        
    def is_empty(self):
        return not bool(self._bemenet_stack.meret() + self._kimenet_stack.meret())
        
        
    def size(self):
        return self._bemenet_stack.meret() + self._kimenet_stack.meret()
        
        
    def __str__(self):
        result = ""
        if self._kimenet_stack.ures():
            for i in range(self._bemenet_stack.meret()):
                self._kimenet_stack.betesz(self._bemenet_stack.kivesz())
        
        
        for i in range(self._kimenet_stack.meret()):
            temp = self._kimenet_stack.kivesz()
            result += str(temp) + ' '
            self._bemenet_stack.betesz(temp)

        return result + ']'
    
    
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
    q = MyQueue()           # üres sor létrehozása
    print(q)                # ]
    print(q.is_empty())     # True
    q.append(1)
    q.append(5)
    q.append('a')
    print(q.is_empty())     # False
    print(q.size())         # 3
    x = q.popleft()
    print(x)                # 1
    q.append(123)
    print(q)                # 5 'a' 123]
    q.popleft()
    q.popleft()
    q.popleft()
    x = q.popleft()
    print(q.is_empty())     # True
    print(x)                # None
   
    
if __name__ == "__main__":
    main()
