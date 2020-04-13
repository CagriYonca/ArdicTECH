#!/usr/bin/env python
# coding: utf-8

# In[1]:


calculated_pisano_period = 217728000		# calculated from pisanoPeriod function
x = 100
n = pow(10, 15)
mod_value = 1307674368000 					# 15 factorial
result = 0


# In[2]:

# divide and conquer function to calculate huge exponential functions
def emod(a,b,c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        d = emod(a, b//2, c)
        return (d * d) % c
    else:
        return ((a % c) * emod(a, b - 1, c)) % c


# In[3]:

# this function calculates and returns pisano period for m value
def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous = current
        current = (previous + current) % m 
          
        if (previous == 0 and current == 1): 
            return i + 1


# In[29]:

"""
# calculated pisano period for mod_value once
pisanoPeriod = pisanoPeriod(mod_value)


# In[30]:


pisanoPeriod

"""
# In[5]:


def fibonacciModulo(n, m):
    result = []
    n = n % calculated_pisano_period
      
    previous, current = 0, 1
    result.append(0)
    for i in range(n-1): 
        previous = current
        current += previous
        result.append(current % m)
    return result 
#    return (current % m) 


# In[38]:

# calculated fibonacci modulo array once
fibModuloArray = fibonacciModulo(n, mod_value)


# In[37]:


for i in range(x):  # x = 100
    for j in range(n + 1):  # n = 10^15
        a = emod(i, j, mod_value)
        b = fibModuloArray[j % calculated_pisano_period]
        result += (a * b) % mod_value
print("Mod value is " , result % mod_value)
