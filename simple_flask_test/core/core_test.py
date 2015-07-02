import unittest
from simple_flask.core.core import say_hallo


class SimpleFlaskBlueprintTest(unittest.TestCase):

    def test_say_hallo(self):
        self.assertEquals(say_hallo('Kalimaha'), 'Hallo Kalimaha from CORE!')
        self.assertEquals(say_hallo(), 'Hallo from CORE!')
