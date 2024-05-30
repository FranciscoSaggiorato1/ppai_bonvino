import csv
import os
from Modelo.tipoUva import TipoUva

class Varietal():
    id=""
    descripcion = ""
    porcentajeComposicion = 0
    tipoUva= None
    def __init__(self,id, descripcion, porcentajeComposicion,tipoUva):
        self.id = id
        self.descripcion = descripcion
        self.porcentajeComposicion = porcentajeComposicion
        self.tipoUva = tipoUva
    def new(self,id, descripcion, porcentajeComposicion,tipoUva):
        return Varietal(id,descripcion, porcentajeComposicion,tipoUva) 

    def __repr__(self):
        return (f"Varietal(descripcion={self.descripcion}, "
                f"porcentajeComposicion={self.porcentajeComposicion},  "
                f"tipoUva={self.tipoUva}")
    

    def get_Id(self):
        return self.id
    def set_Id(self,id):
        self.id = id 
    def get_Descripcion(self):
        return self.descripcion
    def set_Descripcion(self,descripcion):
        self.descripcion = descripcion
    def get_Porcentaje_Composicion(self):
        return self.porcentajeComposicion
    def set_Porcentaje_Composicion(self,porcentajeComposicion):
        self.porcentajeComposicion = porcentajeComposicion
    def get_Tipo_Uva(self):
        return self.tipoUva
    def set_Tipo_Uva(self,tipoUva):
        self.tipoUva = tipoUva

    def cargarData(filepath):
        varietales = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    varietal = Varietal(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        porcentajeComposicion=row['porcentajeComposicion'],
                        tipoUva=""
                    )
                    script_dir = os.path.dirname(__file__)
                    path_tipoUva = os.path.join(script_dir, '..', 'Modelo', './data/tipoUva.csv')
                    TodosLostipoUva = TipoUva.cargarData(path_tipoUva)
                    tipoUva_id = row['tipoUva'],
                    for tipo in TodosLostipoUva:
                            if tipo.get_Id() == tipoUva_id:
                                varietal.tipoUva = tipo
                    
                    varietales.append(varietal)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return varietales
    
    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "porcentajeComposicion": self.porcentajeComposicion,
            "tipoUva": self.tipoUva
        }

 # Ejemplo de uso
if __name__ == "__main__":
        varietales = Varietal.cargarData("./Modelo/data/varietal.csv")
        for varietal in varietales:
            print(varietal)



             