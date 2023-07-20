# RaizEcuacionCuadratica
script en Python que calcula las raices de una ecuación cuadrática. El usuario debe ingresar los términos a, b, c y el programa deberá calcular las raíces con la fórmula general y mostrar el valor de ambas raíces

El código que proporcionas calcula las raíces de una ecuación cuadrática en función de los coeficientes ingresados por el usuario. A continuación, te explico cómo funciona:

print('Ingrese los coeficientes de la ecuacion de izquierda a derecha: '): Muestra un mensaje indicando al usuario que debe ingresar los coeficientes de la ecuación cuadrática.

a = int(input('Ingrese el primer coeficiente: ')): Solicita al usuario que ingrese el primer coeficiente (coeficiente cuadrático) y lo almacena en la variable a.

b = int(input('Ingrese el segundo coeficiente: ')): Solicita al usuario que ingrese el segundo coeficiente (coeficiente lineal) y lo almacena en la variable b.

c = int(input('Ingrese el tercer coeficiente: ')): Solicita al usuario que ingrese el tercer coeficiente (término independiente) y lo almacena en la variable c.

discriminante = (b**2) - (4*a*c): Calcula el discriminante de la ecuación cuadrática utilizando la fórmula discriminante = b^2 - 4ac.

Luego, el código evalúa el valor del discriminante para determinar la cantidad de raíces y muestra el resultado correspondiente:

a. Si el discriminante es menor que 0, significa que la ecuación cuadrática tiene raíces imaginarias. En este caso, se calculan las raíces utilizando la fórmula cuadrática con el símbolo imaginario "i". Las raíces son mostradas en formato "X1 = x; X2 = y".
b. Si el discriminante es igual a 0, significa que la ecuación cuadrática tiene una única raíz real. En este caso, se calcula la raíz utilizando la fórmula cuadrática y se muestra como "La solucion unica es: x".
c. Si el discriminante es mayor que 0, significa que la ecuación cuadrática tiene dos raíces reales distintas. En este caso, se calculan ambas raíces utilizando la fórmula cuadrática y se muestran como "X1 = x; X2 = y".

Es importante tener en cuenta que la fórmula cuadrática asume que los coeficientes a, b y c representan una ecuación cuadrática de la forma ax^2 + bx + c = 0. Además, el código asume que los coeficientes ingresados por el usuario son números enteros (usando int(input(...))). Si se desean coeficientes con decimales, se puede utilizar float(input(...)).
