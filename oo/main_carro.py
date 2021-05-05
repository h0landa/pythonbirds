from carro import motor
print("""Digite a função:
    1 para acelerar
    2 para frear
    """)
funcao = int(input("Qual escolheu ?: "))
if funcao == 1:
    motor.acelerar(motor)
    print(motor.velocidade(motor))
if funcao == 2:
    motor.frear(motor)
    print(motor.velocidade(motor))

print("""+++ Digite para qual lado quer girar o volante +++
    Digite 1, para girar para direita
    Digite 2, para girar para esquerda
    """)