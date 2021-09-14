#!/usr/bin/env python3

PI = 3.14159 #globális konstansokat előre nagy betűvel


def hello(name, color, what):
    #Géza kék az ég!
    #name color what
    #v1
    #print("{0}, {1} az {2}! ({0})".format(name, color, what))
    #v2
    #print("{}, {} az {}!".format(name, color, what))
    #v3
    print("{nev}, {szin} az {obj}!".format(
        nev = name.capitalize(), szin=color, obj=what)
    )
    #v4
    #print(f"{name}, {color} az {what}!")



def main():
    hello("geza", "kek", "eg")
    print("-" * 30)
    hello("leonidas", "rohad", "dögkút")
    print("-.-" * 10)
    print(f"PI értéke: {PI}") 


if __name__ == "__main__":
    main()
