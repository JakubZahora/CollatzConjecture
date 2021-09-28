import matplotlib.pyplot as plt

def col(num: int):
    appx = 0
    x_list = [0]
    y_list = [num]
    while num != 1:
        print("Number tested: %s" % num)
        if (num % 2) == 0:
            print("Even")
            num = num / 2
            print(num)
            y_list.append(num)

        else:
            num = 3*num + 1
            print("ODD")
            print(num)
            y_list.append(num)
        appx += 1
        x_list.append(appx)

    return x_list, y_list
    

def main():
    print("Hello World!")
    #num = int(input("Please input a real, positive, whole number you would like to put into the algorithm: "))
    num = 1
    while num < 50:
        plt.xlabel("Iterations")
        plt.ylabel("Value")
        plt.title("Collatz Conjecture - Number: %s" % num)
        x, y = col(num)
        plt.plot(x, y, marker="o")
        plt.pause(1)
        num += 1
    plt.show()

if __name__ == "__main__":
    main()