import csv  # Importa el módulo csv para trabajar con archivos CSV

class Maridaje:
    def __init__(self, descripcion, nombre): 
        self.descripcion = descripcion  
        self.nombre = nombre  
    
    # Método para crear y devolver una nueva instancia de Maridaje
    def new(self, id, descripcion, nombre):
        return Maridaje(id, descripcion, nombre)
    
    # Método especial para representar la instancia de Maridaje como una cadena
    def _repr_(self):
        return (
            f"Maridaje(nombre={self.nombre}, "
            f"descripcion={self.descripcion})"
        )
    
    # Este método nos remarcó la profe micka que estaba mal, ya que dentro del objeto Maridaje cargabamos y recorriamos todos los maridajes
    # lo cual es incorrecto en POO
    """def sosMaridaje(nombre):
        maridajes = Maridaje.cargarData("./Modelo/data/maridaje.csv")  # Ajusta la ruta según sea necesario
        for maridaje in maridajes:
            if maridaje.nombre == nombre:
                return maridaje
        return None"""

    # Implementacion de sosMaridaje() de una forma alternativa 
    @staticmethod
    def sosMaridaje(maridaje):
        return isinstance(maridaje, Maridaje)

    # Métodos getter y setter para los atributos de la clase
    def get_Id(self):
        return self.id
    
    def set_Id(self, id):
        self.id = id
    
    def get_Descripcion(self):
        return self.descripcion
    
    def set_Descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def get_Nombre(self):
        return self.nombre
    
    def set_Nombre(self, nombre):
        self.nombre = nombre
    
    # Método estático para cargar datos desde un archivo CSV
    @staticmethod
    def cargarData(filepath):
        maridajes = []  # Lista para almacenar las instancias de Maridaje
        with open(filepath, newline='', encoding='utf-8') as csvfile:  # Abre el archivo CSV
            reader = csv.DictReader(csvfile)  # Crea un lector de CSV
            for row in reader:  # Itera sobre las filas del archivo CSV
                try:
                    # Crea una instancia de Maridaje con los datos de la fila actual
                    maridaje = Maridaje(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        nombre=row['nombre']
                    )
                    maridajes.append(maridaje)  # Agrega el maridaje a la lista de maridajes
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return maridajes  # Devuelve la lista de maridajes cargados desde el archivo CSV
    
    # Método para convertir la instancia de Maridaje a un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "nombre": self.nombre,
        }

# Ejemplo de uso
if __name__ == "__main__":
    maridajes = Maridaje.cargarData("../Modelo/data/maridaje.csv")  # Carga los datos de maridajes desde un archivo CSV
    for maridaje in maridajes:  # Itera sobre los maridajes cargados
       print(maridaje)  # Imprime cada maridaje
