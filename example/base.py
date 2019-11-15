from testreportng import NGCase
from testreportng import NGResult
import unittest


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True, "aaa")

    def test_fail(self):
        self.assertTrue(False, "bbb")

    def test_error(self):
        raise RuntimeError("ccc")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)

    # NGCase.ng_result: NGResult
    result: NGResult = NewCase.ng_result

    # you can access its data (dict) directly
    for name, case in result.data.items():
        # name: case's name
        # case: CaseDetail object
        print(f"case: {name}, result: {case}")

        # use CaseDetail directly
        print(
            case.name,
            case.outcome,
            case.status,
            case.error,
            case.traceback,
            # ...
        )

    # or, a total summary?
    print(result.summary())
