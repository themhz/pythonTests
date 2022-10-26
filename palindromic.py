def isPalindrome(str):
    if ''.join(str) == ''.join(reversed(str)):
        return True
    else:
        return False


def CreatePalindrome(string):
    # if isPalindrome(string):
    #     return [string, "String is palindrome", True]

    #remove one char and check if palindrome
    canBe = False
    for i in range(len(string)):
        tempString = string[0:i:1] + string[i+1:len(string):1]
        #print(tempString)
        canBe = isPalindrome(tempString)
        if canBe == True:
            print("The char that will be removed is " + str(string[i]) +" at index " + str(i))
            return canBe

    # remove two chars and check if palindrome
    for i in range(len(string)):
        tempString = string[0:i:1] + string[i+1:len(string):1]
        for j in range(len(tempString)):
            tempString2 = tempString[0:j:1] + tempString[j+1:len(tempString):1]
            canBe = isPalindrome(tempString2)
            if canBe == True:
                print("For string " + string + " the possible palindrome will be " + tempString2 + ". Char's that will be removed is " + str(string[i]) +" at index " + str(i) + " and " + str(string[j+1]) +" at index " + str(j+1))
                return canBe


    return canBe

string = "aaacaabta"
a = CreatePalindrome(string)

print(a)
# print(string[1:7:1])
# print(string[2:len(string):1])
# print(string[4])

