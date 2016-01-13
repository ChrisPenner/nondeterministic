from unittest import TestCase
from nd import ND

class TestND(TestCase):
    def test_something(self):
        x = ND(xrange(1,30))
        x *= 20
        x -= 12
        x.do_if(lambda x: x % 2 == 0, lambda x: x/2)
        print x



        self.assertSetEqual(x._set, set([3, 4, 5]))
