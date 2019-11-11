import unittest

from testreportng.result import NGCaseDetail, NGResult


class NGCase(unittest.TestCase):
    # default cls
    ng_detail_kls = NGCaseDetail
    ng_result_kls = NGResult

    # result inst
    ng_result: NGResult

    # ng hook
    def _start_hook(self, name: str):
        mapping = {
            NGCaseDetail.STATUS_PASS: "when_pass",
            NGCaseDetail.STATUS_FAIL: "when_fail",
            NGCaseDetail.STATUS_ERROR: "when_error",
            NGCaseDetail.STATUS_SKIP: "when_skip",
            NGCaseDetail.STATUS_INIT: "when_init",
        }
        assert name in mapping, f"hook [ {name} ] not found"
        target = mapping[name]
        assert hasattr(self, target)
        return getattr(self, target)()

    def when_pass(self):
        pass

    def when_fail(self):
        pass

    def when_error(self):
        pass

    def when_skip(self):
        pass

    def when_init(self):
        pass

    # origin hook
    @classmethod
    def setUpClass(cls) -> None:
        cls.ng_result: NGResult = cls.ng_result_kls()

    def setUp(self) -> None:
        # init this case
        cur = self.ng_detail_kls(self._testMethodName)
        self.ng_result.set(cur)

    def tearDown(self) -> None:
        # update case's result
        cur = self.ng_result.get(self._testMethodName)
        cur.outcome = getattr(self, "_outcome")
        self.ng_result.set(cur)

        # ng hook
        self._start_hook(cur.status)
