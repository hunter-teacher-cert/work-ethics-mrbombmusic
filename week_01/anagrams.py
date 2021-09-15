import pprint, math

with open('words.txt') as p:
    lines = p.readlines()

lists = lines[0].split(',')
wordList = []
for i in range(len(lists)):
    wordList.append(lists[i].strip("\""))

alphabetical = []
for word in wordList:
    a = sorted(word)
    alphabetical.append("".join(a))

anagrams = {}
indexOffset = 1
for i in range(len(alphabetical)):
    sameLetters = []
    for w in range(indexOffset, len(alphabetical) - 1):
        if alphabetical[i] == alphabetical[w]:
            sameLetters.append(wordList[w])
    if len(sameLetters) > 0:
        sameLetters.append(wordList[i])
        anagrams.setdefault(alphabetical[i], sameLetters)
    indexOffset += 1

pprint.pprint(anagrams)

sqNums = {}

def duplicated(n):
    for i in range(len(n) - 1):
        if n.count(n[i]) > 1:
            return True
    return False


sqResultInt = []
sqResultStr = []
for i in range(111, 315): # 6 digits - 322, 1000, 9 digits - 11111, 31427, 8 digits - 3513, 9940, 5 digits - 111, 315
    n = i ** 2
    if isinstance(n, int):
        nums = list(str(n))
        if duplicated(nums):
            continue
        else:
            sqNums.setdefault(i, nums)
            sqResultInt.append("".join(nums))
            sqResultStr.append(nums)

longest = ['BROAD', 'BOARD']
word1 = list(str(longest[0]))
word2 = list(str(longest[1]))

def checkNumbers(index):
    letters = {}
    i = 0
    for item in word1:
        letters[item] = sqResultStr[index][i]
        i += 1
    # pprint.pprint(letters)
    wordNumbers = []
    for l in word2:
        n = letters.get(l)
        wordNumbers.append(n)
    word2Number = "".join(wordNumbers)
    if sqResultInt.count(str(word2Number)) == 1:
        print("word1 number is: " + str(sqResultInt[index]) + ", word2 number is " + word2Number )
        return word2Number
    else:
        pass

for i in range(len(sqResultStr)):
    checkNumbers(i)
