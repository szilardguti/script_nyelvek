#!/usr/bin/env python3

from typing import List


def find_possible_winning_nums(sumi: int, product: int) -> List[int] :
    for w1 in range(1,42):
        for w2 in range(w1+1, 43):
            for w3 in range(w2+1, 44):
                for w4 in range(w3+1, 45):
                    for w5 in range(w4+1, 46):        
                        w6 = sumi - w1 - w2 - w3 - w4 - w5
                        if w1 + w2 + w3 + w4 + w5 + w6 == sumi and w1 * w2 * w3 * w4 * w5 * w6 == product:
                            return [ w1, w2, w3, w4, w5, w6 ]


def main() -> None:
    print("Lehetséges számok:", ', '.join([ str(i) for i in find_possible_winning_nums(90, 996300)]))
    

if __name__ == "__main__":
    main()
