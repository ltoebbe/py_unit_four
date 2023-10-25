
number = int(input("enter number: "))


def even_or_odd(number):
    if number % 2 == 0:
        return str(number) + " is an even number"
    if number % 2 == 1:
        return str(number) + " is an odd number"


def main():
    even_or_odd(number)
    print(even_or_odd(number))


if __name__ == '__main__':
    main()
