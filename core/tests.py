from django.test import TestCase

from core.templatetags.core_extras import bizzfuzz


class CoreTestCase(TestCase):
    def test_bizz_fuzz(self):
        self.assertEqual(bizzfuzz(0), 'BizzFuzz')
        self.assertEqual(bizzfuzz(1), 1)
        self.assertEqual(bizzfuzz(3), 'Bizz')
        self.assertEqual(bizzfuzz(5), 'Fuzz')
        self.assertEqual(bizzfuzz(15), 'BizzFuzz')
