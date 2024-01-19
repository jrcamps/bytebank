from bytebank import Funcionario

# lucas = Funcionario('Lucas da Silva', '18/09/1997', 1530)
# print(lucas.idade())

def teste_funcionario():
    teste = Funcionario('Teste', '23/05/2000', 1250)
    print(f'Teste: {teste.idade()}')

teste_funcionario()