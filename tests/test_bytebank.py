from codigo.bytebank import Funcionario
import pytest

class TestClass:
    def test_quando_idade_recebe_22_08_2010_deve_retornar_14(self):
        # Utilizando a metodologia Given-When-Then

        entrada = '22/08/2010' # Given - Dado a entrada
        esperado = 14
        
        funcionario_teste = Funcionario('Teste', entrada, 1500) 
        resultado = funcionario_teste.idade() # When - Quando chamar a função
        
        assert resultado == esperado # Then - Então compare o resultado

    def test_quando_sobrenome_recebe_Antonio_Marcos_deve_retornar_Marcos(self):
        entrada = 'Antonio Marcos ' # Given
        esperado = 'Marcos'

        antonio = Funcionario(entrada,'09/03/2000', 1500)
        resultado = antonio.sobrenome() # When

        assert resultado == esperado # Then

    def test_quando_decrescimo_salario_recebe_100000_e_sobrenome_recebe_Ptolomeu_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Andrei Ptolomeu' # Given
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '09/03/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # Given
        esperado = 100

        funcionario_teste = Funcionario('teste', '09/03/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # When

        assert resultado == esperado # Then

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 # Given

            funcionario_teste = Funcionario('teste', '09/03/2000', entrada)
            resultado = funcionario_teste.calcular_bonus() # When

            assert resultado # Then            