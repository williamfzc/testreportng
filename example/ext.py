from testreportng import NGResult, NGCase, NGLoader, NGSuite
import unittest
import typing
from testreportng.ext import HtmlReporter


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


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = NGSuite(
        (
            NGLoader().loadTestsFromTestCase(NewCase),
            NGLoader().loadTestsFromTestCase(NewCase1),
            NGLoader().loadTestsFromTestCase(NewCase2),
        )
    )
    runner.run(suite)

    result: typing.Dict[str, NGResult] = suite.ng_result
    # more functions will be offered in online mode
    # offline = True by default
    html_content = HtmlReporter.render("YOUR_TEST_NAME", result, offline=True)

    with open("haha.html", "w+") as f:
        f.write(html_content)
