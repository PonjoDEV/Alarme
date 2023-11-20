import paho.mqtt.client as mqtt

mqtt_broker = "localhost"
mqtt_topic = "/atuador"

mqtt_client_atuador = mqtt.Client()
mqtt_client_atuador.connect(mqtt_broker, 1883, 60)


def on_message(client, userdata, msg):
    if msg.payload.decode() == "Ligar":
        print(msg.payload.decode())

    elif msg.payload.decode() == "Desligar":
        print(msg.payload.decode())


mqtt_client_atuador.subscribe(mqtt_topic)
mqtt_client_atuador.on_message = on_message
mqtt_client_atuador.loop_forever()
