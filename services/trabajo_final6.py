import os
# Funcion encabezado
def encabezado():
    print()
    print("         Planilla de pacientes")
    print("         *********************")
    print()
    
#Funcion menu principal
def menu_principal(a,b,c,d):
    while True:
        os.system("cls")
        encabezado()
        print("     1-Ver planilla de Pacientes")
        print("     2_Ingresar paciente")
        print("     3-Eliminar paciente")
        print("     4-Modificar paciente")
        print("     5-Salir")
        
        print()
        menu=input("     Ingrese opción: ")
        
        print()
        if (menu=="5"):
            #Salgo del bucle,no del programa...                  
            break
        
        elif(menu=="1"):
            
            ver_planilla()
            input("presione Enter para continuar...")
                  
        elif(menu=="2"):
            
                      
            ingreso_paciente()
            pass
        elif(menu=="3"):
            
            eliminar_paciente()
            
        elif(menu=="4"):
            encabezado()
            
            modificar_paciente()
        else:
            print("Elección incorrecta")
               
            
            
            
def ver_planilla():
    
     while True:
            os.system("cls")
            encabezado()
            print("     Qué acción desea realizar?")
            print()
            print("     1-Ver ficha  \n     2-Regresar")
            print()
            opcion=input("     Elija opción: ")      
            print()
            if (opcion=="2"):
                #Salgo del bucle,no del programa...                  
                break
            elif(opcion=="1"):
                den=input("Ingrese dni del usuario: ")
                print()
                
                for i in range(len(dni)):
                    if dni[i]==den:
                        print("Nombre: ",nombre_apellido[i])
                        print("DNI: ",dni[i])
                        print("Obra Social:",obra_social[i])
                        print("Email: ",email[i])
                        print()
                        break
                
      
    
    
    #for x in range(len(nombre_apellido)):
     #   print ("Paciente:",nombre_apellido[x],"  DNI:",dni[x],"  Obra Social:",obra_social[x],"  mail:",email[x])

    
def ingreso_paciente():
        while True:
            os.system("cls")
            encabezado()
            print("     Qué acción desea realizar?")
            print()
            print("     1-Ingresar paciente  \n     2-Regresar")
            print()
            opcion=input("     Elija opción: ")      
            print()
            if (opcion=="2"):
                #Salgo del bucle,no del programa...                  
                break
            elif(opcion=="1"):
                
                nombre=input("Nombre y apellido completo:")
                dn=input("Dni: ")
                o_social=input("Obra social y plan: ")
                mail=input("Email:")
                print()
                                
                nombre_apellido.append(nombre)
                dni.append(dn)
                obra_social.append(o_social)
                email.append(mail)
                
                                
            else:
                
                print("     Opción incorrecta")
                
def eliminar_paciente():
    while True:
        os.system("cls")
        encabezado()
        print("     Eliminado datos del paciente por dni")
        print()
        elec=input("  1-Eliminar usuario\n 2-Cancelar y volver")
        
        if(elec=="2"):
            break
        
        elif(elec=="1"):
            print()
            den=input(" Ingrese dni de paciente a eliminar:")
            print()
            for i in range(len(dni)-1-1-1):
                if dni[i]==den:
                   nombre_apellido.pop(i)
                   dni.pop(i)
                   obra_social.pop(i)
                   email.pop(i)
                   print("Usuario eliminado")
                   print()
                   break 
            
                else:
                    print("no se encuentra")                     
                
        else:
            print("Digite opción correcta")
   
    
    
             
def modificar_paciente():
    os.system("cls")
    encabezado()
    print("     Modificar paciente por DNI")
    print()
    den=int(input("     Ingrese DNI de paciente a modificar:"))
    print()
    
    for x in range (len(dni)):
         if dni[x]==den:
               nombre_apellido[x]=input("     Nuevo nombre y apellido completo:")
               obra_social[x]=input("     Obra social y plan: ")
               email[x]=input("     Email: ")
               print()
               print("Datos del paciente modificados")
             



nombre_apellido=[]
dni=[]
obra_social=[]
email=[]
nombre_apellidoX=open("nombre_apellido.txt","w")           
dniX=open("dni.txt","w")
obra_socialX=open("obra_social.txt","w")
emailX=open("email.txt","w")

nombre_apellidoX.close()
dniX.close()
obra_socialX.close()
emailX.close()




nombre_apellidoX=open("nombre_apellido.txt","r")           
dniX=open("dni.txt","r")
obra_socialX=open("obra_social.txt","r")
emailX=open("email.txt","r")


for x in nombre_apellidoX.readline().split(","):
      if(x !=" "):
          nombre_apellido.append(x)
        
for x in dniX.readline().split(","):
      if(x!=" "):
          dni.append(str(x))
         
for x in obra_socialX.readline().split(","):
     if(x!=" "):
          obra_social.append(x)
         
for x in emailX.readline().split(","):
      if(x!=" "):
          email.append(x)
  


   
    
menu_principal(nombre_apellido,dni,obra_social,email)

nombre_apellidoX.close()
dniX.close()
obra_socialX.close()
emailX.close()


nombre_apellidoX=open("nombre_apellido.txt","w")           
dniX=open("dni.txt","w")
obra_socialX=open("obra_social.txt","w")
emailX=open("email.txt","w")



for i in range (len(nombre_apellido)):
     nombre_apellidoX.write(nombre_apellido [i]+",")
     dniX.write(str(dni [i])+",")
     obra_socialX.write(obra_social[i]+",")
     emailX.write(email [i]+",")

nombre_apellidoX.close()
dniX.close()
obra_socialX.close()
emailX.close()