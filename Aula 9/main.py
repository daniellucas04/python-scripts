from model import *

person_1 = Pessoa("José", "Souza")
person_1.info()

client = Cliente("Ana", "Ferreira", 1200)
client.info()

seller = Vendedor("Mauricio", "Sales", 12)
seller.info()


class Computer:
    def __init__(self, memory, processor):
        self.memory = memory
        self.processor = processor

    def my_pieces(self):
        print(self.memory, self.processor)


computer_1 = Computer(1, "AMD")
computer_2 = Computer(4, "Intel")

computer_1.my_pieces()
computer_2.my_pieces()
