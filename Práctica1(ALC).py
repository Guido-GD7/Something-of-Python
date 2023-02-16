#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


A=np.array([[3,2,2],[-1,0,1],[-2,2,4]])


# In[3]:


print(A)


# In[4]:


print(A)


# In[5]:


B=np.array([[0,1,-1],[5,-2,1]])


# In[6]:


print(B)


# In[61]:


V=np.array([-1,2,1])


# In[8]:


print(V)


# In[9]:


#A continuación veremos la utilidad del comando "nombredematriz.shape" el cual devuelve una tupla, es decir (a,b), donde "a=número de filas" y "b=número de columnas" de la matriz correspondiente.


# In[10]:


A.shape


# In[11]:


B.shape


# In[12]:


#Es posible solicitar que nos devuelva solo el número de filas como de columnas, utilizando el siguiente comando "nombredematriz.shape[0]" (corresponde al numero de filas, primer elemento de la tupla solicitado con el 0) o, caso contrario, "nombredematriz.shape[1]" (solicitando unicamente el número de columnas)
#Resulta ser que en general python comienza a contar desde el 0. Por eso el primer elemento de la tupla (correspondiente a fila) se lo llama usando el "0".


# In[13]:


A.shape[0]


# In[14]:


A.shape[1]


# In[15]:


B.shape[0]


# In[16]:


B.shape[1]


# In[17]:


V.shape[0]


# In[18]:


V.shape[1]


# In[19]:


#Aclaracion: Cabe notar que cuando uno solicita la "forma(shape)" de un vector V, no obtendre como resultado el orden de tuplas anteriormente descripto. Es decir que si ejecuto "V.shape" ---> (3,) lo cual denota que posee 3 elementos mas no bien filas.


# In[20]:


#Matriz transpuesta "nombredematriz.T"


# In[21]:


A.T


# In[22]:


B.T


# In[23]:


print(A)


# In[24]:


print(B)


# In[25]:


print(A.T)


# In[26]:


print(B.T)


# In[27]:


V.T


# In[28]:


print(V.T)


# In[29]:


#No se puede trasponer un vector.


# In[30]:


#Resulta necesario aclarar que al trasponer la matriz, es decir por ejemplo "A.T" no estoy modificando la asignación previamente realizada para la matriz A. Ya que bien sabemos que python es un lenguaje de programación orientada a objetos, donde asignar "=" es la simple operación de apuntar. Las variables son punteros, es decir que al realizar la operación "A=2" estoy definiendo un puntero de nombre "A" que apunta a un cubo de memoria (memory bucket) el cual si posee el valor "2" guardado en él. Por lo tanto no cambio la asignación de "A" al trasponerla, sino que creo un nuevo array que es la matriz traspuesta. Veamoslo


# In[31]:


print(A)


# In[32]:


A.T


# In[33]:


print(A)


# In[34]:


#La matriz "A" no fue modificada.


# In[35]:


#Si utilizo el comando "np.diag(nombredematriz)" ----> obtengo la diagonal de la matriz "evaluada".


# In[36]:


np.diag(A)


# In[37]:


print(A)


# In[38]:


np.diag(B)


# In[39]:


print(B)


# In[40]:


#Que ocurrirá si utilizo el comando pero coloco un vector como argumento? Es decir ---> "np.diag(vector)". Obtengo como resultado una matriz cuya diagonal son los "componentes" del vector, y todos los demas a(ij) (donde i=filas j=columnas, denota el elemento que corresponde a cada lugar segun fila o columna) son "0" (ceros).


# In[41]:


np.diag(V)


# In[42]:


# Como se ha explicado.


# In[43]:


#El determinante de una matriz se calcula utilizando el siguiente comando "np.linalg.det(nombredematriz)"


# In[44]:


np.linalg.det(A)


# In[45]:


np.linalg.det(B) #Error porque solo es posible calcular el determinante de una matriz cuadrada. Es decir M ∈ K^nxn


# In[46]:


B.shape


# In[48]:


#Si la matriz tiene inversa(es inversible) la calculamos de la siguiente manera ----> "np.linalg.inv(nombredematriz)"


# In[49]:


np.linalg.inv(A)


# In[50]:


#Como B no es una matriz cuadrada no es inversible, obtendremos un error si queremos calcular su inversa.


# In[51]:


np.linalg.inv(B)


# In[52]:


# La norma de una matriz o de un vector se obtiene utilizando el siguiente comando ---> "np.linalg.norm(nombredematriz)"


# In[53]:


np.linalg.norm(V)


# In[54]:


np.linalg.norm(A)


# In[55]:


#Si queremos crear una copia de una matriz o de un vector, lo hacemos añadiendo "nombredematriz/vectorqueserácopia=nombredematriz/vectorquecopiare.copy()"" En este caso no es necesario colocar algo en el argumento.


# In[56]:


C=A.copy()


# In[57]:


print(c)


# In[58]:


print(C)


# In[59]:


print(A)


# In[60]:


#Como se observa C es una copia de la matriz A.


