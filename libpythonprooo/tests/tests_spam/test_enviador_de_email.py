# para testes com venv tem que importar o caminho completo
from libpythonprooo.spam.enviador_de_email import Enviador

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
