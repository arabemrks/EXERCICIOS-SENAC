class Carro:
    def __init__(self, marca, modelo, ano, motor, cavalo, cor = "Fantasia"):
        self.marca = marca; self.modelo = modelo; self.ano = ano; self.motor = motor; self.cavalo = cavalo; self.cor = cor

    def maisNovo(self):
        print(f"O {self.marca}-{self.modelo} é o mais novo da lista sendo do ano {self.ano}")

    def gastaMais(self):
        print(f"O {self.marca}-{self.modelo} é o que gasta mais, pois é {self.motor}")

    def maisPotencia(self):
        print(f"O {self.marca}-{self.modelo} é mais potente , pois é {self.cavalo} cavalos")

car1 = Carro("Koenigsegg", "Jesko", 2022, "V8 Biturbo 5.0 litros", 1280)
car2 = Carro("Bugatti", "Tourbillon", 2024, "W16 8.3 litros", 1800, )
car3 = Carro("Rolls-Royce", "Ghost", 2020, "V12 6.75 litros", 563)
car4 = Carro("Lamborghini", "SVJ", 2021, "V12 6.5 litros", 780)

car2.maisNovo()