from django.test import TestCase
from .models import Pictures


class TestViews(TestCase):

    def test_index(self):
        response = self.client.get('/')
        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка контекста
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 0)

    def test_about(self):
        response = self.client.get('/about/')
        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка контекста
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 0)

    def test_create(self):
        response = self.client.get('/picpart/create/')
        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка контекста
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        self.assertEqual(len(response.context['object_list']), 0)

