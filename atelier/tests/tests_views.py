from django.conf import settings

def test_language_using_cookie(self):
    self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'uk'})
    response = self.client.get('/')
    self.assertEqual(response.content, "Bienvenue sur mon site.")

def test_language_using_header(self):
    response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

from django.utils import translation

def test_language_using_override(self):
     with translation.override('fr'):
         response = self.client.get('/')
     self.assertEqual(response.content, b"Bienvenue sur mon site.")