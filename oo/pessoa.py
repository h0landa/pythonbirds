class Pessoa:
    def comprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(p.comprimentar())
    print(Pessoa.comprimentar())
