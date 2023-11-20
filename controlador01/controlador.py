import paho.mqtt.client as mqtt
import rpyc
from cryptography.fernet import Fernet
encryption_key = 'g5rpWlh1x0cs27Uh9jf5Hs_GMUn5bPp-b_QfB_3h0jg='
cipher_suite = Fernet(encryption_key)
encrypted_value = cipher_suite.encrypt(b"#############")

from conexaoDB import conexao

mqtt_broker = "localhost"
mqtt_topic_pub_atuador = "/atuador"
mqtt_topic_pub_sensor = "/sensor"

mqtt_client_controlador = mqtt.Client()
mqtt_client_controlador.connect(mqtt_broker, 1883, 60)


class Controlador1Service(rpyc.Service):

    def on_connect(self, conn):
        print("Conexão estabelecida com Controlador 1.")

    def on_disconnect(self, conn):
        print("Conexão perdida com Controlador 1.")

    def exposed_acionar_alarme(self):
        acao = "Ligar"
        acao_bytes = acao.encode('utf-8')
        encrypted_value = cipher_suite.encrypt(acao_bytes)
        mqtt_client_controlador.publish(mqtt_topic_pub_atuador, encrypted_value)
        conexao.conectadb(5433, True)

    def exposed_desativar_alarme(self):
        acao = "Desligar"
        acao_bytes = acao.encode('utf-8')
        encrypted_value = cipher_suite.encrypt(acao_bytes)
        mqtt_client_controlador.publish(mqtt_topic_pub_atuador, encrypted_value)
        conexao.conectadb(5433, False)

    #def exposed_aproximacao(self):
    #    acao = "Ligar"
    #    mqtt_client_controlador.publish(mqtt_topic_pub_sensor, acao)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(Controlador1Service, port=18862)
    t.start()
