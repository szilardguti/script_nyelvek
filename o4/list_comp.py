#!/usr/bin/env python3


def feladat1():
    ls = ['auto', 'villamos', 'metro']
    ljo = [ s.upper() + '!' for s in ls ]
    print(ljo)
    

def feladat2():
    ls = ['aladar', 'bela', 'cecil']
    ljo = [ s.capitalize() for s in ls ]
    print(ljo)
    


def feladat3():
    li = [ 0 for i in range(10) ]
    print(li)
    

def feladat4():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ljo = [ 2*i for i in li ]
    print(ljo)
    
    
def feladat5():
    lc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
    li = [ int(c) for c in lc ]
    print(li)
    
    
def feladat6():
    s = "1234567"
    li = [ int(s[i]) for i in range(len(s)) ]
    print(li)
    
    
def feladat7():
    ls = 'The quick brown fox jumps over the lazy dog'.split()
    li = [ len(s) for s in ls ]
    print(li)
    
    
def feladat8():
    ls = "python is an awesome language".split()
    result = [ ls[i][0] for i in range(len(ls)) ]
    print(result)
    
    
def feladat9():
    ls = 'The quick brown fox jumps over the lazy dog'.split()
    result = [ (s, len(s)) for s in ls ]
    print(result)
        

def feladat10():
    result = [ i for i in range(10) if i%2 == 0 ]
    print(result)
    
    
def feladat11():
    result = [ i**2 for i in range(20) if i**2%2 == 0 ]
    print(result)
    
    
def feladat12():
    result = [ i**2 for i in range(20) if str(i**2)[-1] == '4' ]
    print(result)
    
    
def feladat13():
    result = ''.join([ chr(i) for i in range(65, 65+26) ])
    print(result)
    
    
def feladat14():
    ls = [' apple ', ' banana ', ' kiwi']
    result = [ s.strip() for s in ls ]
    print(result)
        
        
def feladat15():
    lb = [1, 0, 1, 1, 0, 1, 0, 0]
    result = ''.join([ str(i) for i in lb ])
    print(result)    
    
        
def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()
    feladat9()
    feladat10()
    feladat11()
    feladat12()
    feladat13()
    feladat14()
    feladat15()

if __name__ == "__main__":
    main()
