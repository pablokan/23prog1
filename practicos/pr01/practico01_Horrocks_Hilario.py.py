
nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 

sexos = ["f","f","m","f","m","f","m"]

fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]



sum= 0




for n in nombres:
    apellido, n = n.split(", ")
    letra = n[0]
    print(f"{letra}. {apellido}")
    

#----------------------------------------------------------------------------------------------------------------



nombreMasLargo = ""


for nombre in nombres:
  
    apellido, nombre = nombre.split()
    
    
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre

print("--------------------------------------------------------------------------------------------------------------")
print("El nombre más largo de la lista es:", nombreMasLargo)
print("--------------------------------------------------------------------------------------------------------------")







#-------------------------------------------------------------------------------------------------------------------------------
""" cantidad_sexos = len(sexos)
total_sexos = 0


for sexo in sexos:   # Calcular la suma de los sexos
    if sexo == "f":
        total_sexos = total_sexos + 1

print("el total de sexos femeninos es",total_sexos)


aH=2023
mH= 5
dH=17


edades=[]


for fecha in fechas:
    dH,mH,aH = fecha.split("/")

    aH=int(aH)
    mH=int(mH)
    dH=int(dH) """
    

    



        







