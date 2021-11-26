#!/usr/bin/env python3
from typing import List

data = [ 
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)
    ]
    
    
lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    
    
matrixi =[ [2,6],[1,3],[5,4] ]

    
def my_func1(t: tuple) -> int:
    return t[-1]
    

def my_func2(s: str) -> int:
    return int(s.split(':')[0])
    
    
def my_func3(sor: List[int]) -> int:
    return sor[1]
    

def main():
    # rendezés az utolsó oszlop szerint (data)
    print(sorted(data, key=my_func1))
    print(sorted(data, key=lambda lt : lt[-1] ))
    
    #rendezés UserID szerint (lst)
    print(sorted(lst, key=lambda s : int(s.split(':')[0]) ,reverse=True))
    print(sorted(lst, key=my_func2 ,reverse=True))

    #a mátrix második sora alapján (matrixi)
    print(sorted(matrixi, key=lambda sor : sor[1]))
    print(sorted(matrixi, key=my_func3))


if __name__ == "__main__":
    main()
