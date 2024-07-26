class AUAU:
    def __init__(self, nome, cor, idade, peso):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.peso = peso

        def disse(self):
            print(f"{self.nome} fez auauauauauauuaauuaua")

dog1 = AUAU("Paçoca", "Caramelo", 10, 5)
dog2 = AUAU("Bethoven", "Branco", 6, 14)

print(f"{dog2.nome} é {dog2.cor}, tem {dog2.idade} anos e pesa {dog2}")