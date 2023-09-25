# factorail of a number

""" def factorial(number):
    if (number == 1 or number == 0):
        return 1
    else:
        return number*factorial(number-1)"""
    
num = int(input("Enter a number = "))
#print(factorial(num))

# fibonacci series # example : 0 1 1 2 3 5 8

global count
count = 0

def fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1 or number == 1):
        return 1
    else:
        for i in range(number):
            if(count == 0):
                count = count + 1
            else:
                count = count + count
        #return number+fibonacci(number-1)

print(fibonacci(num))


#reverse a string 

def reverse(str1):
    if (len(str1)) ==0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0]
    
str1 = input("enter a string : ")
print(reverse(str1))


print(str1[1:])
print(str1[0])