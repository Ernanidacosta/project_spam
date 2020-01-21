import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def teste_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['kakizon@gmail.com', 'foo@bar.com']
)
def teste_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'ernanidacosta@gmail.com',
        'Teste de envio de spam',
        'Se recebeu esse email funciona!'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['kakizon', '']
)
def teste_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'ernanidacosta@gmail.com',
            'Teste de envio de spam',
            'Se recebeu esse email funciona!'
        )

