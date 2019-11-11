from testreportng.case import NGCase
import unittest


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError

    def test_skip(self):
        self.skipTest("test skip hook")

    def when_pass(self):
        print("pass :)")

    def when_fail(self):
        print("fail :(")

    def when_error(self):
        print("error! x_x")

    def when_skip(self):
        print("skip now")

    def when_always(self):
        print("always")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)