# In[61]:


# Con la función "np.eye(n)"" podemos definir la matriz identidad de tamaño  𝑛×𝑛 . Por ejemplo, con np.eye(4) obtenemos la matriz identidad de  4×4 :


# In[62]:


np.eye(3)


# In[63]:


np.eye(1)


# In[64]:


np.eye(4)


# In[65]:


T=np.eye(4)


# In[66]:


print(T)


# In[67]:


#Incluso es posible definir una matriz, en este caso "T" que sea la matriz identidad de 4x4, ya que la definí como "T=np.eye(4)".


# In[69]:


# La función "np.zeros((m, n))" nos permite obtener la matriz nula de tamaño  𝑚×𝑛 . Por ejemplo, si queremos la matriz nula de tamaño  2×3 ----> "np.zeros((2,3))"


# In[70]:


np.zeros((2,3))


# In[71]:


#Matriz nula de 2x3


# In[72]:


L=np.zeros((2,3))


# In[73]:


print(L)


# In[74]:


#Nuevamente queda de manifiesto la facilidad o naturalidad con la que se maneja este lenguaje y uno que esta aprendiendo. Resulta ser muy intuitivo, casi básico, el hecho de que si puedo establecer una matriz nula de nxm, pueda definir una variable "X" que sea una matriz nula de nxm, como se vio en el ejemplo anterior.


# In[76]:


#La intuición que "permite" este lenguaje nos lleva a entender que de igual manera puedo establecer un vector nulo de n-coordenadas( o n-tuplas). Como? muy fácil ---> "np.zeros(n)". Es claro que al no ser una matriz no debo definir dos argumentos, es decir "((m,n))¨ sino unicamente uno, que se corresponde a la cantidad de coordenadas del vector.


# In[77]:


np.zeros(2)


# In[78]:


#Vector nulo de dos coordenadas


# In[79]:


O=np.zeros(4)


# In[80]:


print(O)


# In[81]:


#Nuevamente puedo definir una variable "O" que sea el vector nulo; en este caso de 4 coordenadas.


# In[82]:


# Con "np.ones((n,m))" obtenemos una matriz o vector del tamaño indicado con todos 1's. Su uso es análogo al de "np.zeros((n,m))". En el caso de una matriz si utilizo en el argumento "(n,m)" matriz de nxm. En el caso de un vector "(n,m)=(t)" donde "(t)=cantidad de coordenadas del vector".


# In[83]:


np.ones((2,4))


# In[84]:


np.ones(2)


# In[85]:


#Podemos generar una matriz aleatoria con valores en  [0,1]  de tamaño  𝑚×𝑛  con "np.random.rand(m,n)".


# In[86]:


np.random.rand((2,2))


# In[87]:


np.random.rand(2,2) #Matriz random con valores [0,1] de 2x2 


# In[88]:


#De manera analoga puedo generar un vector aleatorio con valores de [0,1] que tenga tantas coordenadas como lo defina. Coordenadas dadas por "n" ----->"np.random.rand(n)".


# In[89]:


np.random.rand(3) #Vector aleatorio de 3 coordenadas con valores 0<=x<=1.


# In[12]:


#El comando "arange" permite generar un vector que contiene a todos los números en un determinado rango. La sintaxis es "np.arange(inicio, fin, paso)"" donde fin no está incluido y paso es optativo (el valor por defecto es 1). Que es el paso? El paso es cada que intervalo se colocara un número. Es decir si elijo como paso n=2 significa que el rango númerico que solicite,su intervalo por ej [0,6], se hará de 2 en 2 ----> 0 2 4 (No incluido el 6 ya que el final del rango no se cuenta en gral) 


# In[2]:


np.arange(1,3,1)


# In[7]:


np.arange(1,3,1)<


# In[8]:


np.arange(1,3,1)


# In[9]:


np.random.rand(3
              )


# In[10]:


np.random.rand(2,3
              )


# In[11]:


np.arange(0,10,2)


# In[13]:


np.arange(0,100,50)


# In[14]:


np.arange(0,100,3) #"Creame el vector que contenga como elementos los numeros del 0-->100 pero espaciados en 3 lugares"


# In[15]:


#Si queremos sumar dos o más matrices o vectores, lo hacemos con +. Si queremos restar, lo hacemos con -n. Naturalmente, las dimensiones de los sumandos deben ser iguales.


# In[17]:


U=np.array([[2,3,4],[2,5,7]])
Y=np.array([[3,3,3],[23,4,1]])


# In[18]:


U+V


# In[19]:


print(U+Y)


# In[20]:


#Sumar un escalar a una matriz o a un vector equivale a sumarle el escalar a todas sus coordenadas.


# In[21]:


2+A


# In[22]:


#Si queremos multiplicar una matriz o un vector por un escalar, lo hacemos con *. Si queremos dividir por un escalar, los hacemos con /


# In[23]:


2*A


# In[24]:


(2*A)/2


# In[25]:


print(A)


# In[27]:


