import pytest

from libpythonprooo.spam.db import Conexao
from libpythonprooo.spam.modelos import Usuario


# Iniciando com a funcionalidade do pytest: a fixture
# Etapas de Setup e Tear Down isoladas na fixture
@pytest.fixture
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


def test_salvar_usuario(sessao):  # a fixture executa o metodo e recebe o retorno
    """
    Teste salvar usuário no banco.
    """
    #   SQLAlquemy

    # sessao = sessao(conexao)
    usuario = Usuario(nome='Jhonathas')  # cria um usuário
    sessao.salvar(usuario)  # 3 Salva o usuário no banco
    # para certificar que o usuário foi salvo-> conferir o id
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    """
    Teste listar usuários do banco.
    """
    #   SQLAlquemy
    # sessao = conexao.gerar_sessao()  # 2-Utilizado para a comunicação com banco de dados
    usuarios = [Usuario(nome='Jhonathas'), Usuario(nome='César')]  # cria varios usuários
    # itera os usuários
    for usuario in usuarios:
        sessao.salvar(usuario)  # 3 Salva o usuário no banco
    # para certificar que o usuário foi salvo-> conferir o id
    assert usuarios == sessao.listar()  # Metodo para retorna lista de usuários
