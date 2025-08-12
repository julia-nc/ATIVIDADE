class animal:
    def __init__(self, nome):
        self.nome = nome
    def fezer_som(self):
        print("som generico de animal")        
class gato:
    def __init__(self, raça, nome):
        self.raça = raça
        self.nome = nome
        
    def miar(self):
        print("miauu miauu!")
class cachorro:
    def __init__(self, raça, nome):
        self.raça = raça
        self.nome = nome
        print("au au")