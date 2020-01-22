from main import EnviadorDeSpam
from spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'ernanidacosta@gmail.com',
        'Teste envio de spam do PythonPro',
        'Se recebeu, fuunciona!!'
    )