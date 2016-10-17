#/usr/local/bin/python3

def main():
    a = [0 for x in range(0,5)]
    try:
        a[5] = 3
    except IndexError:
        print ("Hello")

    try:
        a[3] = 3
    except IndexError:
        print ("Error")
    finally:
        a[3] = 4

    print (a[3])

if __name__ == "__main__":
    main()
