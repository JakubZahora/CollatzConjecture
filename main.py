def col(num: int):
    while num != 1:
        print("Number tested: %s" % num)
        if (num % 2) == 0:
            print("Even")
            num = num / 2
            print(num)
        else:
            num = 3*num + 1
            print("ODD")
            print(num)

def main():
    print("Hello World!")
    num = int(input("Please input a real, positive, whole number you would like to put into the algorithm: "))
    col(num)

if __name__ == "__main__":
    main()