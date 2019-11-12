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


class NewCase4(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase5(NGCase):
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
            NGSuite(
                (
                    NGLoader().loadTestsFromTestCase(NewCase1),
                    NGLoader().loadTestsFromTestCase(NewCase2),
                )
            ),
            NewCase3("test_pass"),
            NewCase3("test_fail"),
            NewCase3("test_error"),
            NGSuite(
                (
                    NGSuite(NGSuite(NGLoader().loadTestsFromTestCase(NewCase4))),
                    NGSuite(NGLoader().loadTestsFromTestCase(NewCase5)),
                )
            ),
        )
    )
    runner.run(suite)

    # a little different between Suite and Case
    # result is: typing.Dict[str, NGResult]
    result = suite.ng_result
    for each_name, each_suite in result.items():
        # name: suite name
        # suite: NGResult object
        print(each_name)
        print(each_suite)
