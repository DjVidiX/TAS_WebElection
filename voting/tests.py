from django.test import TestCase
from voting.models import Partia


class PartiaAddTestCase(TestCase):
    def setUp(self):
        Partia.objects.create(nazwa='Testowa Partia', skrot='TP')

    def getPartia(self):
        tp = Partia.objects.get(nazwa='Testowa Partia')
        self.assertEqual(tp.skrot,'ZP')
