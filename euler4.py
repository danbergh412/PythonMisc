import sys

def isPalindrome(number):
    strNum = str(number)

    f = 0
    l = len(strNum) - 1

    while (f < len(strNum)/2):
        if (strNum[f] != strNum[l]):
            return False
        f+=1
        l-=1
    return True

largest = 0
for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        product = num1 * num2
        if isPalindrome(product) and product > largest:
            largest = product

print(largest)
