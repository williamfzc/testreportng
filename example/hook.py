from testreportng.case import NGCase
import unittest


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError

    def when_pass(self):
        print("pass :)")

    def when_fail(self):
        print("fail :(")

    def when_error(self):
        print("error! x_x")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)
