#!/usr/bin/env python3

def prim_palindrom(lower_limit: int) -> int:
    itest: int = lower_limit
    while(True):
        if is_palindrom(itest) and is_prime(itest):
            return itest
        else:
            itest = itest + 1


def is_palindrom(i: int) -> bool:
    return str(i) == str(i)[::-1]
    
    
def is_prime(n: int) -> bool:
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return False
        return True


def main() -> None:
    print(prim_palindrom(31))
    print(prim_palindrom(130))
    print(prim_palindrom(131))
    print(prim_palindrom(2001))
    

if __name__ == "__main__":
    main()
