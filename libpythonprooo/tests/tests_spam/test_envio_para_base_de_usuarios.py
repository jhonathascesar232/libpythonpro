import pytest

from libpythonprooo.spam.enviador_de_email import Enviador
from libpythonprooo.spam.main import EnviadorDeSpam
# Produção de codigo testavel
from libpythonprooo.spam.modelos import Usuario


#
# Injeção de dependencias
#
class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [  # list[0]
        [  # list[0][0]
            Usuario(nome='Jhonathas', email='jhonathas@gmail.com'),
            Usuario(nome='César', email='jhonathas@gmail.com')
        ],  # end list[0][0]  # cria varios usuários
        [  # list[0][1]
            Usuario(nome='César', email='jhonathas@gmail.com')
        ]  # end list[0][1]
    ]  # end list[0]
)
def test_qtd_de_spam(sessao, usuarios):
    # Salvar os usuarios
    for usuario in usuarios:
        sessao.salvar(usuario)

    enviador = EnviadorMock()

    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        remetente='renzo@python.pro.br',
        assunto='Curso Python Pro',
        corpo='Confira os modulos Fantasticos'
    )
    # certificar a quantidade de emails
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='César', email='jhonathas@gmail.com')
    # Salvar os usuarios
    sessao.salvar(usuario)
    enviador = EnviadorMock()

    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        remetente='renzo@python.pro.br',
        assunto='Curso Python Pro',
        corpo='Confira os modulos Fantasticos'
    )
    # certificar a quantidade de emails
    assert enviador.parametros_de_envio == (
        'renzo@python.pro.br',
        'jhonathas@gmail.com',
        'Curso Python Pro',
        'Confira os modulos Fantasticos'
    )
