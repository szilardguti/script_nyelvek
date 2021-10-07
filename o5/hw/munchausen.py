#!/usr/bin/env python3
#viszonylag lassú megoldás


MAX_TIPP = 440 * 1000000


def M_numbers(upto):
    return [ n for n in range(upto) if M_calc2(n) == n ]
    
    
def M_calc(n):
    sum = 0
    while(n > 0):
        digit = n % 10
        sum += digit ** digit
        n = n // 10
    return sum
    

def M_calc2(n):
    return sum( [int(c)**int(c) for c in str(n) if c != '0'])


def main():
    print(M_numbers(5000))


if __name__ == "__main__":
    main()
