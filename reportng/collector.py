import typing

from reportng.result import NGCaseResult


class NGCollector(object):
    def __init__(self):
        self.result: typing.Dict[str, NGCaseResult] = dict()

    def set(self, result: NGCaseResult):
        self.result[result.name] = result

    def get(self, name: str) -> typing.Optional[NGCaseResult]:
        if name not in self.result:
            return None
        return self.result[name]

    def to_dict(self) -> typing.Dict[str, NGCaseResult]:
        return self.result

    def __str__(self):
        return f"<{__class__.__name__} result={self.result}>"

    __repr__ = __str__