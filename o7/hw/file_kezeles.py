#!/usr/bin/env python3


def main():
    with open("string1.py", "r") as f, open("string1_clean.py","w") as w:
        w.write("#!/usr/bin/env python3\n")
        
        for lines in f:
            line = lines.strip()
            if line[:1] != '#':
                w.write(lines)
            

if __name__ == "__main__":
    main()
