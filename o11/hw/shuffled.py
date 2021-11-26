#!/usr/bin/env python3
import random
from typing import List


def shuffled(li: List[int]) -> List[int]:
    temp = [elem for elem in li]
    random.shuffle(temp)
    return temp
    

def main() -> None:
    li = [1,2,3,4,5]
    ls = shuffled(li)
    x = shuffled(li)[0]
    print("Li: ", li)
    print("Ls: ", ls)
    print(f"{x = }")


if __name__ == "__main__":
    main()
