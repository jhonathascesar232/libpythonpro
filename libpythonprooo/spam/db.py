from time import sleep


class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def fechar(self):
        pass

    # Iniciando com isolamento de testes
    def roll_back(self):
        # emulando a limpeza no banco de dados
        self.usuarios.clear()  # list.clear() limpa a lista

    def listar(self):
        return self.usuarios


class Conexao:
    """
    Conexao com o banco de dados
    """
    def __init__(self):
        # Emulando a demora com a conexão do com o banco de dados
        sleep(10)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
