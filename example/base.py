from testreportng import NGCase
import unittest


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)

    result = NewCase.ng_result
    # result: NGResult object
    print(result.to_json())

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
