#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
""".strip()


def ekezet_leszedo(s):
     #TEXT.replace nem működött amikor egy key értéket adtam meg (?)
    d = {   'á' : 'a','é' : 'e','í' : 'i','ó' : 'o','ö' : 'o',
            'ő' : 'o','ú' : 'u','ü' : 'u','ű' : 'u','Á' : 'A',
            'É' : 'E','Í' : 'I','Ó' : 'O','Ö' : 'O','Ő' : 'O',
            'Ú' : 'U','Ü' : 'U','Ű' : 'U'
        }
    lc = []
    for c in s:
        lc.append(d.get(c, c))
    return ''.join(lc)


def main():
    print(ekezet_leszedo(TEXT))


if __name__ == "__main__":
    main()
