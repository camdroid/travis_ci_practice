import main
import unittest


class MyTest(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main.main())

    def test_no(self):
        self.assertFalse(main.no())

if __name__ == '__main__':
    unittest.main()
