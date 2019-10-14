from django.test import TestCase
from django.core import mail

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fabio Jacob', cpf='27790490818', 
                    email='fabio.oj@gmail.com', phone='11-99116-5900')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscriptions_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'fabio.oj@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabio Jacob',
            '27790490818',
            'fabio.oj@gmail.com',
            '11-99116-5900',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
                