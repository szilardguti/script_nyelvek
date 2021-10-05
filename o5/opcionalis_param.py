#!/usr/bin/env python3


def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")
    

def main():
    greet("Béla")
    greet("Sanchez", greeting="Hola")
    greet("Jean", greeting="Bonjour")
    greet("Jóska")


if __name__ == "__main__":
    main()
