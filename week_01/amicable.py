
def findDivs(num, count): # number to find divisors of and empty list to store members of chain
    divisors = [] # initialize empty list to store divisors
    if num > 999999: # answer cannot contain numbers greater than 1000000 - if number is greater than a million...
        return 0 #...answer is unacceptable
    elif isPrime(num): # prime numbers will not have divisors
        return 0
    else: # if number is less than a million...
        count.append(num) # ...add number to chain list
        if count.count(num) > 1 and num != 0: # if there are 2 of the same number in the chain list that are not zero...
            return count #...return chain list
        elif count.count(num) > 1 and num == 0: # if chain list includes zero twice...
            return 0 #...not an amicable chain
        else: # still adding to chain list
            for i in range(1, int(num/2) + 1): # iterate through all possible divisors - greatest possible divisor must be half of number
                if num % i  == 0: # if iterated number divides equally into number...
                    divisors.append(i) #... adds iterated number to divisors list
                    if halfway(num, divisors): # checks if divisor list is half finished
                        finishDivisors(num, divisors) # completes divisor list without needing to iterate through all numbers
                        return findDivs(sum(divisors), count)
            return 0

def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
        else:
            return True

def halfway(num, list):
    if list[len(list) - 1] * list[len(list) - 2] == num:
        return True
    else:
        return False

def finishDivisors(num, list):
    indexCutoff = len(list) - 3
    for i in range(indexCutoff, 0, -1):
        list.append(int(num / list[i] ))
    return list


longestChain = []
longestChainLength = 0
chainNumbers = []

for i in range(10000, 20000):
    newChain = findDivs(i, [])
    if newChain != 0:
        if newChain[0] == newChain[len(newChain) - 1]:
            if longestChainLength < len(newChain):
                longestChainLength = len(newChain)
                longestChain = newChain

print("Longest Chain is: " + str(longestChain))
