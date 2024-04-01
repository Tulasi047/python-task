str1=input("Enter the first string=")
str2=input("Enter the second string=")
if(sorted(str1)==sorted(str2)):
    print("Two strings are Anagrams.")
else:
    print("Two strings are not anagrams.")