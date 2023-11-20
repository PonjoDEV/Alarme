import rpyc
from cryptography.fernet import Fernet
import random

#definindo metodo de encriptação
#encryption_key = Fernet.generate_key()
encryption_key = 'g5rpWlh1x0cs27Uh9jf5Hs_GMUn5bPp-b_QfB_3h0jg='

#criando um objeto Fernet
cipher_suite = Fernet(encryption_key)
hello = random.randint(0, 100)
#convertendo texto para ciphertexto usando byte format "b"
encrypted_value = cipher_suite.encrypt(hello)

#print(encrypted_value)

#remove o "b" do formato
print(encrypted_value.decode())

#decifrando mensagem
decyphred_value = cipher_suite.decrypt(encrypted_value).decode()

print(decyphred_value)


class Controlador2Client:

    def realizar_comunicacao(self):

        entrada = input("Digite 1 para acionar o alarme, 2 para desativar o alarme ou 3 para detectar aproximação: ")

        self.conn = rpyc.connect("localhost", 18862)
        #self.conn02 = rpyc.connect("localhost", 18863)

        if entrada == "1":
            result = self.conn.root.acionar_alarme()
            result = self.conn02.root.acionar_alarme()
        elif entrada == "2":
            result = self.conn.root.desativar_alarme()
            result = self.conn02.root.desativar_alarme()
        elif entrada == "3":
            result = self.conn.root.aproximacao()
            result = self.conn02.root.aproximacao()
            return result


if __name__ == "__main__":
    controlador2 = Controlador2Client()
    while True:
        controlador2.realizar_comunicacao()
