# testreport-ng


[![PyPI version](https://badge.fury.io/py/testreportng.svg)](https://badge.fury.io/py/testreportng)
![CI Status](https://github.com/williamfzc/testreportng/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/williamfzc/testreportng/branch/master/graph/badge.svg?token=18PMrmYcAk)](https://codecov.io/gh/williamfzc/testreportng)

next generation of test report, for unittest.

## goal

`unittest` is the standard library of Python. It's powerful and robust, but not designed for human I think.

Because of its weird API, I have already felt tired to hack `unittest` again, again and again. This package offers a middle layer, which is really easy to extend, on the top of `unittest`. 

Based on this repo, you can easily get results from cases or suites, build your own report, or something else. 

## example

```bash
pip install testreportng
```

`NGCase` is a subclass of `unittest.TestCase`, with result collector.

```python
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
    # same as unittest.TestCase
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(NewCase))
    runner.run(suite)
    
    # after running, you can access results easily (NGResult object)
    result = NewCase.ng_result
    print(result.to_json())

    for name, case in result.to_dict().items():
        print(f"case: {name}, result: {case}")
        print(type(case.error), case.error, case.traceback)
```

more example:

- [working with `suite`](./example/suite.py)
- [hook](./example/hook.py)
- [build your own html report](./example/report.py)
- ...

## design

Without stepping into `unittest`, this repo builds another layer for plugins. Developers can easily build their own functions / tools without accessing `unittest` itself.

## why not ...

### py.test?

Personal preferences. `unittest` is a built-in package, and I prefer the standard way.

### other third-party runner?

The most of them hacked the `unittest` module directly. So if you want to add some new functions or do some customization, you need to access `unittest` too ... with its weird API.

some eg:

- tungwaiwip / [HTMLTestRunner](https://github.com/tungwaiyip/HTMLTestRunner)
- oldani / [HtmlTestRunner](https://github.com/oldani/HtmlTestRunner)
- ...

actually they nearly do the same things, with lots of redundant codes between them. I do not think build another runner is a good-enough idea to save our time.

## requirements

- python 3.6+ (because of typing hints)
- and nothing else

## license

[MIT](LICENSE)
