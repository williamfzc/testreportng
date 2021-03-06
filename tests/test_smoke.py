from testreportng import NGLoader, NGCase, NGSuite
from testreportng.result import NGResult, NGResultOperator
from testreportng.constants import Label

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

    # result operator
    operator = NGResultOperator()
    operator.add(result)
    assert operator.data
    operator.remove(result)
    assert not operator.data
    operator.add(result)
    operator.reset()
    assert not operator.data
    operator.add(result)
    print(operator.summary())
    print(operator.get_data_by_status(Label.LABEL_STATUS_PASS))

    # functions check
    print(result.to_json())
    assert result.get("not_existed_case") is None
    assert result.get(list(result.data.keys())[0])
    print(str(result))
    print(result.summary())
    print(result.pass_rate)
    print(result.fail_or_error_num)

    # result check
    for name, case in result.data.items():
        print(case.outcome)
        print(case.to_json())
        print(str(case))
        print(case.to_dict())
        if name == "test_pass":
            assert case.status == Label.LABEL_STATUS_PASS
        elif name == "test_fail":
            assert case.status == Label.LABEL_STATUS_FAIL
        elif name == "test_skip":
            assert case.status == Label.LABEL_STATUS_SKIP
            assert case.reason
        else:
            assert case.status == Label.LABEL_STATUS_ERROR

    for suite_name, each_suite in suite_result.items():
        assert suite_name
        assert isinstance(each_suite, NGResult)
