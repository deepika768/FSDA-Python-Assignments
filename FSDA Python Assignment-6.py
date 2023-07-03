#!/usr/bin/env python
# coding: utf-8

# # Programming Basic Assignment 6

# ### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

# In[1]:


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
x=int(input("enter number:"))
for i in range(x):
    print(fibonacci(i),end=' ')


# ### 2. Write a Python Program to Find Factorial of Number Using Recursion?

# In[1]:


def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
    
x=int(input("enter number:"))
print(factorial(x))
    
    


# ### 3. Write a Python Program to calculate your Body Mass Index?

# In[4]:


def bmi(weight,height):
    bmi=weight/(height*height)*100*100
    return bmi
w=float(input("enter weight in kg: "))
h=float(input("enter height in cm:"))

print("bmi is :",bmi(w,h))


# ### 4. Write a Python Program to calculate the natural logarithm of any number?

# In[5]:


import math

print(math.log(math.e))
print(math.log(1))
print(math.log(10))


# 
# ### 5. Write a Python Program for cube sum of first n natural numbers?
# 

# In[7]:


def cube_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(math.pow(i,3))
    print("cube sum of n natural numbers is :",sum)
    
n=int(input("enter nth number"))
cube_sum(n)

