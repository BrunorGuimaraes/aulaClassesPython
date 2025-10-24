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

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

livro1 = Livro("Cristianismo Puro e Simples", "C.S. Lewis") #Livro bom demais inclusive
livro1.exibir_detalhes()


#EXERCICIO 7 
#Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def resultado(self):
        if self.nota >= 7:
            print(f"{self.nome} foi aprovado com nota {self.nota}. Tirou onda!")
        else:
            print(f"{self.nome} foi reprovado com nota {self.nota}. Deu mole!")

aluno1 = Aluno("Bruno", 8.5)
aluno1.resultado()

aluno2 = Aluno("Theo", 6)
aluno2.resultado()

#EXERCICIO 8. 
#Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.

class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Dividir por 0 não dá né meu querido, bota outra coisa!"

calc = Calculadora()

print("Soma:", calc.somar(10, 5))
print("Subtração:", calc.subtrair(10, 5))
print("Multiplicação:", calc.multiplicar(10, 5))
print("Divisão:", calc.dividir(10, 5))

# EXERCICIO 9
# Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        # botei aqui uma classe pai, ela vai carregar os dados de setor e tals.
        super().__init__(nome, salario)# esse super é a função maneira q pega as info da classe acima, no caso nome e salario
        self.setor = setor

    def exibir_informacoes(self):
        super().exibir_informacoes() #aqui é a msm coisa basicamente
        print(f"Setor: {self.setor}")


# Exemplo de uso:
func1 = Funcionario("Bruno", 3000)
gerente1 = Gerente("Theo", 7000, "Vendas")

print("---- Funcionário ----")
func1.exibir_informacoes()

print("\n---- Gerente ----") #print para fins puramente estéticos, o de cima tb
gerente1.exibir_informacoes()

#10. Crie uma classe Retangulo com base e altura e método area().

# EXERCICIO 10
# Crie uma classe Retangulo com base e altura e método area().

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura 

retangulo1 = Retangulo(5, 3)
print(f"A área do retângulo é: {retangulo1.area()}")