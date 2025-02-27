# Program to check if two strings are anagrams using sorted() 

str1 = input('Enter string 1: ').lower()
str2 = input('Enter string 2: ').lower()

if (len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if (sorted_str1 == sorted_str2):
        print(str1 + "and" + str2 + "are anagram. ")
    else:
        print(str1 + "and" + str2 + "are not anagram.")
    
else:
    print(str1 + "and" + str2 + "are not anagram.")