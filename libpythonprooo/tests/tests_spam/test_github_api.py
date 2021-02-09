from unittest.mock import Mock

import pytest

from libpythonprooo import github_api


@pytest.fixture
def avatar_url(mocker):  # Utiliza a fixture mocker do pytest-mock
    resp_mock = Mock()  # Emula o response
    avatar = 'https://avatars.githubusercontent.com/u/402714?v=4'
    resp_mock.json.return_value = {  # Emula o respone.json()
        'login': 'renzo',
        'id': 402714,
        'avatar_url': avatar,
    }
    # Setup     # endereco completo
    get_mock = mocker.patch('libpythonprooo.github_api.requests.get')
    # Alterado o Objeto requests de github_api para o Teste Unitario
    get_mock.return_value = resp_mock  # Atribui o resp_mock ao requests.get
    return avatar


# Módulo como Objeto: Iniciando
# Teste buscar avatar
# 1 Isolando testes, 2 - contruir o Mock(Substitui as funçõe do módulo original)

def test_buscar_avatar(avatar_url):
    # Faz uma chamada normal com as alterações
    url = github_api.buscar_avatar('renzon')
    assert url == avatar_url


# Isolamento de Imports / Teste de integração que faz busca na api do github
def test_buscar_avatar_integrao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url

# Bibliotéca Pytest-mock
# o mock faz a funcao de restaurar o lib de volta ao original
