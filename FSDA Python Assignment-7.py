#!/usr/bin/env python
# coding: utf-8

# ## Programming Basic Assignment 7

# ### 1. Write a Python Program to find sum of array?

# In[1]:


l1=[3,4,6,8,7]
s=0

for i in l1:
    s=s+i
print(s)


# ### 2. Write a Python Program to find largest element in an array?

# In[3]:


l1=[3,4,6,78,4,6]
max=l1[0]

for i in l1:
    if i>=max:
        max=i
print("maximum of all elements in array is: ",max)



# ### 3. Write a Python Program for array rotation?

# In[4]:


# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))


# ### 4. Write a Python Program to Split the array and add the first part to the end?

# In[6]:


def splitArr(a, n, k):
    b = a[:k]
    return (a[k::]+b[::])
 
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')


# ### 5. Write a Python Program to check if given array is Monotonic?

# In[7]:


def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False

A = [6, 5, 4, 4]
 
# Print required result
print(isMonotonic(A))

