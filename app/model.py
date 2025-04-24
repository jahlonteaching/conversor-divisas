from app.abstractions import IConversor


class Conversor(IConversor):
    def convertir_divisa(self, origen: str, destino: str, monto: float) -> float:
        pass

    def listar_tasas_de_cambio(self, origen: str) -> list[tuple[str, float]]:
        pass