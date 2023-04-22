field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# def show():
#     print(f"  0 1 2")
#     for i in range(3):
#         # print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
#         row_info  = " ".join(field[i])
#         print(f"{i} {row_info}")

def show():
    print()
    print("    | 0 | 1 | 2 |")
    print("  ---------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ---------------")
    print()

def ask(): # проверка на координату и занятость клетки
    while True:
        x, y = map(int, input("Enter x and y: ").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print('cell is full')
        else:
            print("no such coordinate")

num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print('ходит крестик')
    else:
        print('ходит нолик')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if num == 9:
        break
        print('НИЧЬЯ')

    
 







