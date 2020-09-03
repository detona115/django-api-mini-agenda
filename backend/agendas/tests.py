from django.test import TestCase

# Create your tests here.

from .models import Agenda

class AgendaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Agenda.objects.create(
            date='2020-09-15T04:21:15-03:00',
            person='andy',
            subject='talk with client',
            priority='alta',
            place='varsovia',
            email='client@email.com',
            contact='+42 6842 5103'
        )

    def test_content(self):
        agenda = Agenda.objects.get(id=1)
        self.assertEquals(f'{agenda.date}', "2020-09-15 07:21:15+00:00")
        self.assertEquals(f'{agenda.person}', 'andy')
        self.assertEquals(f'{agenda.subject}', 'talk with client')
        self.assertEquals(f'{agenda.priority}', 'alta')
        self.assertEquals(f'{agenda.place}', 'varsovia')
        self.assertEquals(f'{agenda.email}', 'client@email.com')
        self.assertEquals(f'{agenda.contact}', '+42 6842 5103')
