import csv  # Importa el módulo csv para trabajar con archivos CSV

class Siguiendo:
    # Propiedades de la clase SIGUIENDO
    id = ""  # Atributo para almacenar el ID de la relación de seguimiento
    fechaInicio = ""  # Atributo para almacenar la fecha de inicio del seguimiento
    fechaFin = ""  # Atributo para almacenar la fecha de fin del seguimiento
    bodega = None  # Atributo para almacenar la bodega seguida
    enofilo = None  # Atributo para almacenar el enófilo seguido

    # Método de inicialización de la clase SIGUIENDO
    def __init__(self, id, fechaInicio, fechaFin, bodega, enofilo):
        self.id = id  # Asigna el ID proporcionado al atributo id
        self.fechaInicio = fechaInicio  # Asigna la fecha de inicio proporcionada al atributo fechaInicio
        self.fechaFin = fechaFin  # Asigna la fecha de fin proporcionada al atributo fechaFin
        self.bodega = bodega  # Asigna la bodega proporcionada al atributo bodega
        self.enofilo = enofilo  # Asigna el enófilo proporcionado al atributo enofilo

    # Método para crear y devolver una nueva instancia de SIGUIENDO
    def new(self, id, fechaInicio, fechaFin, bodega, enofilo):
        return Siguiendo(id, fechaInicio, fechaFin, bodega, enofilo)

    # Método especial para representar la instancia de SIGUIENDO como una cadena
    def __repr__(self):
        return (
            f"fechaInicio={self.fechaInicio},"
            f"fechaFin={self.fechaFin},"
            f"bodega={self.bodega},"
            f"enofilo={self.enofilo}"
        )

    # Métodos getter y setter para los atributos de la clase
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_fechaInicio(self):
        return self.fechaInicio
    def set_fechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio
    def get_fechaFin(self):
        return self.fechaFin
    def set_fechaFin(self, fechaFin):
        self.fechaFin = fechaFin
    def get_bodega(self):
        return self.bodega
    def set_bodega(self, bodega):
        self.bodega = bodega
    def get_enofilo(self):
        return self.enofilo
    def set_enofilo(self, enofilo):
        self.enofilo = enofilo

    # Método para verificar si la relación de seguimiento es de una bodega
    def sosDeBodega(self):
        if self.bodega != None:
            return True
        else:
            return False

    # Método estático para cargar datos desde un archivo CSV
    @staticmethod
    def cargarData(filepath):
        siguiendos = []  # Lista para almacenar las instancias de SIGUIENDO
        with open(filepath, newline='', encoding='utf-8') as csvfile:  # Abre el archivo CSV
            reader = csv.DictReader(csvfile)  # Crea un lector de CSV
            for row in reader:  # Itera sobre las filas del archivo CSV
                try:
                    # Crea una instancia de SIGUIENDO con los datos de la fila actual
                    siguiendo = Siguiendo(
                        id=row['id'],
                        fechaInicio=row['fechaInicio'],
                        fechaFin=row['fechaFin'],
                        bodega=row['bodegas'],
                        enofilo=row['enofilo']
                    )
                    siguiendos.append(siguiendo)  # Agrega la relación de seguimiento a la lista
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return siguiendos  # Devuelve la lista de relaciones de seguimiento cargadas desde el archivo CSV

    # Método para convertir la instancia de SIGUIENDO a un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "fechaInicio": self.fechaInicio,
            "fechaFin": self.fechaFin,
            "bodega": self.bodega,
            "enofilo": self.enofilo
        }

# Ejemplo de uso
if __name__ == "__main__":
    # Carga los datos de relaciones de seguimiento desde un archivo CSV
    siguiendos = Siguiendo.cargarData("ruta_al_archivo.csv")
    for siguiendo in siguiendos:  # Itera sobre las relaciones de seguimiento cargadas
        print(siguiendo)  # Imprime cada relación de seguimiento
