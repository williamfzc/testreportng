from testreportng import NGLoader, NGCase, NGSuite
from testreportng.result import NGResult
import unittest


def test_smoke():
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

    result = NewCase.ng_result
    suite_result = suite.ng_result

    # functions check
    print(result.to_json())
    assert result.get("not_existed_case") is None
    print(str(result))

    # result check
    for name, case in result.data.items():
        print(case.outcome)
        print(case.to_json())
        print(str(case))
        print(case.to_dict())
        if name == "test_pass":
            assert case.status == case.STATUS_PASS
        elif name == "test_fail":
            assert case.status == case.STATUS_FAIL
        elif name == "test_skip":
            assert case.status == case.STATUS_SKIP
            assert case.reason
        else:
            assert case.status == case.STATUS_ERROR

    for suite_name, each_suite in suite_result.items():
        assert suite_name
        assert isinstance(each_suite, NGResult)
