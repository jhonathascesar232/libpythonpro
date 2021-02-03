# para testes com venv tem que importar o caminho completo
from libpythonprooo.spam.enviador_de_email import Enviador
import pytest

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_rementente():
    enviador = Enviador()
    resposta = enviador.enviar(
        'jhonathascesar232@gmail.com',      #   de
        'silva@gmail.com',                  #   para
        'Assunto',                          #   Assunto
        'Mensagem',                         #   Mensagem
    )
    assert 'jhonathascesar232@gmail.com' in resposta


# parametrização: utilizado para varios testes na mesma função, com listas
# @pytest.mark.parametrize(
#     'remetente',                                        #   VÁRIAVEL A SER UTILIZADA NA FUNÇÃO
#     ['jhonathascesar232@gmail.com', 'bol@gmail.com']    #   Lista que vai ser iterada
# )

@pytest.mark.parametrize(
    'remetente',['jhonathascesar232@gmail.com', 'bol@gmail.com']
)
def test_rementente_com_parametrize(remetente):                         # VARIAVEL RECEBIDA DO DECORATOR
    enviador = Enviador()
    resposta = enviador.enviar(
        remetente,                          #   de
        'silva@gmail.com',                  #   para
        'Assunto',                          #   Assunto
        'Mensagem',                         #   Mensagem
    )
    assert remetente in resposta
