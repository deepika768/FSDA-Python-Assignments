#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to convert kilometers to miles?

# In[6]:


def km_to_miles(kilometers):
    miles = kilometers * 0.621371 
    return miles
 
# Test the function
kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles.")


# # 2.Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


celsius = float(input("Enter temperature in celsius: "))
 
fahrenheit = (celsius * 1.8) + 32
 
print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+" degree Fahrenheit.")


# # 3. Write a Python program to display calendar?

# In[5]:


import calendar
 
yy = 2023
mm = 8
 
# display the calendar
print(calendar.month(yy, mm))


# # 4. Write a Python program to solve quadratic equation?

# In[6]:


import cmath
 
a = 1
b = 4
c = 2
 
# calculating  the discriminant
dis = (b**2) - (4 * a*c)
 
# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
 
# printing the results
print('The roots are')
print(ans1)
print(ans2)


# # 5. Write a Python program to swap two variables without temp variable?

# In[3]:


a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("a = ",a," ","b = ",b)
a=a+b
b=a-b
a=a-b
print("a = ",a," ","b = ",b)

