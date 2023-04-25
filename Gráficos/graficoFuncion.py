import numpy as np
import matplotlib.pyplot as plt

#Se define la función f(t)
def f(t):
    return 2 - 2*np.exp(-t/3) * np.cos(2*t) #np.exp se refiere a la exponencial, np.cos al coseno y 2 a la constante

#Con la función "linespace" se crea un arreglo de valores equidistantes (0 y 20)
t = np.linspace(0, 20)  

#Se calculan los valores de la función f(t) para cada valor de t
f_values = f(t)

#Se crea la gráfica de f(t) y t
plt.plot(t, f_values) #La variable "t" es un array que contiene los valores del eje X y f_values" los valores del eje Y 

#Se agregan etiquetas a los ejes y un título al gráfico
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Gráfica de f(t) = 2 - 2e(-t/3) * cos(2t)')

#Se establece los límites del eje x
plt.xlim([0, 20])

#Se muestra el grafico
plt.show()
