#!/usr/bin/env python3


def feladat1():
    ls = ['auto', 'villamos', 'metro']
    result = [ s.upper() + '!' for s in ls ]
    return result
    

def feladat2():
    ls = ['aladar', 'bela', 'cecil']
    result = [ s.capitalize() for s in ls ]
    return result
    

def feladat3():
    li = [ 0 for i in range(10) ]
    return li
    

def feladat4():
    result = [ 2*i for i in range(1,10+1) ]
    return result
    
    
def feladat5():
    lc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
    result = [ int(c) for c in lc ]
    return result
    
    
def feladat6():
    s = "1234567"
    result = [ int(c) for c in s ]
    return result
    
    
def feladat7():
    ls = 'The quick brown fox jumps over the lazy dog'.split()
    result = [ len(s) for s in ls ]
    return result
    
    
def feladat8():
    ls = "python is an awesome language".split()
    result = [ s[0] for s in ls]
    return result
    
    
def feladat9():
    ls = 'The quick brown fox jumps over the lazy dog'.split()
    result = [ (s, len(s)) for s in ls ]
    return result
        

def feladat10():
    result = [ i for i in range(10) if i%2 == 0 ]
    return result
    
    
def feladat11():
    result = [ i**2 for i in range(20) if i**2%2 == 0 ]
    return result
    
    
def feladat12():
    result = [ i**2 for i in range(20) if str(i**2)[-1] == '4' ]
    return result
    
    
def feladat13():
    result = ''.join([ chr(i) for i in range(65, 65+26) ])
    return result
    
    
def feladat14():
    ls = [' apple ', ' banana ', ' kiwi']
    result = [ s.strip() for s in ls ]
    return result
        
        
def feladat15():
    lb = [1, 0, 1, 1, 0, 1, 0, 0]
    result = ''.join([ str(i) for i in lb ])
    return result    
    
        
def main():
    print(feladat1())
    print(feladat2())
    print(feladat3())
    print(feladat4())
    print(feladat5())
    print(feladat6())
    print(feladat7())
    print(feladat8())
    print(feladat9())
    print(feladat10())
    print(feladat11())
    print(feladat12())
    print(feladat13())
    print(feladat14())
    print(feladat15())


if __name__ == "__main__":
    main()
