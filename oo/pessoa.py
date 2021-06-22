class Pessoa:
    olhos = 2
    def __init__(self,*filhos,nome=None,idade=35):
        self.idade = idade
        self.filhos = list(filhos)
        self.nome = nome
    @staticmethod
    def metodo_estatico():
        return 56
    @classmethod
    def metodo_classe(cls):
        return f'{cls} - Olhos {cls.olhos}'


    def comprimentar(self):
        return f'Olá, meu nome é {self.nome}'
class Mutante(Pessoa):
    olhos = 3
class Homen(Pessoa):
    def comprimentar(self):
    comprimentar_da_classeP = Pessoa.comprimentar(self)

        return f'{comprimentar_da_classeP}.Aperto de mão'

if __name__ == '__main__':

    arthur = Mutante(nome='Arthur')
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
    print('xx')
    print(Pessoa.metodo_estatico(),arthur.metodo_estatico())
    print(Pessoa.metodo_classe(),  arthur.metodo_classe())
    pessoa = Pessoa('Anonima')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(arthur,Homen))
    print(isinstance(pessoa,Homen))
    print(Pessoa.comprimentar(arthur))
