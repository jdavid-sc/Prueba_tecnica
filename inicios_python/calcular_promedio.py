#@Nombre: David
#@Fecha: 16-08-2024
#@Descripcion: Programa que permite calcular el promedio del estudiante y recibir los datos nombre y asugnatura

nombre = input("Ingrese su nombre: ")
asignatura = input("Ingrese la asignatura: ")
nota_uno = float(input("Ingrese la primera nota: "))
nota_dos = float(input("Ingresa la segunda nota: "))
nota_tres = float(input("Ingresar la tercera nota: "))
definitiva = (nota_uno + nota_dos + nota_tres) / 3 
aprobo = "No"

if definitiva >= 3.5:
    aprobo = "Si"
    print("El estudiante gano la materia")
else: 
	print("el estudiante perdio la materia")

print(f"""
┌───────────┬────────────────┬─────────────┬──────────────┬─────────────┬───────────────┬────────────┐   
│  nombre   │   asignatura   │  nota_uno   │  nota_dos    │  nota_tres  │  definitiva   │ aprobo     │   
├───────────┼────────────────┼─────────────┼──────────────┼─────────────┼───────────────┼────────────┤
│{nombre:11s}│{asignatura:16s}│ {nota_uno:10.1f}  │ {nota_dos:10.1f}   │ {nota_tres:11.1f} │ {definitiva:12.1f}  │ {aprobo:8s}   │
└───────────┴────────────────┴─────────────┴──────────────┴─────────────┴───────────────┴────────────┘
      
      """)