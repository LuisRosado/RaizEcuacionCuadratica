

print('Ingrese los coeficientes de la ecuacion de izquierda a derecha: ')

a = int(input('Ingrese el primer coeficiente: '))

b = int(input('Ingrese el segundo coeficiente: '))

c = int(input('Ingrese el tercer coeficiente: '))

discriminante = (b**2) - (4*a*c)

if discriminante < 0:

    x = (-b + (discriminante ** 0.5 )) / (2 * a)

    y = (-b - (discriminante ** 0.5 )) / (2 * a)

    print('Recordando que i = √ -1, tenemos que las raices son:  ')
    print('X1 = ', x, '; X2 = ', y)

elif discriminante == 0:
    x = (-b + (discriminante ** 0.5 )) / (2 * a)
    print('La solucion unica es: ',x)

else:
    x = (-b + (discriminante ** 0.5 )) / (2 * a)

    y = (-b - (discriminante ** 0.5)) / (2 * a)

    print('Las Raices son: ')
    print('X1 = ',x,'; X2 = ',y)
