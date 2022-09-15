def show():
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(area):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while 1:
        value = input("Введите число:").split()
        
        if len(value) != 2:
            print(" Введите два числа! ")
            continue
        
        x, y = value
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        
        x, y = int(x), int(y)
        
        if (0 > x or x > 2) or (0 > y or  y > 2):
            print(" Числа вне диапазона! ")
            continue
        
        if area[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y

def condition():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for part in win:
        sign = []
        for a in part:
            sign.append(area[a[0]][a[1]])
        if sign == ["X", "X", "X"]:
            print("-- Win X --")
            return True
        if sign == ["0", "0", "0"]:
            print("-- Win 0 --")
            return True
    return False

area = [[" "] * 3 for i in range(3)]
count = 0
while 1:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    x, y = ask()
    
    if count % 2 == 1:
        area[x][y] = "X"
    else:
        area[x][y] = "0"
    
    if condition():
        break
    
    if count == 9:
        print("-- Draw --")
        break