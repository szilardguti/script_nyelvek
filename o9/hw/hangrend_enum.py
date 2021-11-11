#!/usr/bin/env python3
from enum import Enum, auto

class Hangrend(Enum):
    MELY = auto()
    MAGAS = auto()
    VEGYES = auto()
    SEMMILYEN = auto()

def hangrend(s):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    magdb = melydb = 0
    
    for c in s:
        if c in MELY_MGHK:
            melydb += 1
        elif c in MAGAS_MGHK:
                magdb += 1
    
    if melydb > 0 and magdb == 0:
        return Hangrend.MELY
    elif magdb > 0 and melydb == 0:
        return Hangrend.MAGAS
    elif magdb > 0 and melydb > 0:
        return Hangrend.VEGYES
    else:
        return Hangrend.SEMMILYEN
      

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "nll"]
    for word in words:
        print(word, "->", hangrend(word).name)


if __name__ == "__main__":
    main()
