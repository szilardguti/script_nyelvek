#!/usr/bin/env python3


def szamjegyek_osszege(ite):
    return sum( [ sum([ int(e) for e in n ]) for n in [ list(str(i)) for i in ite ] ]) 


def szamjegyek_osszege_atlathato(ite):
    osszeg = 0
    szamjegy_matrix = [ list(str(i)) for i in ite ]
    
    for sor in szamjegy_matrix:
        for char in sor:
            osszeg += int(char)
    return osszeg        
    

def main():
    print(szamjegyek_osszege( range(1, 100+1)))
    print(szamjegyek_osszege_atlathato( range(1, 100+1)))


if __name__ == "__main__":
    main()
