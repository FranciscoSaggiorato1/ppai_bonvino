import csv
class Usuario:
    #Propiedades de la clase Usuario
    id=""
    contraseña = ""
    nombre = ""
    premium = None

    def __init__(self,id, nombre, contraseña, premium):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium
    def new(self,id, nombre, contraseña, premium):
        return Usuario(id,nombre, contraseña, premium)
    def __repr__(self):
            return (f"Usuario(nombre={self.nombre}, "
                    f"contraseña={self.contraseña},"
                    f"premium={self.premium}"
                    )
    #Metodos de la clase Usuario
    def get_Id(self):
        return self.id
    def set_Id(self, id):
        self.id = id
    def getNombre(self, nombre):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getContraseña(self, contraseña):
        return self.contraseña
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    def getPremium(self):
        return self.premium
    def setPremium(self, premium):
        self.premium = premium
    def cargarData(filepath):
        usuarios = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    usuario=Usuario(
                        id=row['id'],
                        nombre=row['nombre'],
                        contraseña=row['contraseña'],
                        premium=row['premium']
                    )
                    usuarios.append(usuario)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return usuarios
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "contraseña": self.contraseña,
            "premium": self.premium
        }

 # Ejemplo de uso
if __name__ == "__main__":
        usuarios = Usuario.cargarData("ruta_al_archivo.csv")
        for usuario in usuarios:
            print(usuario)
