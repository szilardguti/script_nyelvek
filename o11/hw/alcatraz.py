#!/usr/bin/env python3

from typing import List


def alcatraz_doors(door_count: int) -> List[int]:
    ldoor = [ 0 for i in range(door_count) ]
    for i in range(door_count):
        for j in range(door_count):
            if (j+1) % (i+1) == 0:
                if ldoor[j] == 0:
                    ldoor[j] = 1
                else:
                    ldoor[j] = 0

    return [ i+1 for i in range(door_count) if ldoor[i] == 1 ]
    
    
def main() -> None:
    print(', '.join([ str(i) for i in alcatraz_doors(600)]))
    



if __name__ == "__main__":
    main()
