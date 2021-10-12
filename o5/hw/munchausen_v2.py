#!/usr/bin/env python3


MAX_TIPP = 440 * 1000000


def M_numbers(upto):
    """returns every Münchausen number upto the input limit"""
    pre_calc = [0] + [i**i for i in range(1,10)]
    result = []
    i = 0
    while i < upto:
        digits = [int(c) for c in str(i)]
        max_num_len = len(str(pre_calc[max(digits)]))
        i_len = len(str(i))
        if  max_num_len > i_len or max_num_len < i_len :
            i += abs(max_num_len - i_len)
            continue
        elif sum([pre_calc[int(c)] for c in str(i)]) == i:
            result.append(i)
        i += 1
    return result


def main():
    #print(M_numbers(10000000))
    print(M_numbers(MAX_TIPP))


if __name__ == "__main__":
    main()
