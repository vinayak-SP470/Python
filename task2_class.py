import  re
class PythonBasics:

    def checkUniquChar(self,stringToCheck):
        list1 = []
        for i in stringToCheck:
            if i not in list1:
                list1.append(i);
                flag = True
            else:
                flag = False
                break
        if flag:
            print("The given string '" + stringToCheck + "' has all characters unique")
        else:
            print("The given string '" + stringToCheck + "' does not have all characters unique")

    def checkAnagram(self,firstString, secondString):
        firstStringList = list(firstString)
        flag = False
        for i in secondString:
            if i in firstStringList and len(firstString) == len(secondString):
                firstStringList.remove(i)
                flag = True
            else:
                flag = False
                print("The given strings '" + firstString + "' & '" + secondString + "' are not anagram")
                break
        if flag:
            print("The given strings '" + firstString + "' & '" + secondString + "' are anagram")

    def checkPalindrome(self,stringToCheck):
        punctuations = r'[^\w]'
        stringWithoutPunctuations = re.sub(punctuations, "", stringToCheck)
        lowercasedString = stringWithoutPunctuations.lower()
        if lowercasedString == lowercasedString[::-1]:
            print("'" + stringToCheck + "' is a palindrome")
        else:
            print("'" + stringToCheck + "' is not a palindrome")

    def findMissingNumber(self,listToCheck):
        sortedList = sorted(listToCheck)
        largestInteger = sortedList[-1]
        for i in range(1, largestInteger):
            if i not in listToCheck:
                print(str(i) + " is the missing number from the given list " + str(listToCheck))
                break

    def commonElements(self,firstList, secondList):
        duplicateElements = []
        for i in firstList:
            if i in secondList:
                if i not in duplicateElements:
                    duplicateElements.append(i)
        print(duplicateElements)

    def countOccurance(self,listOfTuple):
        dictonary = {}
        for key,value in listOfTuple:
            if key not in dictonary:
                dictonary[key]={}
            if value not in dictonary[key]:
                dictonary[key][value] = 1
            else:
                dictonary[key][value] += 1
        print(dictonary)

    def romanNumberToInteger(self,romanNumber):
        romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        previousValue = 0
        integer = 0
        reversedRomanNumber = romanNumber[::-1]
        for i in reversedRomanNumber:
            value = romanValues[i]
            if value >= previousValue:
                integer += value
            else:
                integer -= value
            previousValue = value
        print("Numerical value of Roman number " + romanNumber + " is " + str(integer))


obj1 = PythonBasics()

uniqueCharCheck = obj1.checkUniquChar("qwerty")
anagramCheck = obj1.checkAnagram("silent","listen")
palindromeCheck = obj1.checkPalindrome("A man, a plan, a canal, Panama!")
missingNUmber = obj1.findMissingNumber([3, 7, 1, 2, 8, 4, 6])
duplicateElements = obj1.commonElements([1, 2, 3, 4, 5],[3, 4, 5, 6, 7])
count = obj1.countOccurance([(1, 'a'), (2, 'b'), (1, 'c'), (2, 'a'), (3, 'b')])
numericValue = obj1.romanNumberToInteger("LVIII")