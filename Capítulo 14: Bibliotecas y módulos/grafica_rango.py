"""
Crear una gráfica de caja y bigotes para la cotización de un valor en bolsa
"""
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc

# Extraemos las cotizaciones para las fechas siguientes
fecha1 = (2014, 10, 13)
fecha2 = (2014, 11, 13)

# Vamos a la web y nos traemos la información de la cotización
valores = quotes_historical_yahoo_ohlc('AAPL', fecha1, fecha2)
if len(valores) == 0:
    raise SystemExit

# Definimos el aspecto de la gráfica
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

# Ponemos marcas mayores para los lunes
lunes = WeekdayLocator(MONDAY)
ax.xaxis.set_major_locator(lunes)

# Ponemos marcas menores para el resto de días
resto_dias = DayLocator()
ax.xaxis.set_minor_locator(resto_dias)

# Damos formato a los días
formato_semana = DateFormatter('%b %d')  # e.g., Ene 12
ax.xaxis.set_major_formatter(formato_semana)
ax.xaxis_date()

candlestick_ohlc(ax, valores, width=0.6)

ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()