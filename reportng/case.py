import unittest

from reportng.collector import NGCaseResult, NGCollector


class NGCase(unittest.TestCase):
    # default cls
    _ng_result_cls = NGCaseResult
    _ng_collector_cls = NGCollector

    # result
    ng_result: NGCollector

    @classmethod
    def setUpClass(cls) -> None:
        cls.ng_result: NGCollector = cls._ng_collector_cls()

    def setUp(self) -> None:
        cur = self._ng_result_cls(self._testMethodName)
        self.ng_result.set(cur)

    def tearDown(self) -> None:
        cur = self.ng_result.get(self._testMethodName)
        cur.outcome = getattr(self, "_outcome")

        self.ng_result.set(cur)
