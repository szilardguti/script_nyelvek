#!/usr/bin/env python3


def draw_queens(li):
    print('+' + '-'*17 + '+')
    for i in range(7, 0-1, -1):
        print('| ', end='')
        Q_index = li.index(i)
        for j in range(8):
            if j == Q_index:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print('|')
    print('+' + '-'*17 + '+')


def main():
    li = [0,4,7,5,2,6,1,3]
    print(li)
    draw_queens(li)
    
    
    li = [7,3,0,2,5,1,6,4]
    print(li)
    draw_queens(li)


if __name__ == "__main__":
    main()
