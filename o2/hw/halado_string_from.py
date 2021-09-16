#!/usr/bin/env python3


def main():
    n64_games = [ ("Super Mario 64", 1996, 94.42), 
                  ("The Legend of Zelda: Ocarina of Time", 1998, 99.32),
                  ("GoldenEye 007", 1997, 96.0535),
                  ("Mario Kart 64", 1996, 83.1337),
                  ("Donkey Kong 64", 1999, 90),
                  ("The Legend of Zelda: Majora's Mask", 2000, 95.1),
                  ("Banjo-Kazooie", 1998, 92.0003) ]


    print("{0:^40} {1:<20} {2:>20}".format("Játék neve", "Megjelenésének éve",
            "Metacritic pontszáma /100"))
    
    print("-"*100)
    
    for element in n64_games:
        print("{nev:^40} {kiadas:<20} {score:^20.2f}".format(nev=element[0],
                kiadas=element[1], score=element[2]))


if __name__ == "__main__":
    main()
