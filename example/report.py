from testreportng.case import NGCase
from testreportng.suite import NGSuite, NGLoader
import unittest

# need jinja2 for rendering
from jinja2 import Template

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
        <tr>
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


class NewCase(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase1(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase2(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


class NewCase5(NGCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = NGSuite(
        (
            NGSuite(NGLoader().loadTestsFromTestCase(NewCase)),
            NGSuite(
                (
                    NGLoader().loadTestsFromTestCase(NewCase1),
                    NGLoader().loadTestsFromTestCase(NewCase2),
                )
            ),
        )
    )
    runner.run(suite)
    result = suite.ng_result

    # building your own report has become very simple
    test_name = "example_test"
    html_template = Template(TEMPLATE)
    content = html_template.render(
        test_name=test_name,
        test_result=result,
    )
    with open(f"{test_name}.html", "w+") as f:
        f.write(content)
