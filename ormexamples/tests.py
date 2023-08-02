from django.test import TestCase
from ormexamples.models import Customer

# Create your tests here.
class CustomerTestCase(TestCase):
    def Setup(self):
        print('setup activity')
        #Customer.objects.create('Suryam')
        #Customer.objects.create('Mukkoteswara Rao')
        print('created')
    def test_customer_info(self):
        print('testing customer fuctionality')
        self.assertEqual(1,1)
        qs=Customer.objects.all()
        print(qs.count())
        #self.assertGreater(qs.count(),3)
        #e1=Customer.objects.get(name='Suryam')
        #e2=Customer.objects.get(name='Mukkotwswara Rao')
