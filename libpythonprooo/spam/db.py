class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    # Iniciando com isolamento de testes
    def roll_back(self):
        pass

    def fechar(self):
        pass

    def listar(self):
        return Sessao.usuarios


class Conexao:

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
