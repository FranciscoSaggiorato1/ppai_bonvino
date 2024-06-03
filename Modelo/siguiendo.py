import csv
import os
from Modelo.bodega import Bodega

class Siguiendo:
    """
    Clase para representar una relación de seguimiento entre un enófilo y una bodega.
    """

    def __init__(self, fechaInicio, fechaFin, enofilo, bodega):
        """
        Inicializa una nueva instancia de la clase Siguiendo.

        Args:
            id (str): El ID de la relación de seguimiento.
            fechaInicio (str): La fecha de inicio del seguimiento.
            fechaFin (str): La fecha de fin del seguimiento.
            bodega (Bodega): La bodega seguida.
            enofilo (Enofilo): El enófilo seguido.
        """
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.enofilo = enofilo
        self.bodega = bodega
        

    def new(self, fechaInicio, fechaFin, bodega, enofilo):
        """
        Método para crear y devolver una nueva instancia de Siguiendo.

        Args:
            id (str): El ID de la relación de seguimiento.
            fechaInicio (str): La fecha de inicio del seguimiento.
            fechaFin (str): La fecha de fin del seguimiento.
            bodega (Bodega): La bodega seguida.
            enofilo (Enofilo): El enófilo seguido.

        Returns:
            Siguiendo: Una nueva instancia de la clase Siguiendo.
        """
        return Siguiendo(fechaInicio, fechaFin, bodega, enofilo)

    def __repr__(self):
        """
        Devuelve una representación de cadena de la instancia de Siguiendo.
        """
        return (
            f"fechaInicio={self.fechaInicio},"
            f"fechaFin={self.fechaFin},"
            f"bodega={self.bodega},"
            f"enofilo={self.enofilo}"
        )

    def sosDeBodega(self, bodega):
        """
        Verifica si la relación de seguimiento es de una bodega.

        Returns:
            bool: True si la relación es de una bodega, False en caso contrario.
        """
        
        if self.bodega == bodega:
            return True
        else:
            return False

    @staticmethod
    def cargarData(filepath, enofilos_data=None):
        """
        Carga datos desde un archivo CSV y crea instancias de Siguiendo.

        Args:
            filepath (str): La ruta del archivo CSV.
            enofilos_data (list): Lista de enófilos, opcional.

        Returns:
            list: Lista de instancias de Siguiendo.
        """
        from Modelo.enofilo import Enofilo
        siguiendos = []
        if enofilos_data is None:
            script_dir = os.path.dirname(__file__)
            path_enofilo = os.path.join(script_dir, '..', 'Modelo', './data/enofilo.csv')
            enofilos_data = Enofilo.cargarData(path_enofilo)

        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    siguiendo = Siguiendo(
                        id=row['id'],
                        fechaInicio=row['fechaInicio'],
                        fechaFin=row['fechaFin'],
                        bodega=None,
                        enofilo=None
                    )
                    enofilo_id = row['enofilo']
                    for enofilo in enofilos_data:
                        if enofilo.id == enofilo_id:
                            siguiendo.enofilo = enofilo
                    
                    script_dir = os.path.dirname(__file__)
                    path_bodega = os.path.join(script_dir, '..', 'Modelo', './data/bodega.csv')
                    TodasLasBodegas = Bodega.cargarData(path_bodega)
                    bodega_id = row['bodegas']
                    for bodega in TodasLasBodegas:
                        if bodega.id == bodega_id:
                            siguiendo.bodega = bodega

                    siguiendos.append(siguiendo)
                except ValueError as e:
                    print(f"Error al procesar la fila: {row}. Error: {e}")
        return siguiendos

    def to_dict(self):
        """
        Convierte la instancia de Siguiendo en un diccionario.

        Returns:
            dict: Un diccionario con los atributos de Siguiendo.
        """
        return {
            "fechaInicio": self.fechaInicio,
            "fechaFin": self.fechaFin,
            "bodega": self.bodega,
            "enofilo": self.enofilo
        }
