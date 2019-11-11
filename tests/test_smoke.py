from reportng.case import NGCase
import unittest


def test_smoke():
    class NewCase(NGCase):
        def test_pass(self):
            self.assertTrue(True)

        def test_fail(self):
            self.assertTrue(False)

        def test_error(self):
            raise RuntimeError

    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)

    result = NewCase.ng_result
    print(result.to_json())

    for name, case in result.to_dict().items():
        if name == "test_pass":
            assert case.status == case.STATUS_PASS
        elif name == "test_fail":
            assert case.status == case.STATUS_FAIL
        else:
            assert case.status == case.STATUS_ERROR
