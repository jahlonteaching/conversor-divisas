from abc import ABC, abstractmethod


class IConversor(ABC):

    @abstractmethod
    def convertir_divisa(self, origen: str, destino: str, monto: float) -> float:
        ...

    @abstractmethod
    def listar_tasas_de_cambio(self, origen: str) -> list[tuple[str, float]]:
        ...

