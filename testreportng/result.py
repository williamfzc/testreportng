import typing
import json

from testreportng.detail import NGCaseDetail


class NGResult(object):
    def __init__(self):
        self.result: typing.Dict[str, NGCaseDetail] = dict()

    def set(self, cur: NGCaseDetail):
        self.result[cur.name] = cur

    def get(self, name: str) -> typing.Optional[NGCaseDetail]:
        if name not in self.result:
            return None
        return self.result[name]

    def to_dict(self, safe_repr: bool = None) -> typing.Dict[str, dict]:
        r = dict()
        for name, result in self.result.items():
            r[name] = result.to_dict(safe_repr=safe_repr)
        return r

    def to_json(self) -> str:
        r = dict()
        for name, result in self.result.items():
            r[name] = result.to_dict(safe_repr=True)
        return json.dumps(r)

    def __str__(self):
        return f"<{__class__.__name__} result={self.result}>"

    __repr__ = __str__
