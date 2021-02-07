from libpythonprooo.spam.enviador_de_email import Enviador
from libpythonprooo.spam.main import EnviadorDeSpam


# Iniciando com conftest.py > compartilhar as fixture o com o
# pacote correspondente a que pertence
def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        remetente='renzo@python.pro.br',
        assunto='Curso Python Pro',
        corpo='Confira os modulos Fantasticos'
    )
