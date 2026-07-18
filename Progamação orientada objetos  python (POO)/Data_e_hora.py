from datetime import date, datetime, time

#data = date(2023, 7, 10) 
#print(data)
#print(date.today()) # date apenas ano mes dia


#data_hora = datetime(2023, 7, 10)
#print(data_hora)
#print(datetime.today()) #dia hora mes minuto ano "datetime" se for utilizado today mostra do momento atual

#hora = time(10, 20, 0)
#print(hora)
# ------------------------------------------------------------------------------------
from datetime import timedelta
# Timedelta = possui dia, segundos, microsegundos, dias, semanas.

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # traz o timezone ja setado... ?

if tipo_carro == "":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
# ------------------------------------------------------------------------------------
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a" #%H é usado pra horas 
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr)) # horario ptbr

data_convertida = datetime.strptime(data_hora_str, mascara_en) # horario ingles padrão
print(data_convertida)
print(type(data_convertida))
# ------------------------------------------------------------------------------------
from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)
# ------------------------------------------------------------------------------------
from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)