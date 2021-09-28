#!/usr/bin/env python3


def XOR(var1, var2):
    return ((bool(var1) and not bool(var2)) or (not bool(var1) and bool(var2)))


def main():
    str1 = "python"
    str2 = None
    print("str példa:", XOR(str1, str2))
    
    int1 = 0
    int2 = 42
    print("int példa:", XOR(int1, int2))
    
    print("ellen példa:", XOR(int1, str2), '|', XOR(int2, str1))


if __name__ == "__main__":
    main()
