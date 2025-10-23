'''

#EXERCICIO 1
#Crie uma classe Pessoa com os atributos nome e idade.
#Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Bruno", 20)
p1.apresentar()


#EXERCICIO 2
#Crie uma classe Carro que tenha modelo, ano e velocidade.
#Adicione métodos acelerar() e frear().

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo      # Atributo
        self.ano = ano        # Atributo
        self.velocidade = 0   # Atributo inicial

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        print(f"{self.modelo} reduziu para {self.velocidade} km/h")

    def bater(self):
        self.velocidade = 0
        print(f"{self.modelo} bateu e agora está a {self.velocidade} km/h")

carro1 = Carro("Monza", "2008")
carro2 = Carro("Palio", "2010")

carro1.acelerar()
carro2.acelerar()
carro1.acelerar()
carro2.frear()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.bater()

#EXERCICIO 3
#Crie uma classe Conta com saldo e métodos depositar() e sacar().

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


#EXERCICIO 4       
#4. Crie uma classe Animal com método falar().

class Animal:
    def emitir_som (self):
        print("Rooooaaaarrr")
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

animais=[Cachorro(),Gato(),Animal()]

for a in animais:
    a.emitir_som()
'''
#EXERCICIO 5
#Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco -(self.preco * (percentual / 100));
        print(f"Você recebeu {percentual}% de desconto!")
        print(f"O valor total agora é {self.preco}")

compra = Produto("Iphone 17 Pro Max",7500)
compra.desconto(33)

   
#EXERCICIO 6
#Crie uma classe Livro com título, autor e método exibir_detalhes().

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
