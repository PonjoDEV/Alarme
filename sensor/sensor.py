import random
import time

import paho.mqtt.client as mqtt

mqtt_broker = "localhost"
mqtt_topic = "/sensor"

mqtt_client_sensor = mqtt.Client()
mqtt_client_sensor.connect(mqtt_broker, 1883, 60)


def on_publish(client, userdata, result):
    print("Dispositivo 1: Dados Publicados.")
    pass


while True:
    time.sleep(1)
    intensidade = random.randint(0, 100)
    print(intensidade)
    resultado = mqtt_client_sensor.publish(mqtt_topic, intensidade)
    mqtt_client_sensor.on_publish = on_publish
