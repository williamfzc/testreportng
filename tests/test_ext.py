from testreportng.ext import HtmlReporter
from testreportng.ext.html import TEMPLATE
from testreportng import NGCase, NGSuite, NGLoader, NGResultOperator

import unittest

TEST_NAME = "test_name"


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
    assert HtmlReporter.render(TEST_NAME, result)

    # test on merged result
    merged = NGResultOperator.merge(TEST_NAME, result)
    assert HtmlReporter.render(TEST_NAME, merged)

    # render a Result object
    result = list(result.values())[0]
    assert HtmlReporter.render(TEST_NAME, result)

    # custom HTML
    assert HtmlReporter.render(TEST_NAME, result, with_template=TEMPLATE)
