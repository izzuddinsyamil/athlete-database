from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from athletedb.models import Sex


class ModelTests(TestCase):
    def setUp(self):
        sex = Sex(name='Laki')
        sex.save()

    def test_sex(self):
        sex = Sex.objects.get(name='Laki')
        expected_object_name = f'{sex.name}'
        self.assertEquals(expected_object_name, 'Laki')
