#!/usr/bin/env python3


def find_palindroms(limit: int) -> int:
    result: int = 0
    for i in range(limit+1):
        if decimal_is_palindrom(i) and binary_is_palindrom(i):
            result = result + i
    return result


def decimal_is_palindrom(i: int) -> bool:
    return str(i) == str(i)[::-1]
    
    
def binary_is_palindrom(i: int) -> bool:
    return bin(i)[2:] == bin(i)[2:][::-1]
    

def main() -> None:
    print(find_palindroms(1000000))


if __name__ == "__main__":
    main()
