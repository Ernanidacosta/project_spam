from modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ernani', email='ernanidacosta@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Ernani', email='ernanidacosta@gmail.com'),
                Usuario(nome='Rose', email='ernanidacosta@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()