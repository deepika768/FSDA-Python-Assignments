#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_3
# ----------------

# ### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


a=int(input("enter a integer: "))

if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("Zero")


# ### 2. Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


a=int(input("enter a integer: "))
if a%2==0:
    print("even number")
else:
    print("odd number")


# # 3. Write a Python Program to Check Leap Year?

# In[ ]:


year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year


# ### 4. Write a Python Program to Check Prime Number?

# In[17]:


n=int(input("enter a integer: "))
flag=False
if n==0 or n==1:
    flag=True
for j in range(2,n//2):
    if n%j==0:
        flag=True
        
if flag:
    print("Not a prime number")
    
else:
    print("prime number")


# ### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[20]:


for i in range(1,10000):
    flag=False
    if i==0 or i==1:
        flag=True
    for j in range(2,i//2+1):
        if i%j==0:
            flag=True
    if flag == False:
        print(i)
    


# In[ ]:




