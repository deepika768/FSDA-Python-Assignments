#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Assignment - 5
# --------------
# 

# ### 1. Write a Python Program to Find LCM?

# In[2]:


def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

compute_lcm(10,5)


# ### 2. Write a Python Program to Find HCF?

# In[ ]:


def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))


# ### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[1]:


dec = int(input("Enter an integer: "))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# ### 4. Write a Python Program To Find ASCII value of a character?

# In[21]:


c=input("enter a character: ")
print(ord(c))


# ### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[4]:


x=int(input("enter first number: "))
y=int(input("enter second number: "))

#summation
print("sum is :",x+y)
#subtraction
print("subtraction is:",x-y)
#multiplication
print("multiplication is:",x*y)
#divide
print("division is:",x//y)

