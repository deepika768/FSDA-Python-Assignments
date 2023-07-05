#!/usr/bin/env python
# coding: utf-8

# # Python Basic Programming Assignment 8

# ### 1. Write a Python Program to Add Two Matrices?

# In[9]:


X = [[9,9,8],
    [4 ,0,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,9],
    [7,2,0]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)


# ### 2. Write a Python Program to Multiply Two Matrices?

# In[10]:


A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)


# ### 3. Write a Python Program to Transpose a Matrix?

# In[11]:


N = 4

 
def transpose(A,B):
 
 for i in range(N):
  for j in range(N):
   B[i][j] = A[j][i]
 
# driver code
A = [ [1, 1, 1, 1],
 [2, 2, 2, 2],
 [3, 3, 3, 3],
 [4, 4, 4, 4]]
 
 
B = A[:][:] # To store result
 
transpose(A, B)
 
print("Result matrix is")
for i in range(N):
 for j in range(N):
  print(B[i][j], " ", end='')
 print()


# 
# ### 4. Write a Python Program to Sort Words in Alphabetic Order?
# 

# In[32]:


def sort_alpha(s):
    w = s.split(" ")
    for i in range(len(w)):
        w[i] = w[i].lower()
    w.sort()
 
    # return the sorted words
    return ' '.join(w)
 
# Driver code
s = "hello i am deepika"
print(sort_alpha(s))


# ### 5. Write a Python Program to Remove Punctuation From a String?

# In[36]:


test_str = "hello welcome% to world @!of& programming :"
 
print("The original string is : " + test_str)
 
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, "")
 
print("The string after punctuation filter : " + test_str)

