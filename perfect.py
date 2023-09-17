#program to check a number is perfect square
def perfect(number):
    x = number**(1/2)
    z = x*x
    if number==z:
        print("It is a perfect square.")
    else:
        print("Not a perfect square")
number = int(input("Enter a number to be check : "))
perfect(number)
