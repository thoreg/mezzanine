from django.test import TestCase

from mezzanine.utils.models import get_user_model
from mezzanine.core.managers import DisplayableManager

User = get_user_model()


class Tests(TestCase):

    def test_searchable_manager_search_fields(self):
        """
        Test that SearchableManager can get appropriate params.
        """
        manager = DisplayableManager()
        self.assertFalse(manager._search_fields)
        manager = DisplayableManager(search_fields={'foo': 10})
        self.assertTrue(manager._search_fields)