#El producto interno entre vectores, el producto matriz-matriz y matriz-vector se realiza con "@" o con el comando "np.dot(matrizquevaalaizquierda,matrizquevaaladerecha)". Siempre y cuando dicha operación sea posible, es decir cuando sea M matriz perteneciente a R^nxm y sea M1 matriz perteneciente a R^mxn. Coinciden la cantidad de columnas de la primera con la cantidad de filas de la segunda.


# In[28]:


np.dot(A,V)


# In[29]:


#Equivalente a


# In[31]:


A@V


# In[32]:


#Para resolver el sistema de ecuaciones lineales  𝐴𝑥=𝑏  utilizamos "np.linalg.solve(A,b)".  𝐴  debe ser una matriz cuadrada.


# In[33]:


def row_echelon(M):
    """ Return Row Echelon Form of matrix A """
    A = np.copy(M)
    if (issubclass(A.dtype.type, np.integer)):
        A = A.astype(float)
    #A = M.astype(float)
    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])


# In[34]:


# En el campus está disponible el archivo row_echelon.py con la función que aplica Gauss para escalonar una matriz.
#Probemoslo con la matriz A.


# In[35]:


row_echelon(A)


# In[36]:


#Matriz escalonada de A. Podemos ver que los componentes de la matriz A son linealmente independientes.


# In[37]:


#Para obtener la i-ésima coordenada de un vector lo hacemos con el siguiente comando ----> "nombredevector[i]"


# In[38]:


H=np.array([1,2,3,4,5,6,7,8,9,10])


# In[39]:


print(H)


# In[40]:


H[10]


# In[41]:


#Error porque python comienza a contar de 0 y le solicite la coordenada decima, la cual no esta dentro del "rango".


# In[42]:


H[9]


# In[43]:


#Si queremos obtener el lugar  𝑖,𝑗  de la matriz  𝐴  (o sea,  𝑎𝑖𝑗 ) lo hacemos agregando "nombredematriz[i,j]". i=filas j=columnas.


# In[45]:


#Podemos obtener submatrices con la sintaxis "nombredematriz[inicio:fin(filas),inicio:fin(columnas)]" donde se incluye el índice inicio y se excluye fin. Veamos un ejemplo.


# In[46]:


print(A)


# In[50]:


A[:,:] #Al no colocarle número alguno python interpreta que le solicito todas las filas y todas las columnas


# In[52]:


A[0:2,2:3] #Obtuvimimos la submatriz A´ donde el rango de filas son la 1 y la 2, el rango de columnas simplemente la 2.(Recordar como cuenta python)


# # Resolución de ejercicios:

# In[54]:


A=np.array([[0,2,2],[-1,0,1],[-1,1,4]])
B=np.array([[0,0,-1],[2,0,1]])
C=np.array([[0,2],[-1,3],[1,-1]])
v=np.array([-1,2,0])
u=np.array([3,1,2])
w=np.array([0,3,-1])


# In[55]:


print(A)


# In[56]:


print(B)


# In[57]:


print(C)


# In[58]:


print(v)


# In[62]:


print(u)


# In[63]:


print(w)


# In[64]:


#Haré los calculos sin exponer que estoy calculando(no copiare enunciado). El enunciado se encuentra en el archivo Numpy-campus.


# 2)a)

# In[65]:


(A.T)@C


# In[66]:


#El resultado es correcto. Simplemente lo resolvere nuevamente utilizando el comando "np.dot((A.T),C)".Funcionará?


# In[67]:


np.dot((A.T),C)


# In[68]:


#Evidenemente funciona.


# b)

# In[70]:


((2*B)@A) + C.T


# In[71]:


#Resultado correcto.


# c)

# In[86]:


(A@v)@u


# In[87]:


#Analogamente.


# In[88]:


np.dot(np.dot(A,v),u)


# d)

# In[92]:


A*(v@u)


# In[93]:


#Resultado correcto.


# e) El producto interno entre la primera columna de  𝐶  y  𝑤

# In[94]:


print(C)


# In[105]:


(C[:,0:1])@w #??


# f)

# 2*v + (C@B)@w

# In[106]:


#Resultado correcto.


# g) La solución del sistema  𝐴𝑥=𝑢

# In[108]:


np.linalg.solve(A,u)


# In[109]:


#Resultado correcto.


# h)

# In[110]:


(np.linalg.inv(A))@C


# In[111]:


#Resultado correcto. Pruebo otra forma de hacerlo.


# In[112]:


np.dot((np.linalg.inv(A)),C)


# i) El producto entre  𝐶  y la matriz que resulta de escalonar  𝐵

# In[113]:


C@(row_echelon(B))


# In[114]:


#Resultado correcto.


# j) El producto entre $C$ y la transpuesta de la submatriz de $A$ compuesta por los elementos de las primeras dos filas y últimas dos columnas.
# 

# In[115]:


C@((A[0:2,1:3]).T)


# In[116]:


#Resultado correcto.


# In[118]:


2*(np.linalg.norm(v-u))


# In[119]:


#Resultado correcto.


# In[ ]:




