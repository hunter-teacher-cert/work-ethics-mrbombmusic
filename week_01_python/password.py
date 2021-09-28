import pprint, copy

with open('passkey.txt') as p:
    lines = p.readlines()

digitsInPassword = []

for num in range(len(lines)):
    for digit in range(3):
        nextDigit = lines[num][digit]
        if nextDigit not in digitsInPassword:
            digitsInPassword.append(nextDigit)

def checkNextDigits(num, passcodes):
    digitsAfter = []
    containsDigit = False
    for digit in range(3):
        if containsDigit:
            digitsAfter.append(passcodes[digit])
        if passcodes[digit] == num:
            containsDigit = True
    return digitsAfter


def followingDigits(digit, lines):
    digitsAfter = []
    for i in range(len(lines)):
        num = lines[i][0:3]
        nextDigit = checkNextDigits(digit, num)
        if len(nextDigit) == 1 and nextDigit[0] not in digitsAfter:
            digitsAfter.append(nextDigit[0])
        elif len(nextDigit) > 1:
                for i in range(len(nextDigit)):
                    if nextDigit[i] not in digitsAfter:
                        digitsAfter.append(nextDigit[i])
        else:
            continue
    return digitsAfter

afterDigits = {}
for n in digitsInPassword:
    following = followingDigits(n, lines)
    afterDigits.setdefault(n, following)
pprint.pprint(afterDigits)

def getLength(key):
    a = len(afterDigits.get(key))
    return a

longest = 0
longestKey = ''
password = ''
digitsCopy = copy.copy(digitsInPassword)

while len(digitsCopy) != 0:
    for n in digitsCopy:
        length = getLength(n)
        if length > longest:
            longest = length
            longestKey = n
    password = password + longestKey
    del afterDigits[longestKey]
    digitsCopy.remove(longestKey)
    if len(digitsCopy) > 1:
        longest = 0
        longestKey = ''
    else:
        password = password + digitsCopy[0]
        break

print(password)

# pprint.pprint(afterDigits)
# print(digitsCopy)
# print("length of list is " + str(len(digitsCopy)))
# print(longestKey + " has the longest length of " + str(longest))
