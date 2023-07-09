#!/usr/bin/env python
# coding: utf-8

# # Python Basic Programming Assignment 11
# --------------------

# ### 1. Write a Python program to find words which are greater than given length k?

# In[23]:


def greater_words(string,k):
    s=string.split()
    s1=[]
    for word in s:
        if len(word)>k:
            s1.append(word)
    return s1

string="hello welcome to the world of programming , hope you are enjoying"
k=int(input("enter the length: "))
print(greater_words(string,k))
    


# ### 2. Write a Python program for removing i-th character from a string?

# In[5]:


test_str = "Hello welcome to the world of python programming" 
# Removing char at pos 3
new_str = ""
 
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
 

print ("The string after removal of i'th character : " + new_str)


# ### 3. Write a Python program to split and join a string?

# In[3]:


s ="Hello welcome to the world of python programming"
# print the string after split method
print(s.split(" "))
# print the string after join method
print("-".join(s.split()))


# ### 4. Write a Python to check if a given string is binary string or not?

# In[6]:


def check(string):
 
    # set function convert string
    # into set of characters .
    p = set(string)
 
    # declare set of '0', '1' .
    s = {'0', '1'}
 
    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")
        
string="10010"
check(string)


# ### 5. Write a Python program to find uncommon words from two Strings?

# In[2]:


def UncommonWords(A, B):
     
    # split the strings A and B into words and create sets
    setA = set(A.split())
    setB = set(B.split())
     
    # find the uncommon words in setA and setB and combine them
    uncommonWords = setA.difference(setB).union(setB.difference(setA))
     
    # convert the set to a list and return
    return list(uncommonWords)
 
# Driver Code
A = "Welcome to the world of programming"
B = "Welcome to the world of programming , hope you are enjoying"
 
# Print required answer
print(UncommonWords(A, B))


# ### 6. Write a Python to find all duplicate characters in string?

# In[4]:


def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print(" ".join(x))
 
# Driver program
input = 'Welcome to the world of programming , hope you are enjoying'
find_dup_char(input)


# ### 7. Write a Python Program to check if a string contains any special character?

# In[6]:


n = "Hello#%*how @*(are &! you"
n.split()
c = 0
s = '[@_!#$%^&*()<>?/\|}{~:]'  # special character set
for i in range(len(n)):
    # checking if any special character is present in given string or not
    if n[i] in s:
        c += 1   # if special character found then add 1 to the c
 
if c:
    print("string is not accepted")
else:
    print("string accepted")

