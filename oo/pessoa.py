class Pessoa:
    def __init__(self,*filhos,nome=None,idade=35):
        self.idade = idade
        self.filhos = list(filhos)
        self.nome = nome


    def comprimentar(self):
        return f'Olá'

if __name__ == '__main__':

    arthur = Pessoa(nome='Arthur')
    ananda = Pessoa(arthur,nome = 'Ananda')
    print(ananda.comprimentar())
    print(ananda.nome)
    ananda.idade = 18
    print(ananda.idade)

    for filho in ananda.filhos:
        print(filho.nome)
