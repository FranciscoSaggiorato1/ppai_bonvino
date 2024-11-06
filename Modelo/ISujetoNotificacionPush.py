from abc import ABC, abstractmethod

# Interfaz del Sujeto
class ISujetoNotificacionPush(ABC):

    def __init__(self):
        self.observadores = []

    @abstractmethod
    def suscribir(self, observers: list):
        pass

    @abstractmethod
    def quitar(self, observers: list):
        pass

    @abstractmethod
    def notificar(self):
        pass
		