from testreportng import NGResult, NGCase, NGLoader, NGSuite
import unittest
import typing


def test_setup_error():
    class SubCase(NGCase):
        def setUp(self) -> None:
            super(SubCase, self).setUp()
            raise RuntimeError

    class NewCase(SubCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

    class NewCase1(SubCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

    class NewCase2(SubCase):
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

    class NewCase4(SubCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

    class NewCase5(SubCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

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
