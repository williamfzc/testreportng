import unittest

from testreportng.collector import NGCaseResult, NGCollector


class NGCase(unittest.TestCase):
    # default cls
    ng_result_cls = NGCaseResult
    ng_collector_cls = NGCollector

    # result collector
    ng_result: NGCollector

    # ng hook
    def _start_hook(self, name: str):
        mapping = {
            NGCaseResult.STATUS_PASS: "when_pass",
            NGCaseResult.STATUS_FAIL: "when_fail",
            NGCaseResult.STATUS_ERROR: "when_error",
            NGCaseResult.STATUS_SKIP: "when_skip",
            NGCaseResult.STATUS_INIT: "when_init",
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
        cls.ng_result: NGCollector = cls.ng_collector_cls()

    def setUp(self) -> None:
        # init this case
        cur = self.ng_result_cls(self._testMethodName)
        self.ng_result.set(cur)

    def tearDown(self) -> None:
        # update case's result
        cur = self.ng_result.get(self._testMethodName)
        cur.outcome = getattr(self, "_outcome")
        self.ng_result.set(cur)

        # ng hook
        self._start_hook(cur.status)
