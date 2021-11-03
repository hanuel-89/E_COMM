from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test  category model data insertion/types/field attributes.
        """
        data = self.data1

        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Test  category model return attribute name.
        """
        data = self.data1

        self.assertEqual(str(data), 'django')


class TestProductsModels(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='iPhoneX',
            created_by_id=1, slug='iPhoneX',
            price='20.00', image='iPhone'
            )

    def test_product_model_entry(self):
        """ Test  category model data insertion/types/field attributes. """
        data = self.data1

        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'iPhoneX')
