from unittest import mock

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
class Enviadormock(Enviador):

    def __init__(self):
        super().__init__()
        self.quantidade_email_enviado = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)


def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviadormock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
    assert len(usuarios) == enviador.quantidade_email_enviado


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Ernani', email='ernanidacosta@gmail.com')
    sessao.salvar(usuario)
    enviador = Enviadormock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kakizon@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
    assert enviador.parametros_de_envio == (
        'kakizon@gmail.com',
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, funciona!!'
    )
