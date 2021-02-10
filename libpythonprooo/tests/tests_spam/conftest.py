import pytest

from libpythonprooo.spam.db import Conexao

# Iniciando com a funcionalidade do pytest: a fixture
# Etapas de Setup e Tear Down isoladas na fixture
# Escopo de session > é executada apenas uma vez durante toda a sessao de testes(toda a função)
# A execução da conexão foi apenas uma vez quando o modulo foi criado(Tempo contado apenas uma vez)

@pytest.fixture(scope='session')  # A fixture é executada no escopo de função(executa a função a cada teste)
def conexao():  # A fixture executa a função e retorna um objeto
    # Setup
    conexao_obj = Conexao()
    # retorna conexao_obj
    yield conexao_obj  # 1-Cria conexão, responsavel pela autenticação com o banco de dados
    # Tear down
    conexao_obj.fechar()  # depois fecha a conexao no mesmo periodo de


@pytest.fixture
def sessao(conexao):  # fixture da conexão
    # não pode ter o mesmo nome da function
    sessao_obj = conexao.gerar_sessao()  # 2-Utilizado para a comunicação com banco de dados
    yield sessao_obj
    sessao_obj.roll_back()  # para desfazer todas as alterações de testes no banco de dados
    sessao_obj.fechar()  # Fechar a sessão para liberar recursos