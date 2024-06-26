import csv
class TipoUva:
    id=""
    descripcion = ""
    nombre = ""

    def __init__(self,id, descripcion, nombre):
        self.id = id
        self.descripcion = descripcion
        self.nombre = nombre
    def new(self,id, descripcion, nombre):
        return TipoUva(id,descripcion, nombre)
    def __repr__(self):
            return (f"TipoUva(nombre={self.nombre}, "
                    f"descripcion={self.descripcion},  "
                    )
        

    @staticmethod
    def sosTipoUva(nombre):
        tiposUva = TipoUva.cargarData("./Modelo/data/tipoUva.csv")  # Adjust the path as needed
        for tipo in tiposUva:
            if tipo.nombre == nombre:
                return tipo
        return None
     
    def get_Id(self):
        return self.id
    def set_Id(self,id):
        self.id = id

    def get_Descripcion(self):
        return self.descripcion 
    def set_Descripcion(self,descripcion):  
        self.descripcion = descripcion

    def get_Nombre(self):
        return self.nombre
    def set_Nombre(self,nombre):
        self.nombre = nombre
    def cargarData(filepath):
        tipos = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    tipo = TipoUva(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        nombre=row['nombre']
                    )
                    tipos.append(tipo)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return tipos
    
    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "nombre": self.nombre
        }

 # Ejemplo de uso
if __name__ == "__main__":
        tipos= TipoUva.cargarData("ruta_al_archivo.csv")
        for tipo in tipos:
            print(tipo)



             
