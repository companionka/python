def factorial (x):
    if x == 1:
        return 1
    else:
        while x > 0:
            x = x * factorial (x - 1)
            return x
n = factorial (int(raw_input("Enter a number:")))
print n