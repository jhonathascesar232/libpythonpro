from libpythonprooo.spam.modelos import Usuario


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
