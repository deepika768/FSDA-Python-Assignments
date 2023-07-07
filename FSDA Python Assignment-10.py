#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Assignment 10

# ### 1. Write a Python program to find sum of elements in list?

# In[5]:


def sum_list(l):
    s=0
    for i in l:
        s=s+i
    return s

#driver code
l=[3,6,9,12,17,20]
print(sum_list(l))


# ### 2. Write a Python program to  Multiply all numbers in the list?

# In[2]:


def multiply_list(l):
    mul=1
    for i in l:
        mul=mul*i
    return mul

#driver code
l=[3,6,9,12,17,20]
print(multiply_list(l))


# ### 3. Write a Python program to find smallest number in a list?

# In[4]:


def small_num(l):
    min=l[0]
    for i in range(1,len(l)):
        if l[i]<min:
            min=l[i]
        else:
            min
    return min

#driver code
l=[1,5,2,7,4]
print("smallest number in list is :",small_num(l))


# ### 4. Write a Python program to find largest number in a list?

# In[7]:


def largest_num(l):
    max=l[0]
    for i in range(1,len(l)):
        if l[i]>max:
            max=l[i]
        else:
            max
    return max

#driver code
l=[1,5,2,7,4]
print("largest number in list is  :",largest_num(l))


# ### 5. Write a Python program to find second largest number in a list?

# In[18]:


l=[3,5,4,1,6,7]
l.sort(reverse=True)
print(l[1])


# ### 6. Write a Python program to find N largest elements from a list?

# In[20]:


l = [10,29,30,14,78,34]
n = 3
 
l.sort()
arr = []
 
while n:
    arr.append(l[-n])
    n -= 1
     
print(arr)


# ### 7. Write a Python program to print even numbers in a list?

# In[25]:


def even_num(l):
    l.sort()
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i) 
    return l1
            
l=[2,5,3,7,6,9,8,12,13]
print(even_num(l))


# ### 8. Write a Python program to print odd numbers in a List?

# In[26]:


def odd_num(l):
    l.sort()
    l1=[]
    for i in l:
        if i%2!=0:
            l1.append(i) 
    return l1
            
l=[2,5,3,7,6,9,8,12,13]
print(odd_num(l))


# ### 9. Write a Python program to Remove empty List from List?

# In[28]:


l1= [5, 6, [], 3, [], [], 9,13,[]]
 
# printing original list
print("The original list is : " + str(l1))
 
# using list comprehension
res = [ele for ele in l1 if ele != []]
 
# printing result
print("List after empty list removal : " + str(res))


# ### 10. Write a Python program to Cloning or Copying a list?

# In[32]:


import copy
l=[6,4,6,2,3,0,9]
print("original list is :",l)
l1=copy.copy(l)
print("copied list is :",l1)


# ### 11. Write a Python program to Count occurrences of an element in a list?

# In[38]:


def countX(lst, x):
    return lst.count(x)
 
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

