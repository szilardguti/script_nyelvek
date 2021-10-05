#!/usr/bin/env python3


def hangrend(s):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    magdb = melydb = 0
    
    for c in s:
        if c in MELY_MGHK:
            melydb += 1
        else:
            if c in MAGAS_MGHK:
                magdb += 1
    
    if melydb > 0 and magdb == 0:
        return "mély" # szebb lenne nevesített constanssal - MAGAS akár enumban
    if magdb > 0 and melydb == 0:
        return "magas"
    if magdb > 0 and melydb > 0:
        return "vegyes"
    else:
        return "semmilyen"
      

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "nll"]
    for word in words:
        print(word, "->", hangrend(word))


if __name__ == "__main__":
    main()
