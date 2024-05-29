class Maridaje():
    id=""
    descripcion = ""	
    nombre = ""
    def __init__(self,id, descripcion, nombre):
        self.id = id
        self.descripcion = descripcion
        self.nombre = nombre
    def new(self,id, descripcion, nombre):
        return Maridaje(id,descripcion, nombre)
    def __repr__(self):
        return (
            f"Maridaje(nombre={self.nombre}, "
            f"descripcion={self.descripcion},  "
            
        )
    def sosMaridaje(self,nombre):
        if self.nombre == nombre:
            return True
        else:
            return False
        
    
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
        maridajes = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    maridaje=Maridaje(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        nombre=row['nombre']
                    )
                    maridajes.append(maridaje)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return maridajes
    
    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "nombre": self.nombre,
        }

 # Ejemplo de uso
if __name__ == "__main__":
    maridajes=Maridaje.cargarData("data/maridajes.csv")
    for maridaje in maridajes:
        print(maridaje)