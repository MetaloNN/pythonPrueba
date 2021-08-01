def salir():
  aux = True
  while aux == True:
    print("Desea realizar otra operacion? (Si/No)")
    operacion = input()
    if operacion.lower() == "si":
      return True
    elif operacion.lower() == "no":
      return False
    else:
      print("Opcion no valida ingrese nuevamente.")

def actualizarUser(newUser):
  validaBlanco = newUser != ''
  validaMinusculas = newUser.islower()
  validaAlfanumerico = newUser.isalnum()

  if validaBlanco == False:
    print('Error: No se puede dejar vacio')
  if validaMinusculas == False:
    print('Error: Solo se pueden usar minusculas')
  if validaAlfanumerico == False:
    print('Error: Solo se pueden ingresar datos alfanumericos')

  return validaBlanco and validaMinusculas and validaAlfanumerico

def actualizarPassword(newPassword):
  validaBlanco = newPassword != ''
  largoPassword = len(newPassword)>7
  validaAlfanumerico = newPassword.isalnum()

  if validaBlanco == False:
    print('Error: No se puede dejar vacio')
  if largoPassword == False:
    print('Error: La contraseña no puede ser menor de 8 caracteres')
  if validaAlfanumerico == False:
    print('Error: Solo se pueden ingresar datos alfanumericos')

  return validaBlanco and largoPassword and validaAlfanumerico

def validador(user, password):
  
  validaBlanco = user!='' and password!=''
  validaMinusculas = user.islower()
  largoPassword = len(password)>7
  validaAlfanumerico = user.isalnum() and password.isalnum()

  if validaBlanco == False:
    print('Error: No se puede dejar vacio')
  if validaMinusculas == False:
    print('Error: Solo se pueden usar minusculas')
  if largoPassword == False:
    print('Error: La contraseña no puede ser menor de 8 caracteres')
  if validaAlfanumerico == False:
    print('Error: Solo se pueden ingresar datos alfanumericos')
  
  return validaBlanco and validaMinusculas and largoPassword and validaAlfanumerico

bucle = True
while bucle == True:
  user = input("Cree su nombre de usuario: ")
  password = input("Cree una contraseña: ")
  comprobador = validador(user, password)
  if comprobador == True:
    print("Se a creado exitosamente su usuario y contraseña.")
    bucle = False
  else:
    print("Intente nuevamente")

rut = input("Ingrese su rut: ")
diccionario = {rut : [user, password]}

menu = True
while menu == True:
  print("Ingrese el numero correspondiente para lo que sigue:")
  opcion = input("1.Mostrar los datos.\n2.Ingresar un dato.\n3.Actualizar usuario/password.\n4.Eliminar un dato.\n5.Salir.\n")
  if opcion == "1":
    print(diccionario)
    menu = salir()
  elif opcion == "2":
    dato = input("Ingrese el nuevo dato: ") #El ejercicio dice ingresar datos solicitados, nunca especifica cuantos ni que tipo.
    diccionario.get(rut).append(dato)
    menu = salir()
  elif opcion == "3":
    act = int(input("Que dato desea actualizar ?\n1.Usuario.\n2.Password.\n"))
    if act == 1 :
      bucle2 = True
      while bucle2 == True:
        newUser = input("Ingrese su nuevo usuario: ")
        comprobadorUser = actualizarUser(newUser)
        if comprobadorUser == True:
          print("Se a actualizado exitosamente su usuario.")
          bucle2 = False
        else:
          print("Intente nuevamente")
      user = newUser
      diccionario.update({rut : [user, password]})
      menu = salir()
    elif act == 2:
      bucle3 = True
      while bucle3 == True:
        newPassword = input("Ingrese su nueva contraseña: ")
        comprobadorPass = actualizarPassword(newPassword)
        if comprobadorPass == True:
          print("Se a actualizado exitosamente su contraseña.")
          bucle3 = False
        else:
          print("Intente nuevamente")
      password = newPassword
      diccionario.update({rut: [user, password]})
      menu = salir()
    else:
      print("Opcion no valida")
      menu = salir()
  elif opcion == "4":
    print("que dato desea eliminar?", end="")
    print(diccionario.get(rut))
    borrar = input("Escriba exactamente el dato que quiera eliminar: ")
    if diccionario.get(rut).count(borrar) > 0:
      diccionario.get(rut).remove(borrar)
      print("usted a eliminado *",borrar,"* la lista queda de la siguente forma", diccionario.get(rut))
      menu = salir()
    else:
      print("error, dato mal ingresado")
      menu = salir()

  elif opcion == "5":
    print("Salir.")

    menu = False

  else:
    print("opcion no valida")
    menu = salir()

print(diccionario)