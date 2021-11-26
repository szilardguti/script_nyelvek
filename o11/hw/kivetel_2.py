#!/usr/bin/env python3

def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("A program csak két számot fogad el, ennek megfelelően adja meg őket!")
            print('-' * 10)
        except (EOFError,KeyboardInterrupt):
            print()
            break
        except ZeroDivisionError:
            print("A nullával való osztás nincs értelmezve!")
            print('-' * 10)

#####

if __name__ == "__main__":
    main()
