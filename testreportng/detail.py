import traceback
import json


class NGCaseDetail(object):
    STATUS_INIT: str = "init"
    STATUS_PASS: str = "pass"
    STATUS_FAIL: str = "fail"
    STATUS_ERROR: str = "error"
    STATUS_SKIP: str = "skip"

    def __init__(self, name: str, status: str = None):
        if not status:
            status = self.STATUS_INIT
        self.name: str = name
        self.status: str = status

        # data
        self._outcome = None

        # skip
        self.reason: str = ""

        # error
        self.error = None
        self.traceback = None

    def to_json(self) -> str:
        """
        dump Detail to json string

        :return:
        """
        res_dict = self.to_dict(safe_repr=True)
        return json.dumps(res_dict)

    def to_dict(self, safe_repr: bool = None) -> dict:
        """
        dump Detail to dict, for easier usage by others

        :param safe_repr:
            bool.
            dump all the objects to string if True.
            default to False.
        :return:
        """
        if safe_repr:
            return {
                "name": self.name,
                "status": self.status,
                "reason": self.reason,
                "error": repr(self.error) if self.error else "",
                "traceback": traceback.format_tb(self.traceback)
                if self.traceback
                else "",
            }
        return self.__dict__

    @property
    def outcome(self):
        """
        origin _outcome. same as unittest.TestCase

        :return:
        """
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        self._outcome = value

        # skipped
        if value.skipped:
            self.status = self.STATUS_SKIP
            self.reason = value.skipped[0][1]
            return

        # normal test
        error = value.errors[1][1]

        # no error happened
        if not error:
            self.status = self.STATUS_PASS
            return

        # error or fail
        if error[0] is AssertionError:
            self.status = self.STATUS_FAIL
        else:
            self.status = self.STATUS_ERROR

        self.error = error[1]
        self.traceback = error[2]

    def __str__(self):
        return f"<{__class__.__name__} name={self.name} status={self.status}>"

    __repr__ = __str__
