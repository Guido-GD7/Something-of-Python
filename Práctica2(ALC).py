#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# Resolución de ejercicios:

# Calcular: $$
# 10! = \prod_{i=1}^{10} i
# $$

# In[5]:


producto = 1
for i in range(1,11):
    producto = producto * i
print(producto)


# In[6]:


#Como funciona la función anterior? Simple, definimos que producto es igual a 1. luego que multiplique producto(caso base=1) por i, donde i se mueve entre 1 y 10 (1<=i<11, ya que el intervalo no toma al 11).
#Es decir ----> producto(1)= 1*1, producto(2)= 1*2, producto(3)= 2*3, producto(4)=6*4, producto(5)=24*5, producto(6)=120*6, producto(7)=720*7, producto(8)=5040*8, producto(9)=40320*9, producto(10)= 362880*10=3628800=10!


# Evaluar: $$
# \sum_{i=1}^{15} \left(\sum_{j=5}^{20} \frac{1}{i+j+3}\right)
# $$

# In[7]:


#Sumatoria de una sumatoria. Debo primero calcular la sumatoria donde 5<=j<=20 y luego evaluar el resultado en la sumatoria donde 1<=i<=15.


# In[21]:


suma1= 0
for i in range(1,16):
    for j in range(5,21):
        suma1= suma1 + (1 / ( i + j + 3 ))
print(suma1)
    
   


# In[23]:


#Al final es mas sencillo de lo que pensaba. No fue necesario calcular la primera sumatoria por separado, a mano esto es posible y resultaria lo mas sencillo. Computacionalmente todavia no se si es posible realizar la primera sumatoria y mantener el caracter "i" fijo y luego evaluar dentro de los valores posibles de "i". En este caso se resuelve de una manera que resulta "natural"; es decir calculo la primera sumatoria tal cual esta expresada con el rango de "j" y a dicha operación le "coloco" el rango de "i" como se ve arriba. Conclusión, simplemente defini la suma "(1/(i+j+3))" y luego los rangos en orden, primero "j" luego "i".


# Calcular: $$\sum_{i=1}^{100} \frac{1}{i} \quad \text{y} \quad \sum_{i=1}^{100} \frac{1}{i^2}$$

# In[24]:


suma2=0
for i in range(1,101):
    suma2= suma2 + ( 1/i )
print(suma2)


# In[26]:


suma3=0
for i in range(1,101):
    suma3= suma3 + ( 1 / (i**2))
print(suma3)


# In[1]:


#Todos los resultados del ejercico que corresponde a "for" son correctos.


# ### Ejercicio
# - Contar cuántos número naturales entre 1 y 1000 inclusive hay tales que su cuadrado termina en 9.

# In[3]:


numNa=0
for i in range(1,1001):
    if(((i**2)-9) % 10 == 0):
        numNa= numNa + 1 
    else:
        numNa= numNa + 0 
print(numNa)

