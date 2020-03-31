from unittest import TestCase

from scripts.consumer import Consumer


class Test(TestCase):
    def test_consumer(self):
        for msg in Consumer():
            print(msg)
