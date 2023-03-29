from machine import Pin
from time import sleep
import dht

sensorDHT = dht.DHT11(Pin(14))

while True:
    try:
        sleep(2)
        sensorDHT.measure()
        temperatura = sensorDHT.temperature()
        umidade = sensorDHT.humidity()
        print(f"Temperatura ambiente: {temperatura: .0f}°C")
        print(f"Umidade relativado ar: {umidade: .0f}%")
        if temperatura <= 0:
            print("Muito Frio")
        elif temperatura > 0 and temperatura <= 10:
            print("Frio")
        elif temperatura > 10 and temperatura <= 15:
            print("Frio Leve")
        elif temperatura > 15 and temperatura <= 20:
            print("Agradavel")
        elif temperatura > 20 and temperatura <= 25:
            print("Levemente Quente")
        elif temperatura > 25 and temperatura <= 30:
            print("Quente")
        elif temperatura > 30:
            print("Muito Quente")
    except OSError as e:
        print("Erro na leitura do sensor DHT!")
