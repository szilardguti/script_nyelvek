#!/usr/bin/env python3


def main():
    while(True):    
        try:
            a, b = input("Kérem adjon meg két számot: ").split()
            a = int(a)
            b = int(b)
            if a < 0 or b < 0:
                raise ValueError
            break
        except ValueError:
            print("Kérem helyes értéket adjon meg")
        except KeyboardInterrupt:
            print("Feladat megszakítva!")
            break
        except Exception as e:
            print("Váratlan hiba")
            
    print("helyes")
    
    try:
        with open("input.txt") as f:

            print(f.read())

    except IOError:
        print("IO probléma")
    except EOFError:
        print("EOF?")

if __name__ == "__main__":
    main()
