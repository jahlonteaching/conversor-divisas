import requests
from app.abstractions import IConversor
from app.util import obtener_divisas


class Conversor(IConversor):

    API_URL = "https://api.fxratesapi.com/latest"

    def convertir_divisa(self, origen: str, destino: str, monto: float) -> float:
        response = requests.get(f"{self.API_URL}?currencies={destino}&base={origen}&amount={monto}")
        if response.status_code != 200:
            raise RuntimeError("Error al obtener los datos de la API")

        tasa_cambio = response.json().get("rates", {}).get(destino)
        if not tasa_cambio:
            raise RuntimeError(f"No se encontró tasa de cambio para {destino}")

        return tasa_cambio


    def listar_tasas_de_cambio(self, origen: str) -> list[tuple[str, float]]:
        divisas = obtener_divisas()
        response = requests.get(f"{self.API_URL}?base={origen}&currencies={','.join(divisas)}")

        if response.status_code != 200:
            raise RuntimeError("Error al obtener los datos de la API")

        tasas = response.json().get("rates", {})
        if not tasas:
            raise RuntimeError(f"No se encontraron tasas de cambio para {origen}")

        return [(divisa, tasa) for divisa, tasa in tasas.items() if divisa in divisas]
