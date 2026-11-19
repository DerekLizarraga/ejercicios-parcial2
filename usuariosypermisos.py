nombre=[]
apellido=[]
edad=[]
cumpleanos=[]
contrasena=[]
confirmarcontrasena=[]
correo=[]
opcion = 0

while True: #aqui inicia mi ciclo
    print("bienvenido al sistema de usuarios y sus permisos")
    print("-----------menu-----------")
    print("1.dar de alta a usuario")
    print("2.analizar informacion del usuario")
    print("3.eliminar informacion del usuario")
    print("4.modificar infomacion del usuario")
    print("5.salir del menu")
    opcion = int(input("selecciona una opcion"))

    match opcion:
        case 1: 
            nombre.append(input("ingrese su nombre completo"))
            apellido.append(input("ingresa tu appelido"))
            edad.append(int(input("ingresa su edad")))
            cumpleanos.append(input("ingrese su cumpleaños"))
            correo.append(input("ingrese su corrreo"))
            contrasena.append(input("ingrese su contrasena"))
            confirmarcontrasena.append(("verifique su contrasena"))
        case 2:
            print("Visualización de usuarios")
            #print("nombre: ", nombre,"edad: ", edad, "cumpleaños: ", cumpleanos, "correo: ", correo,"contraseña:"contraseña)
        
        case 3:
            print("borrar informacion de usuario")
            
        case 4:
            nombre.append(input("ingresa tu nombre"))
            apellido.append(input("ingresa tu apellido"))
            edad.append(input("ingresa tu edad"))
            cumpleanos.append(input("ingresa tu fecha de nacimiento"))
            correo.append(input("ingresa tu correo"))
        case 5:
            print("gracias por usar el sistema de usuarios y permisos")
        case _: 
            print("opcion no valida, por favor ingrese una opcion valida")