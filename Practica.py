#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


4 % 2


# In[3]:


11 % 5


# In[4]:


11 // 5


# In[5]:


11 / 5


# In[6]:


bin(10)


# In[7]:


x=5


# In[8]:


y=x


# In[9]:


print(y)


# In[10]:


x=+-3


# In[11]:


prin(x)


# In[12]:


print(x)


# In[13]:


print(y)


# In[14]:


a = 24 
print(a)


# In[15]:


a + 2


# In[16]:


print(a)


# In[17]:


a += 2
print(a)


# In[18]:


a -= 2
print(a)


# In[19]:


a *= 2 
print(a)


# In[20]:


3 == 2


# In[21]:


3 != 2


# In[22]:


b = 23 
print(b)


# In[23]:


20 < b < 31


# In[24]:


x = 3
(x < 5 ) or ( x == 3 )


# In[25]:


not ( x != 3 )


# In[26]:


1 in [1,2,3]


# In[27]:


a = [1,2,3]


# In[28]:


b = [1,2,3,4,5,6]


# In[29]:


a in b


# In[30]:


b = [[1,2,3],4]


# In[31]:


a in b


# In[32]:


a is b


# In[33]:


1 is 1


# In[2]:


message = 'what do you like?'
response = 'spam'


# In[35]:


len(message)


# In[36]:


response.upper()


# In[37]:


message.below()


# In[38]:


message.capitalize()


# In[39]:


message + response


# In[40]:


5 * message


# In[41]:


message [0]


# In[42]:


if ( x % 2 == 0 ):
    print('par')
    if not print( 'impar' ) 


# In[3]:


str.lower()


# In[4]:


str.lower(response)


# In[6]:


str.title()


# In[7]:


str.title(message)


# In[8]:


L=[2,3,5,7]


# In[9]:


2 in L


# In[10]:


2 not in L


# In[11]:


len(L)


# In[12]:


length(L)


# In[13]:


L.append(11)


# In[14]:


print(L)


# In[15]:


len(L)


# In[16]:


L + [13,17,19]


# In[17]:


print(L)


# In[18]:


L += [13,17,19]


# In[19]:


print(L)


# In[20]:


L -= [13,17,19]


# In[21]:


del L[5:8]


# In[22]:


print(L)


# In[23]:


L=[2,5,1,6,3,4]


# In[24]:


L.sort()


# In[25]:


L


# In[26]:


L=[0,20,17,14,2,5,7,3,1,9,19,13,15,6,10,4,11,8,16,12,18]


# In[27]:


L.sort()
L


# In[28]:


L=[0,3,22,4,17
  ]


# In[29]:


L.sort()


# In[30]:


L


# In[31]:


L=[2,3,5,7,11]


# In[32]:


L[0
 ]


# In[33]:


L[-1]


# In[34]:


l[-5]


# In[35]:


L[-5]


# In[36]:


L[-5]==L[0]


# In[37]:


L[0:3]


# In[38]:


L[-3:0]


# In[39]:


L[-5:-1]


# In[40]:


L[-3:]


# In[41]:


L[0:]


# In[42]:


L[::1]


# In[43]:


L[::2]


# In[44]:


L[::-1]


# In[45]:


L[0]=100
print(L)


# In[46]:


L[0:2]=[1,1]


# In[47]:


print(L)


# In[48]:


del L[0:1]


# In[49]:


print(L)


# In[50]:


L=[100,2,3,5,7,11]


# In[51]:


print(L)


# In[52]:


t = (1,2,3)
print(t)


# In[53]:


len.t()


# In[54]:


len(t)


# In[55]:


len(L)


# In[56]:


t[0]


# In[57]:


t.append(2)


# In[58]:


L.append(1,2,3)


# In[59]:


L += [1]
print(L
     )


# In[60]:


del L[5:7]


# In[61]:


print(L)


# In[62]:


t[0]=1


# In[63]:


x= 0.125


# In[64]:


x.as_integer_ratio()


# In[65]:


1/8


# In[66]:


numerator , denominator = x.as_integer_ratio()


# In[67]:


print( numerator / denominator )


# In[68]:


t[0:1
 ]


# In[69]:


t[2]


# In[70]:


numbers = {'one':1 , 'two':2 , 'three':3 }
print(numbers)


# In[71]:


numbers['one']


# In[72]:


numbers['one':'two']


# In[73]:


numbers[0,1]


# In[74]:


numbers['one':'three']


# In[75]:


numbers['ninety']=90


# In[76]:


print(numbers)


# In[77]:


numbers['four','eight']=[4,8]


# In[78]:


print(numbers)


# In[79]:


numbers['four','eight']=4,8


# In[80]:


print(numbers
     )


# In[81]:


del t[0]


# In[82]:


primes={2,3,5,7}
odds={1,3,5,7,9}


# In[83]:


primes[1]


# In[84]:


primes[0:1]


# In[85]:


primes.append(1)


# In[86]:


primes | odds 


# In[87]:


primes.union(odds)


# In[88]:


odds.union(primes)


# In[89]:


primes & odds


# In[90]:


primes.intersection(odds)


# In[91]:


primes - odds


# In[92]:


primes.difference(odds)


# In[93]:


primes ^ odds 


# In[94]:


primes.symetric_difference(odds)


# In[95]:


primes.symmetric_difference(odds)


# In[96]:


collections.namedtuple


# In[114]:


x = 22
if ( x % 2 == 0):
    print(x ,"es par")
elif ( x % 2 == 1):
    print(x , " es impar")
 


# In[116]:


x = -15
if x == 0: 
    print(x,'is zero')
elif x > 0:
    print(x,'is positive')
elif x < 0:
    print(x,'is negative')
else:
    print(x, 'is unlike anything ive ever seen..')


# In[118]:


for N in [1,2,3,4,5,6]:
    print(N, end=' ')


# In[119]:


for i in range(10):
    print(i, end= ' ')


# In[120]:


list(range(10))


# In[121]:


list(range(0,25,2))


# In[122]:


list(range(25,0,-2))


# In[2]:


list(range(0,11,1))


# In[4]:


i = 0 
while i < 10:
    print(i, end=' ')
    i += 1 


# In[7]:


for i in range(22):
       if i % 2 == 0:
           continue 
       print(i, end=' ')


# In[8]:


print(1,2,3, sep='...')


# In[9]:


def fibonnaci(N):
    L = []
    a, b = 0, 1
    while len(L) < N: 
        a, b = b, a + b 
        L.append(a)
    return L 


# In[10]:


fibonnaci(10)


# In[ ]:




