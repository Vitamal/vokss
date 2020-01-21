from .develop_and_test_settings_common import *


# Disable migrations when running tests
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()
DJANGO_CRADMIN_INCLUDE_TEST_CSS_CLASSES = True
LANGUAGE_CODE = 'en'  # We test against the english original text

# Faster tests with less time spent on hashing passwords
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)
