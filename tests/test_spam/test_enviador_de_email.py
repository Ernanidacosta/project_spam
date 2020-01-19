from spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    enviador.enviar(
        'kakizon@gmail.com',
        'ernanidacosta@gmail.com',
        'Teste de envio de spam',
        'Se recebeu esse email funciona!'
    )
