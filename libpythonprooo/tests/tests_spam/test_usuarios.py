from libpythonprooo.spam.db import Conexao
from libpythonprooo.spam.modelos import Usuario


def test_salvar_usuario():
    """
    Teste salvar usuário no banco.
    """
    #   SQLAlquemy
    conexao = Conexao()  # 1-Cria conexão, responsavel pela autenticação com o banco de dados
    sessao = conexao.gerar_sessao()  # 2-Utilizado para a comunicação com banco de dados
    usuario = Usuario(nome='Jhonathas')  # cria um usuário
    sessao.salvar(usuario)  # 3 Salva o usuário no banco
    # para certificar que o usuário foi salvo-> conferir o id
    assert isinstance(usuario.id, int)
    # Etapa de encerramento da conexão (TEAR DOWN)
    sessao.roll_back()  # para desfazer todas as alterações de testes no banco de dados
    sessao.fechar()  # Fechar a sessão para liberar recursos
    conexao.fechar()  # Fechar a conexão com banco de dados


def test_listar_usuarios():
    """
    Teste listar usuários do banco.
    """
    #   SQLAlquemy
    conexao = Conexao()  # 1-Cria conexão, responsavel pela autenticação com o banco de dados
    sessao = conexao.gerar_sessao()  # 2-Utilizado para a comunicação com banco de dados
    usuarios = [Usuario(nome='Jhonathas'), Usuario(nome='César')]  # cria varios usuários
    # itera os usuários
    for usuario in usuarios:
        sessao.salvar(usuario)  # 3 Salva o usuário no banco
    # para certificar que o usuário foi salvo-> conferir o id
    assert usuarios == sessao.listar()  # Metodo para retorna lista de usuários
    # Etapa de encerramento da conexão (TEAR DOWN)
    sessao.roll_back()  # para desfazer todas as alterações de testes no banco de dados
    sessao.fechar()  # Fechar a sessão para liberar recursos
    conexao.fechar()  # Fechar a conexão com banco de dados
