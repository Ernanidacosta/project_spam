class Conexao(object):
    def gerar_sessao(self):
        pass


class Usuario(object):
    pass


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Ernani')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Ernani', Usuario='Rose')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()