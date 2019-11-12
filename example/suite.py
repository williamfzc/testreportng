from testreportng.case import NGCase
from testreportng.suite import NGSuite, NGLoader
import unittest


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase1(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase2(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase3(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = NGSuite(
        (
            NGSuite(NGLoader().loadTestsFromTestCase(NewCase)),
            NGSuite(NGLoader().loadTestsFromTestCase(NewCase1)),
            NGSuite(
                (
                    NGLoader().loadTestsFromTestCase(NewCase2),
                    NGLoader().loadTestsFromTestCase(NewCase3),
                )
            ),
        )
    )
    runner.run(suite)

    result = suite.ng_result
    print(result)
