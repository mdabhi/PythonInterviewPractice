# write a program to find a substring in string

def checkSubstring(mainStr, subStr)-> bool:
    mainLength = len(mainStr)
    subLength = len(subStr)

    if subLength > mainLength: 
        return False
    
    mainStr = mainStr.lower()
    subStr = subStr.lower()

    for i in range(mainLength - subLength + 1):
        if mainStr[i:i+subLength] == subStr:
            print("Found")
            return True
        
    return False
        
str1 = input("Enter main string:")
str2 = input("Enter sub string:")

Found = checkSubstring(str1, str2)

if Found == True:
    print(f'The substring is a part of main string!!')
else:
    print(f'The substring is not a part of main string!!')