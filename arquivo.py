class Carro:
    def __init__(self, nome, cor):
        self.nome = nome      # Atributo
        self.cor = cor        # Atributo
        self.velocidade = 0   # Atributo inicial

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.nome} está a {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        print(f"{self.nome} reduziu para {self.velocidade} km/h")

carro1 = Carro("Fusca", "Azul")
carro2 = Carro("Gol", "Vermelho")

carro1.acelerar()
carro2.acelerar()
carro2.frear()

# ENCAPSULAMENTO

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo}")