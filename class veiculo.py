class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
  
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):    
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_detalhes(self):
        print("--- Detalhes do Carro ---")
        super().exibir_detalhes()
        print(f"Portas: {self.portas}")

class Motocicleta(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindrada: float):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def exibir_detalhes(self):
        print("--- Detalhes da Motocicleta ---")
        super().exibir_detalhes()
        print(f"Cilindrada: {self.cilindrada}cc")

if __name__ == "__main__":
    meu_carro = Carro("Ford", "Ka", 4)
    meu_carro.exibir_detalhes()

    print("\n" + "="*20 + "\n")
    minha_moto = Motocicleta("Honda", "CB 500", 500.0)
    minha_moto.exibir_detalhes()
