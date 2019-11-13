from jinja2 import Template
import typing

from testreportng.result import NGResult
from testreportng.case import NGCaseDetail

COLOR_DICT = {
    NGCaseDetail.STATUS_PASS: "#dff0d8",
    NGCaseDetail.STATUS_FAIL: "#fcf8e3",
    NGCaseDetail.STATUS_ERROR: "#f2dede",
    NGCaseDetail.STATUS_SKIP: "#ffffff",
    NGCaseDetail.STATUS_INIT: "#ffffff",
}

TEMPLATE = r"""
<!DOCTYPE html>
<html>
<head>
<title>{{ test_name }}</title>

<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
}
th {
  text-align: left;
}
</style>
</head>

<body>
<h1>{{ test_name }}</h1>
<table style="width:100%">
  <tr>
    <th>suite</th>
    <th>case</th>
    <th>status</th>
    <th>traceback</th>
  </tr>

  {% for suite_name, each in test_result.items() %}
    {% for each_case_name, each_case in each.to_dict(safe_repr=True).items() %}
        <tr style="background-color: {{ color_dict[each_case.status] }}">
          <td>{{ suite_name }}</td>
          <td>{{ each_case_name }}</td>
          <td>{{ each_case.status }}</td>
          <td>{{ each_case.traceback }}</td>
        </tr>
    {% endfor %}
  {% endfor %}
</table>

</body>
</html>
"""


class HtmlReporter(object):
    _template = TEMPLATE
    _default_test_name = "default"

    @classmethod
    def render(
        cls, test_name: str, result: typing.Union[typing.Dict[str, NGResult], NGResult]
    ) -> str:
        html_template = Template(TEMPLATE)
        if isinstance(result, NGResult):
            result = {cls._default_test_name: result}
        return html_template.render(
            test_name=test_name, test_result=result, color_dict=COLOR_DICT
        )
