
#Ejercicio 1
informacion_personal = {
    "nombre": "Mauro",
    "edad": 16,
    "ciudad": "Ciudad Incorrecta",
    "profesion": "Profesión Incorrecta"
}


#Ejercicio 2
informacion_personal["ciudad"] = "CABA"
informacion_personal["profesion"] = "Estudiante"
informacion_personal["telefono"] = 1158903918
informacion_personal["email"] = "mauro.armendia.et32@gmail.com"


#Ejercicio 3
calificaciones = {
    "matematica": 6,
    "lengua": 8,
    "ciencia": 8
}
print(calificaciones.get("matematica"))


#Ejercicio 4
promedio = calificaciones.get("matematica") + calificaciones.get("lengua") + calificaciones.get("ciencias")
promedio = promedio / 3
print(promedio)


#Ejercicio 5
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Paraguay": "Asunción",
    "Uruguay": "Montevideo"
}

pais_ingresado = input("Ingresá un país: ")
print("La capital es:", paises.get(pais_ingresado, "País no encontrado"))

