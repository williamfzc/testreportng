import typing
import json

from testreportng.detail import NGCaseDetail


class NGResult(object):
    def __init__(self):
        self.data: typing.Dict[str, NGCaseDetail] = dict()

    def set(self, cur: NGCaseDetail):
        self.data[cur.name] = cur

    def get(self, name: str) -> typing.Optional[NGCaseDetail]:
        if name not in self.data:
            return None
        return self.data[name]

    def to_dict(self, safe_repr: bool = None) -> typing.Dict[str, dict]:
        """
        dump Result to dict, for easier usage by others

        :param safe_repr:
            bool.
            dump all the objects to string if True.
            default to False.
        :return:
        """
        r = dict()
        for name, result in self.data.items():
            r[name] = result.to_dict(safe_repr=safe_repr)
        return r

    def to_json(self) -> str:
        """
        dump Detail to json string

        :return:
        """
        r = self.to_dict(True)
        return json.dumps(r)

    def __str__(self):
        return f"<{__class__.__name__} result={self.data}>"

    __repr__ = __str__
