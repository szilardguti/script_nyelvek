#!/usr/bin/env python3


def calculate_sum_three_or_five(upto):
    """
    calculate sum of the integers upto the input,that
    are dividable by 3 or 5
    """
    return sum([ i for i in range(upto) if i%3 == 0 or i%5 == 0])


def main():
    print(calculate_sum_three_or_five(1000))


if __name__ == "__main__":
    main()
