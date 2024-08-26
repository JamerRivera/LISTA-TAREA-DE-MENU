c = ["jamer", "dairon", "junior", "juan keo", "ronaldo", "el primo jesus", "luis diaz"]

menu = int(input("Elige una opción del menú:\n1. Crear Personas\n2. Eliminar personas\n3. Lista de personas\n4. Buscar persona\n"))

if menu == 1:
    print(c)
    c1 = input("Ingresa el nombre de la persona: ")
    c.append(c1)
    print(c)
if menu==2:
    print(c)
    c2=input("ingrese el nombre que desea eliminar:  ")
    c.remove(c2)
    print(c)
if menu==3:
    print(c)
if menu==4:
    print(c)
    c3=input("ingrese el nombre de la persona que quiere buscar:   ")
    if c3 in c:
        print("La persona esta en la lista")
    else:
        print("la persona no esta en la lista")


