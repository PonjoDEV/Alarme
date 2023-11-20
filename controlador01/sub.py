import paho.mqtt.client as mqtt

mqtt_broker = "localhost"
mqtt_topic = "/sensor"

mqtt_client_sensor = mqtt.Client()
mqtt_client_sensor.connect(mqtt_broker, 1883, 60)


def on_message(client, userdata, msg):
    intensidade = msg.payload.decode()
    print(intensidade)


mqtt_client_sensor.subscribe(mqtt_topic)
mqtt_client_sensor.on_message = on_message
mqtt_client_sensor.loop_forever()
