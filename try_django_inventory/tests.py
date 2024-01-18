from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os

class TreyDjangoSettingsTest(TestCase):

    def test_secret_key(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        try:
            is_valid = validate_password(SECRET_KEY) # Raise an exception if password too common
        except Exception as e:
            self.fail(e)
