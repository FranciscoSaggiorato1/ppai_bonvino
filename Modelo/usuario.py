import csv  # Importa el módulo csv para trabajar con archivos CSV

class Usuario:
    # Propiedades de la clase Usuario
    id = ""  # Atributo para almacenar el ID del usuario
    contraseña = ""  # Atributo para almacenar la contraseña del usuario
    nombre = ""  # Atributo para almacenar el nombre del usuario
    premium = None  # Atributo para indicar si el usuario es premium o no

    # Método de inicialización de la clase Usuario
    def __init__(self, contraseña, nombre, premium):
        self.nombre = nombre  # Asigna el nombre proporcionado al atributo nombre
        self.contraseña = contraseña  # Asigna la contraseña proporcionada al atributo contraseña
        self.premium = premium  # Asigna el estado de premium proporcionado al atributo premium

    # Método para crear y devolver una nueva instancia de Usuario
    def new(self, contraseña, nombre, premium):
        return Usuario(contraseña, nombre, premium)

    # Método especial para representar la instancia de Usuario como una cadena
    def __repr__(self):
        return (f"Usuario(nombre={self.nombre}, "
                f"contraseña={self.contraseña},"
                f"premium={self.premium}"
                )

    # Métodos getter y setter para los atributos de la clase

    def getNombre(self):
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

    # Método estático para cargar datos desde un archivo CSV
    @staticmethod
    def cargarData(filepath):
        usuarios = []  # Lista para almacenar las instancias de Usuario
        with open(filepath, newline='', encoding='utf-8') as csvfile:  # Abre el archivo CSV
            reader = csv.DictReader(csvfile)  # Crea un lector de CSV
            for row in reader:  # Itera sobre las filas del archivo CSV
                try:
                    # Crea una instancia de Usuario con los datos de la fila actual
                    usuario = Usuario(
                        id=row['id'],
                        nombre=row['nombre'],
                        contraseña=row['contraseña'],
                        premium=row['premium']
                    )
                    usuarios.append(usuario)  # Agrega el usuario a la lista de usuarios
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return usuarios  # Devuelve la lista de usuarios cargados desde el archivo CSV

    # Método para convertir la instancia de Usuario a un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "contraseña": self.contraseña,
            "premium": self.premium
        }

# Ejemplo de uso
if __name__ == "__main__":
    # Carga los datos de usuarios desde un archivo CSV
    usuarios = Usuario.cargarData("ruta_al_archivo.csv")
    for usuario in usuarios:  # Itera sobre los usuarios cargados
        print(usuario)  # Imprime cada usuario
