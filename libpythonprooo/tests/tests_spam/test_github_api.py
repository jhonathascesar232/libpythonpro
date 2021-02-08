from libpythonprooo import github_api


# Módulo como Objeto: Iniciando
# Teste buscar avatar
# 1 Isolando testes

def test_buscar_avatar():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
