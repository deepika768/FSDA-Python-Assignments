#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_1
# -------------

# ### 1. Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# 

# In[3]:


a=int(input("enter first number: "))
b=int(input("enter second number: "))
#addition 
add=a+b
#division
if b==0:
    print("enter non zero integer: ")
else:
    div=a/b
    
print("addition is :",add)
print("division is :",div)


# ### 3. Write a Python program to find the area of a triangle?

# In[7]:


import math

s1=float(input("enter first side of a traingle:"))
s2=float(input("enter second side of a traingle:"))
s3=float(input("enter third side of a traingle:"))

s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)


# ### 4. Write a Python program to swap two variables?

# In[10]:


a=int(input("enter first number: "))
b=int(input("enter second number: "))

print(f"value of a and b before swapping is {a} and {b}")

#swapping without using any extra variable

a=a+b
b=a-b
a=a-b

print(f"value of a and b after swapping is {a} and {b}")

a=int(input("enter first number: "))
b=int(input("enter second number: "))

print(f"value of a and b before swapping is {a} and {b}")

#using third variable is 


c=a
a=b
b=c

print(f"value of a and b after swapping is {a} and {b}")


# ### 5. Write a Python program to generate a random number?
# 

# In[19]:


import random
a=random.random()
a

