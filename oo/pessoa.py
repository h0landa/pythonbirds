class Pessoa:
    def __init__(self,*filhos,nome=None,idade=35):
        self.idade = idade
        self.filhos = list(filhos)
        self.nome = nome


    def comprimentar(self):
        return 'Olá'

if __name__ == '__main__':

    arthur = Pessoa(nome='Arthur')
    ananda = Pessoa(arthur,nome = 'Ananda')
    print(ananda.comprimentar())
    print(ananda.nome)
    ananda.sobrenome = 'maria'
    arthur.sobrenome = 'Holanda'
    del ananda.filhos
    arthur.idade = 18
    ananda.idade = 5
    print(ananda.idade)
    print(arthur.__dict__)
    print(ananda.__dict__)
