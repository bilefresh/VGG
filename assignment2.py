"""
Created by Bilesanmi Faruk
"""
#Question 1

def check_string(word):
    uppers = [l for l in word if l.isupper()]
    lowers = [l for l in word if l.islower()]
    print("No. of Upper case characters :",len(uppers))
    print("No. of Lower case characters :",len(lowers))

#check_string('The quick Brow Fox')

#Question 2

def check_max(*numbers):
    try:
        print("The maximum number is :", max(numbers))
    except TypeError:
        print("Please input only numbers")

#check_max(3,99.8,80)

#Question 3
def check_prime(number):
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if number% i == 0:
                print("This is not a prime number")
                break
            else:
                print("This is a prime number")
                break

#check_prime(3)
