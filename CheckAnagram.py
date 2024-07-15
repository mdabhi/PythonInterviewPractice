# Write a program to check anagrams

def checkAnagram(str1, str2)-> bool:
    if len(str1)!=len(str2):
        return False
    
    st11 = str1.replace(" ","").lower()
    st12 = str2.replace(" ","").lower()
    
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)

    if sortedStr1 == sortedStr2:
        return True
    else:
        return False

str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")

result = checkAnagram(str1,str2)
if result == True:
    print(f'Entered 2 strings are anagrams!!')
else:
    print(f'Entered 2 strings are not anagrams!!')