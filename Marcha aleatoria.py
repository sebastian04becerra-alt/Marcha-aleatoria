import numpy as np
import matplotlib.pyplot as plt
#7///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def random_walk_1d(N, num_simulaciones):

    # Cada paso es +1(derecha) o -1(izquierda) con igual probabilidad
    pasos = np.random.choice([-1, 1], size=(num_simulaciones, N))
    # En este procedimiento elegimos aleatoriamente un elemento de la lista [-1,1] N veces
    # Donde N serian los pasos totales. Este procedimiento se realiza un cantidad de veces
    # denotado por la variable num_simulaciones.
    # Finalmente, pasos seria un array que contiene listas donde cada lista es una simulacion
    # con N elementos
    posiciones_finales = pasos.sum(axis=1)
    # En este procedimiento, tomamos los elementos de cada lista, que son los pasos, y los sumamos.
    # Por lo que posiciones_finales seria una lista cuyo len corresponde al numero de simulaciones
    # y cada posicion de la lista es la posicion final de cada simulacion.
    return posiciones_finales

# Parámetros
N = 1000
num_simulaciones = 1000

# Simulación
posiciones = random_walk_1d(N, num_simulaciones)

# Histograma
#Normalizamos el histograma con density=True ya que de lo contrario, si dejamos solo la frecuencia,
#El histograma no estara a escala de la funcion gaussiana con la que queremos compararla.
plt.hist(posiciones, bins=50, density=True, alpha=0.6, label="Simulación")

# Comparación con distribución gaussiana predicha por TCL
media= 0
varianza= N
x= np.linspace(min(posiciones), max(posiciones), 500)
gaussiana = (1/np.sqrt(2*np.pi*varianza)) * np.exp(-(x-media)**2/(2*varianza))
plt.plot(x, gaussiana, 'r-', label="Gaussiana (TCL)")

# Gráfica
plt.xlabel("Posición final")
plt.ylabel("Probabilidad")
plt.title(f"Marcha aleatoria 1D, N={N}, repeticiones={num_simulaciones}")
plt.legend()
plt.show()
#8//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Definimos una lista para varios Ns
lista_Ns=[800,850,900,910,950,1000,1010,1100,1200,1250,1400]
#Creamos una lista para los valores promedios x
x_promedio=[]
#Creamos una lista para los valores promedios de x^2
x2_promedio=[]
#Realizamos un recorrido de la lista
for i in lista_Ns:
  posiciones_finales=  random_walk_1d(i, num_simulaciones)
#Sacamos el promedio de x
  promedio_x= (sum(posiciones_finales))/num_simulaciones
  x_promedio.append(promedio_x)
#Sacamos el promeido de x2
  posiciones_finales1= np.array(posiciones_finales)
  posiciones_finales1=posiciones_finales1**2
  promedio_x2 = (sum(posiciones_finales1)) / num_simulaciones
  x2_promedio.append(promedio_x2)
print("Valores x promeido para cada N:", np.array(x_promedio))
#Luego hacemos una ajuste lineal para graficas x2 y N
def ajuste_lineal(x, y, graficar=True):

    x = np.array(x)
    y = np.array(y)
    a, b = np.polyfit(x, y, 1)



    return a, b



pendiente, intercepto = ajuste_lineal(lista_Ns, x2_promedio)
y_ajuste = pendiente * np.array(lista_Ns) + intercepto
print("Pendiente:", pendiente)
print("Intercepto:", intercepto)
# Gráfica
plt.scatter(lista_Ns, x2_promedio, color="blue", label="Datos")
plt.plot(lista_Ns, y_ajuste, color="red")
plt.title(r"Comportamiento de $\langle x^2 \rangle$ con $N$", fontsize=14, pad=15)
plt.xlabel("Número de pasos N", fontsize=12)
plt.ylabel(r"$\langle x^2 \rangle$", fontsize=12)
plt.legend(fontsize=11, loc="upper left", frameon=True)
plt.grid(alpha=0.3)

plt.show()
# Constante de difusión
#Tomamos delta_t=1
delta_t=1
D = pendiente / (2*delta_t)
print("Constante de difusion:", D)