#!/usr/bin/env python3
import string


TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""".strip()


def dekodol(s):
    megoldas = []
    kisbetu = string.ascii_lowercase
    nagybetu = string.ascii_uppercase
    for e in s:
        if e in kisbetu:
            megoldas.append(kisbetu[(kisbetu.find(e)+2)%26])
        else: 
            if e in nagybetu:
                megoldas.append(nagybetu[(nagybetu.find(e)+2)%26])
            else:
                megoldas.append(e)
    return ''.join(megoldas)


def main():
    print(dekodol(TEXT))


if __name__ == "__main__":
    main()
