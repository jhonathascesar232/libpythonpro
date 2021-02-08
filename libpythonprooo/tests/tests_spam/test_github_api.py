from unittest.mock import Mock

from libpythonprooo import github_api


# Módulo como Objeto: Iniciando
# Teste buscar avatar
# 1 Isolando testes, 2 - contruir o Mock(Substitui as funçõe do módulo original)

def test_buscar_avatar():
    resp_mock = Mock()  # Emula o response
    resp_mock.json.return_value = {  # Emula o respone.json()
        'login': 'renzo',
        'id': 402714,
        'avatar_url': 'https://avatars.githubusercontent.com/u/402714?v=4',
    }
    # Alterado o Objeto requests de github_api para o Teste Unitario
    github_api.requests.get = Mock(return_value=resp_mock)  # Atribui o resp_mock ao requests.get
    # Faz uma chamada normal com as alterações
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
