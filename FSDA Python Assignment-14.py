#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Assignment - 14
# ---------------------

# ### 1. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# In[6]:


class Iter:
    def __init__(self):
        pass
        
    def divide(self,n):
        for i in range(0,n):
            if i%7==0:
                print(i)
                
iter=Iter()
iter.divide(30)


# 
# ### 2. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

# In[8]:


input_line = input("Enter a string : ")

words_dict = {}

for word in input_line.split():
    words_dict[word] = words_dict.get(word,0) + 1

for key in sorted(words_dict):
  print("{} : {}".format(key,words_dict[key]))


# 
# ### 3. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# In[9]:


class Person(object):
    def getGender( self ):
        return "Unknown"
class Male( Person ):
    def getGender( self ):
        return "Male"
class Female( Person ):
    def getGender( self ):
        return "Female"
    


# 
# ### 4. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ['Play', "Love"] and the object is in ["Hockey","Football"].

# In[28]:


subjects=["I","You"]
verbs=["play","Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
    


# 
# ### 5. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"

# In[11]:


def reduceString(s, l):
    count = 1;
    steps = 0;
   
    # traverse in 
    # the string
    for i in range(1,l):
        # if adjacent 
        # characters are same
        if (s[i] is s[i - 1]):
            count += 1;
   
        else:
            # if same adjacent pairs 
            # are more than 1
            steps +=(int)(count / 2);
   
            count = 1;
        steps +=(int)(count / 2);
    return steps;
  
   
# Driver Code
s = "hello world!hello world!hello world!hello world!";
   
l = len(s);
print(reduceString(s, l));


# 
# ### 6. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# In[10]:


def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
 
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
 
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

