#!/usr/bin/env python
# coding: utf-8

# # Python Basic Programming Assignment 12
# -------------

# ### 1. Write a Python program to Extract Unique values dictionary values?

# In[1]:


test_dict = {'gfg' : [5, 6, 7, 8],
'is' : [10, 11, 7, 5],
'best' : [6, 12, 10, 8],
'for' : [1, 2, 5]}
 
#printing original dictionary
print("The original dictionary is : " + str(test_dict))

result = list(set(sum(test_dict.values(), [])))
 
#printing result
print("The unique values list is : " + str(result))


# ### 2. Write a Python program to find the sum of all items in a dictionary?

# In[2]:


def returnSum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 
 
# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# ### 3. Write a Python program to Merging two Dictionaries?

# In[5]:


def Merge(dict1, dict2):
    return(dict2.update(dict1))
 
 
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This returns None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)


# ### 4. Write a Python program to convert key-values list to flat dictionary?

# In[7]:


test_dict = {'month' : [1, 2, 3],
            'name' : ['Jan', 'Feb', 'March']}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Convert key-values list to flat dictionary
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict
for i in range(0,len(a)):
    d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))


# ### 5. Write a Python program to insertion at the beginning in OrderedDict?

# In[9]:


from collections import OrderedDict
 
# Initialising ordered_dict
iniordered_dict = OrderedDict([('akshay', '1'), ('John', '2')])
 
# Inserting items in starting of dict
iniordered_dict.update({'kitty': '3'})
iniordered_dict.move_to_end('kitty', last=False)
 
# Printing result
print("Resultant Dictionary : "+str(iniordered_dict))


# ### 6. Write a Python program to check order of character in string using OrderedDict()?

# In[11]:


from collections import OrderedDict
 
def checkOrder(input, pattern):
     
    # create empty OrderedDict
    # output will be like {'a': None,'b': None, 'c': None}
    dict = OrderedDict.fromkeys(input)
 
    # traverse generated OrderedDict parallel with
    # pattern string to check if order of characters
    # are same or not
    ptrlen = 0
    for key,value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1
         
        # check if we have traverse complete
        # pattern string
        if (ptrlen == (len(pattern))):
            return 'true'
 
    # if we come out from for loop that means
    # order was mismatched
    return 'false'
 
# Driver program
if __name__ == "__main__":
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern))


# ### 7. Write a Python program to sort Python Dictionaries by Key or Value?

# In[12]:


from collections import OrderedDict
 
dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

