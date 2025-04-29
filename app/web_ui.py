from nicegui import ui

from app.model import Conversor
from app.util import obtener_divisas

conversor = Conversor()

ui.markdown('# 💱 Conversor de Divisas').classes('text-center text-3xl font-bold mb-8')

with ui.row().classes('justify-center'):

    with ui.card().classes('w-1/2 shadow-xl p-6 rounded-2xl bg-white'):
        ui.markdown('## Convertir Divisa')

        origen = ui.select(obtener_divisas(), label='Divisa Origen')
        destino = ui.select(obtener_divisas(), label='Divisa Destino')
        monto = ui.input(label='Monto a Convertir', placeholder='Ej. 100', validation={'Ingrese un número': lambda v: v.replace('.', '', 1).isdigit()})
        resultado = ui.label()

        def convertir():
            if origen.value and destino.value and monto.value:
                valor = conversor.convertir_divisa(origen.value, destino.value, float(monto.value))
                resultado.text = f'Resultado: {valor:.2f} {destino.value}'

        ui.button('Convertir', on_click=convertir, icon='swap_horiz').classes('bg-blue-500 hover:bg-blue-600 text-white rounded-xl px-4 py-2')
        resultado.classes('mt-4 text-lg text-green-700')

    with ui.card().classes('w-1/2 shadow-xl p-6 rounded-2xl bg-white'):
        ui.markdown('## Tasas de Cambio')

        origen_tasa = ui.select(obtener_divisas(), label='Divisa Origen')
        resultado_tasas = ui.markdown('')

        def listar_tasas():
            tasas = conversor.listar_tasas_de_cambio(origen_tasa.value)
            texto = '\n'.join([f'- 1 {origen_tasa.value} = {valor:.2f} {destino}' for destino, valor in tasas])
            resultado_tasas.content = f'**Tasas de cambio:**\n{texto}' if tasas else 'No se encontraron tasas.'

        ui.button('Listar Tasas', on_click=listar_tasas, icon='list').classes('bg-green-500 hover:bg-green-600 text-white rounded-xl px-4 py-2')
        resultado_tasas.classes('mt-4')

ui.run()
