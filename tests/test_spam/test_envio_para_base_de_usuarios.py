import pytest

from main import EnviadorDeSpam
from modelos import Usuario
from spam.enviador_de_email import Enviador


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Ernani', email='ernanidacosta@gmail.com'),
            Usuario(nome='Rose', email='ernanidacosta@gmail.com')
        ],
        [
            Usuario(nome='Ernani', email='ernanidacosta@gmail.com'),
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, fuunciona!!'
    )
    assert len(usuarios) == enviador.quantidade_email_enviado
