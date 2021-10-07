#!/usr/bin/env python3


MAX_TIPP = 440 * 1000000



def M_numbers(upto):
    pre_calc = [0] + [i**i for i in range(1,10)]
    result = []
    for i in range(upto):
        digits = [int(c) for c in str(i)]
        if len(str(pre_calc[max(digits)])) > len(str(i)):
            continue
        elif sum([pre_calc[int(c)] for c in str(i)]) == i:
            result.append(i)
    return result


def main():
    print(M_numbers(MAX_TIPP))


if __name__ == "__main__":
    main()
