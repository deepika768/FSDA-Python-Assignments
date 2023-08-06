#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python Program to Find the Factorial of a Number?

# In[1]:


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n)*factorial(n-1)

n=int(input("enter a number: "))
print(factorial(n))


# # 2. Write a Python Program to Display the multiplication Table?

# In[2]:


def multiplication(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)
        
n=int(input("enter a number: "))
multiplication(n)


# # 3. Write a Python Program to Print the Fibonacci sequence?

# In[7]:


def fibonacci(n):
    f=1
    s=1
    print(f,s,end=' ')
    for i in range(2,n+1):
        t=f+s
        f=s
        s=t
        print(s,end=' ')
        
fibonacci(10)


# # 4. Write a Python Program to Check Armstrong Number?

# In[10]:


def armstrong(n):
    m=n
    p=0
    
    while n!=0:
        r=n%10
        p=p+(r*r*r)
        n=n//10
    if p==m:
        return "Armstrong number"
    else:
        return "Not a Armstrong number"
    
armstrong(153)
        
        


# # 5. Write a Python Program to Find Armstrong Number in an Interval?

# In[18]:


lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
    
    


# # 6. Write a Python Program to Find the Sum of Natural Numbers?

# In[14]:


def summation(n):
    s=0
    for i in range(1,n):
        s=s+i
    return s
summation(10)

