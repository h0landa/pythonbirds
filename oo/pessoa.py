class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = nome


    def comprimentar(self):
        return f'Olá {p.nome}'

if __name__ == '__main__':
    p = Pessoa()
    print('Digite seu nome: ')
    p.nome = input(str())
    print(p.comprimentar())
    print(Pessoa.comprimentar(p))
    print(p.nome)
    p.nome = 'Arthur'
    print(p.nome)
    p.idade = 18
    print(p.idade)
