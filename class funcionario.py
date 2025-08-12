class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def calcular_bonus(self) -> float:
        bonus = self.salario * 0.20
        return bonus

class Desenvolvedor(Funcionario):
    def calcular_bonus(self) -> float: 
        bonus = self.salario * 0.10
        return bonus

if __name__ :
    gerente_ana = Gerente("Ana", 12000.00)
    dev_carlos = Desenvolvedor("Carlos", 7500.00)

    bonus_gerente = gerente_ana.calcular_bonus()
    print(f"Funcionário: {gerente_ana.nome}")
    print(f"Cargo: Gerente")
    print(f"Salário Base: R$ {gerente_ana.salario:.2f}")
    print(f"Bônus Calculado: R$ {bonus_gerente:.2f}\n")

    bonus_dev = dev_carlos.calcular_bonus()
    print(f"Funcionário: {dev_carlos.nome}")
    print(f"Cargo: Desenvolvedor")
    print(f"Salário Base: R$ {dev_carlos.salario:.2f}")
    print(f"Bônus Calculado: R$ {bonus_dev:.2f}")