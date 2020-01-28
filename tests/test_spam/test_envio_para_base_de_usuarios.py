from unittest import mock
from unittest.mock import Mock

import pytest

from main import EnviadorDeSpam
from modelos import Usuario
from spam.enviador_de_email import Enviador


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.quantidade_email_enviado = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.quantidade_email_enviado += 1


@pytest.mark.parametrize(
    "usuarios",
    [
        [
            Usuario(nome='Ernani', email='ernanidacosta@gmail.coom'),
            Usuario(nome='Rose', email='roseane152@gmail.com')
        ],
        [
            Usuario(nome='Ernani', email='ernanidacosta@gmail.com')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Ernani', email='ernanidacosta@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kakizon@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
    enviador.enviar.assert_called_once_with(
        'kakizon@gmail.com',
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
