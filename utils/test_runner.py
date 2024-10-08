import time
import traceback
from copy import deepcopy


class BColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def _yellow(s):
    return f"{BColors.WARNING}{s}{BColors.ENDC}"


def _green(s):
    return f"{BColors.OKGREEN}{s}{BColors.ENDC}"


def _red(s):
    return f"{BColors.FAIL}{s}{BColors.ENDC}"


def _to_str(s, limit=30):
    s = str(s)
    if len(s) > limit:
        return f"{s[:limit]}..."
    return s


class TestRunner:
    def __init__(self, fn) -> None:
        self.run = fn

    def _test(self, test_no, case, serialize=(lambda x: x)):
        input = case["input"]
        expected = case["expected"]

        try:
            s = time.time()
            output = self.run(**deepcopy(input))
            e = time.time()

            input = _to_str(input)
            rt = round((e - s) * 1000, 6)
            if serialize(output) == serialize(expected):
                print(f"{test_no}. {_green('PASSED')} input={input}, {rt=}ms")
            else:
                pad = "." * (8 + len(str(test_no)))
                print(f"{test_no}. {_red('FAILED')} input={input}")
                print(f"{pad} expected: {_red(expected)}")
                print(f"{pad} output: {_red(output)}")
        except Exception:
            print(f"Runtime Error, input={input}")
            print(_red(traceback.format_exc()))

        return self

    def test(self, test_cases, serialize=(lambda x: x)):
        print(f"Testing {self.run}")
        for i in range(len(test_cases)):
            self._test(i, test_cases[i], serialize)
