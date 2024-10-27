from abc import ABC, abstractmethod

class IObserverNotificacionPush(ABC):
    @abstractmethod
    def enviarNotificacion(self, bodega, fechaActualizacion, vinosActializados, vinosCreados):
        pass