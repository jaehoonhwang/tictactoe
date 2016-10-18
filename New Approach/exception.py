#/usr/local/bin/python3

def main():
    a = [0 for x in range(0,5)]
    try:
        a[6] = 3
    except IndexError:
        print ("Hello")

    a = None

    print(typeCheck(a, None))



def evalGrid(grid, x):
    try:
        grid[x] == 0
    except IndexError:
        return False
    return True

def typeCheck(target, target_type):
    if isinstance(target, target_type):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
