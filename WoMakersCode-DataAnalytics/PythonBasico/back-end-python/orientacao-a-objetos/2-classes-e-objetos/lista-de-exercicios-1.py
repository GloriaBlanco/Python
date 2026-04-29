# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.


class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "Preto"
        self.modelo = 10
        self.velocidade = 20
        self.acelera_min = 0
        self.acelera_max = 200

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def mudar_cor(self):
        self.cor = "azul"

    def mudar_modelo(self):
        self.modelo = 7

    def desacerela(self):
        if not self.ligado:
            return

        if self.velocidade > self.acelera_min:
            self.velocidade -= 10

    def acelera(self):
        if not self.ligado:
            return

        if self.velocidade > self.acelera_max:
            self.velocidade += 10


    def __str__(self) -> str:
        return f'Carro  - ligado {self.ligada} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}'

    
# Crie uma instância da classe carro.
carro = Carro()


# Faça o carro "andar" utilizando os métodos da sua classe.
carro.ligar()
print('Carro está ligada? {}'.format(carro.ligado))


# Faça o carro "parar" utilizando os métodos da sua classe.
"""for _ in range(3):
    tv_sala.aumentar_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))
print()
"""
