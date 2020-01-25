class Enviador:
    def __init__(self):
        self.quantidade_email_enviado = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email do remetente inválido: {remetente}')
        self.quantidade_email_enviado += 1
        return remetente


class EmailInvalido(Exception):
    pass