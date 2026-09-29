import os
from unittest import mock

from django.conf import settings
from django.test import SimpleTestCase

from users import views


class GeminiConfigTests(SimpleTestCase):
    def test_get_gemini_api_key_prefers_environment(self):
        with mock.patch.dict(os.environ, {"GOOGLE_API_KEY": "env-key"}, clear=False):
            self.assertEqual(views.get_gemini_api_key(), "env-key")

    def test_get_gemini_api_key_falls_back_to_settings(self):
        with mock.patch.object(settings, "GOOGLE_API_KEY", "settings-key", create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                self.assertEqual(views.get_gemini_api_key(), "settings-key")
