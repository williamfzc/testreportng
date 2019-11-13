from testreportng.ext import HtmlReporter
from testreportng import NGCase, NGSuite, NGLoader

import unittest


def test_html_reporter():
    class NewCase(NGCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

        def test_skip(self):
            self.skipTest("test skip hook")

    runner = unittest.TextTestRunner()
    suite = NGSuite(NGLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)
    result = suite.ng_result
    assert HtmlReporter.render("some_test", result)

    # render a Result object
    result = result.values()[0]
    assert HtmlReporter.render("some_test", result)
