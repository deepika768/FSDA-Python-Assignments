#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_9
# ----------------

# ### 1. Write a Python program to check if the given number is a Disarium Number?

# In[1]:


import math
 
# Method to check whether a number is disarium or not
def check(n) :
 
    count_digits = len(str(n))
      
    # Compute sum of terms like digit multiplied by
    # power of position
    sum = 0  # Initialize sum of terms
    x = n
    while (x!=0) :
 
        # Get the rightmost digit
        r = x % 10
          
        # Sum the digits by powering according to
        # the positions
        sum = (int) (sum + math.pow(r, count_digits))
        count_digits = count_digits - 1
        x = x//10
        
    # If sum is same as number, then number is
    if sum == n :
        return 1
    else :
        return 0
       
# Driver method
n = 135
if (check(n) == 1) :
    print ("Disarium Number")
else :
    print("Not a disarium number")


# ### 2. Write a Python program to print all disarium numbers between 1 to 100?

# In[1]:


import math

def print_all_disarium_nos():
    
    for i in range(100):
        sum=0
        l=len(str(i))
        j=i
        while j!=0:
            
            r=j%10
            sum=(int)(sum+math.pow(r,l))
            l=l-1
            j=j//10
        if i==sum:
            print(i)
            
print_all_disarium_nos()
    


# ### 3. Write a Python program to check if the given number is Happy Number?

# In[2]:


def numSquareSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;
 
# method return true if
# n is Happy number
def isHappynumber(n):
 
    # initialize slow
    # and fast by n
    slow = n;
    fast = n;
    while(True):
         
        # move slow number
        # by one iteration
        slow = numSquareSum(slow);
 
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;
    return (slow == 1);
 
# Driver Code
n = 13;
if (isHappynumber(n)):
    print(n , "is a Happy number");
else:
    print(n , "is not a Happy number");


# ### 4. Write a Python program to print all happy numbers between 1 and 100?

# In[1]:


def numSquareSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;


def isHappynumber(n):
 
    # initialize slow
    # and fast by n
    slow = n;
    fast = n;
    while(True):
         
        # move slow number
        # by one iteration
        slow = numSquareSum(slow);
 
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;
    return (slow == 1);

for i in range(1,101):
    if isHappynumber(i):
        print(i)
    


# ### 5. Write a Python program to determine whether the given number is a Harshad Number?

# In[1]:


def checkHarshad( n ) :
    sum = 0
    temp = n
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10
    # Return true if sum of
    # digits is multiple of n
    return n % sum == 0
 
# Driver Code
if(checkHarshad(12)) : print("Yes")
else : print ("No")
 
if (checkHarshad(15)) : print("Yes")
else : print ("No")


# ### 6. Write a Python program to print all pronic numbers between 1 and 100?

# In[3]:


def isPronicNumber(num):
    flag = False;
    for j in range(1, num+1):
        #Checks for pronic number by multiplying consecutive numbers  
        if((j*(j+1)) == num):
            flag = True;
            break;
    return flag;
#Displays pronic numbers between 1 and 100  
print("Pronic numbers between 1 and 100: ")
for i in range(1, 101):
    if(isPronicNumber(i)):
        print(i)
        print(" ")

