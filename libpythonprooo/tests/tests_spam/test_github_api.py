from unittest.mock import Mock

import pytest

from libpythonprooo import github_api


# Módulo como Objeto: Iniciando
# Teste buscar avatar
# 1 Isolando testes, 2 - contruir o Mock(Substitui as funçõe do módulo original)

def test_buscar_avatar(avatar_url):
    # Faz uma chamada normal com as alterações
    url = github_api.buscar_avatar('renzo')
    assert url == avatar_url


@pytest.fixture
def avatar_url():
    resp_mock = Mock()  # Emula o response
    avatar = 'https://avatars.githubusercontent.com/u/402714?v=4'
    resp_mock.json.return_value = {  # Emula o respone.json()
        'login': 'renzo',
        'id': 402714,
        'avatar_url': avatar,
    }
    # Setup
    # get original
    get_original = github_api.requests.get
    # Alterado o Objeto requests de github_api para o Teste Unitario
    github_api.requests.get = Mock(return_value=resp_mock)  # Atribui o resp_mock ao requests.get
    yield avatar
    # Tear Down
    github_api.requests.get = get_original


# Isolamento de Imports / Teste de integração que faz busca na api do github
def test_buscar_avatar_integrao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
