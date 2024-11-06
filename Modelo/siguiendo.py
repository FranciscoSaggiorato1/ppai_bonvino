import csv
import os
from Modelo.enofilo import Enofilo
from Modelo.bodega import Bodega

class Siguiendo:
    #Propiedades de la clase SIGUIENDO
    id=""
    fechaInicio = ""
    fechaFin = ""
    bodega = None
    enofilo = None
#Metodos de la clase SIGUIENDO
    def __init__(self,id, fechaInicio, fechaFin, bodega, enofilo):
        self.id = id
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.bodega = bodega
        self.enofilo = enofilo
    def new(self, id,fechaInicio, fechaFin, bodega, enofilo):
        return Siguiendo(id,fechaInicio, fechaFin, bodega, enofilo)
    def __repr__(self):
                return (
                        f"fechaInicio={self.fechaInicio},"
                        f"fechaFin={self.fechaFin},"
                        f"bodega={self.bodega},"
                        f"enofilo={self.enofilo}"
                        
                        )
    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id = id

    def get_fechaInicio(self):
        return self.fechaInicio

    def set_fechaInicio(self,fechaInicio):
        self.fechaInicio = fechaInicio

    def get_fechaFin(self):
        return self.fechaFin

    def set_fechaFin(self,fechaFin):
        self.fechaFin = fechaFin

    def get_bodega(self):
        return self.bodega
    def set_bodega(self,bodega):
        self.bodega = bodega
    def get_enofilo(self):
        return self.enofilo
    def set_enofilo(self,enofilo):
        self.enofilo = enofilo

    def sosDeBodega(self):
        if self.bodega != None:
            return True
        else:
            return False
    def cargarData(filepath):
        siguiendos = []
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    siguiendo = Siguiendo(
                        id=row['id'],
                        fechaInicio=row['fechaInicio'],
                        fechaFin=row['fechaFin'],
                        bodega=row['bodegas'],
                        enofilo=row['enofilo']
                    )

                    script_dir = os.path.dirname(__file__)
                    path_enofilo = os.path.join(script_dir, '..', 'Modelo', './data/enofilo.csv')
                    TodosLosEnofilos = Enofilo.cargarData(path_enofilo)
                    enofilo_id = row['enofilo'],
                    for enofilo in TodosLosEnofilos:
                            if enofilo.get_Id() == enofilo_id:
                                siguiendo.enofilo = enofilo
                    
                    script_dir = os.path.dirname(__file__)
                    path_bodega = os.path.join(script_dir, '..', 'Modelo', './data/bodega.csv')
                    TodasLasBodegas = Bodega.cargarData(path_bodega)
                    bodega_id = row['bodegas'],
                    for bodega in TodasLasBodegas:
                            if bodega.get_Id() == bodega_id:
                                siguiendo.bodega = bodega

                    siguiendos.append(siguiendo)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return siguiendos
    
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
        siguiendos= Siguiendo.cargarData("ruta_al_archivo.csv")
        for siguiendo in siguiendos:
            print(siguiendo)