nombre=""
apellido=""
edad=0
cumpleanos=""
contrasena=""
confirmarcontrasena=""
correo=""


print=("bienvenido al sistema de usuarios y sus permisos")
print=("-----------menu-----------")
print=("1.dar de alta a usuario")
print=("2.analizar informacion del usuario")
print=("3.eliminar informacion del usuario")
print=("4.modificar infomacion del usuario")
print=("5.salir del menu")
opcion=int(input)("selecciona una opcion")

match option:
    case 1: 
        name=input=("ingrese su nombre completo")
        apellido=input("ingresa tu appelido")
        edad=int=input("ingresa su edad")
        cumpleanos=input("ingrese su cumpleaños")
        correo=input("ingrese su corrreo")
        contrasena=input("ingrese su contrasena")
        confirmarcontraseña=("verifique su contrasena")
    case 2:
        print=("nombre: ", nombre,"edad: ", edad, "cumpleaños: ", cumpleanos, "correo: ", correo,"contraseña:"contraseña)
        case 3
        nombre=""
        apellido=""
        edad=0
        cumpleanos=""
        contrasena=""
        correo=""
        contrasena=""
    case 4
        nombre=input("ingresa tu nombre")
        apellido=input("ingresa tu apellido")
        edad=input("ingresa tu edad")
        cumpleanos=input("ingresa tu fecha de nacimiento")
        correo=input("ingresa tu correo")
    case 5 
        print("gracias por usar el sistema de usuarios y permisos")
    case 6 
        print("opcion no valida, por favor ingrese una opcion valida")