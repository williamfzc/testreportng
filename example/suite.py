from testreportng import NGResult, NGCase, NGLoader, NGSuite, NGResultOperator
import unittest
import typing


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

    # NGSuite.ng_result: typing.Dict[str, NGResult]
    result: typing.Dict[str, NGResult] = suite.ng_result

    # is a dict
    for each_name, each_suite in result.items():
        # name: suite name
        # suite: NGResult object
        print(each_name)
        print(each_suite)
        print(each_suite.summary())

    # or, you can use NGResultOperator to handle this dict easily
    operator = NGResultOperator()
    # load this dict
    operator.load(result)
    # merge all the suites into one
    new_suite = operator.merge("test suite name", result)
    print(new_suite.summary())
    # call its API !!
    # get total summary of these suites ?
    print(operator.summary())
