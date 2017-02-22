import sys
""" This program checks if 2 strings are anagrams
Eg. earth and heart are anagrams"""
def check_anagram(str1,str2):
    if(len(str1) != len(str2)):
        print "Not Anagrams"
    else:
        string1=[ord(i) for i in str1]
        string2=[ord(i) for i in str2]
        anagram= [False for i in string2 if i not in string1]
        if not anagram:
           print("Anagrams")
        else:
           print("Not Anagrams")
           
           
str1=raw_input("Enter first string: ")
str2=raw_input("Enter second string: ")
check_anagram(str1,str2)

"""if(set(string1).intersection(string2)): 
          print("Anagrams")
      else:
          print("Not Anagrams")"""
