import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class UlpingTest():
    def __init__(self):
        pass


if __name__ == '__main__':
    unittest.main()
