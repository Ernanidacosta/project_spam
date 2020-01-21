import pytest

from db import Conexao
from modelos import Usuario


@pytest.fixture
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()



@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ernani')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Ernani'), Usuario(nome='Rose')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()