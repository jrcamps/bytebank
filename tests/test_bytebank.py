from codigo.bytebank import Funcionario

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