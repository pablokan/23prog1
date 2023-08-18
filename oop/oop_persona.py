class Persona():
    def __init__(self, id, name, address, phone):
        # El constructor se ejecuta de manera automática en el momento de la creación del objeto y recibe los argumentos enviados entre los paréntesis de la clase

        self.dni = id # atributo del objeto
        self.nombre = name
        self.direccion = address
        self.telefono = phone

    def getDNI(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getTelefono(self):
        return self.telefono
    
#humano1 = Persona() # creación de una persona
#humano1.setData(34345345, 'Ana Molina', 'Mitre 1234', 3585121212)
# Reemplazo las dos líneas anteriores por una sola
humano1 = Persona(34345345, 'Ana Molina', 'Mitre 1234', 3585121212) # estos argumentos ingresa en los parámetros del constructor

humano2 = Persona(14345345, 'Juan Perez', 'Alvear 1234', 3585121299)

print(f'El teléfono del humano1 es {humano1.telefono}')
print(f'Los datos de humano2 son DNI:{humano2.getDNI()} Nombre:{humano2.getNombre()} Dirección:{humano2.getDireccion()} Teléfono:{humano2.getTelefono()}')







    
