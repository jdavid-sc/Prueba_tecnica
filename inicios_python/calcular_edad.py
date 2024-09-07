nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

if edad >= 18:
    print(f"el estudiante {nombre} tiene {edad} años y es mayor de edad")
else: 
    print(f"el estudiante {nombre} tiene {edad} años y es menor de edad")