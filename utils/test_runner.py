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


class TestRunner:
    def __init__(self, fn, tc) -> None:
        self.run = fn
        self.test_cases = tc

    def _test(self, case, serialize=(lambda x: x)):
        input = case["input"]
        expected = case["expected"]

        try:
            s = time.time()
            output = self.run(**deepcopy(input))
            e = time.time()

            if serialize(output) == serialize(expected):
                print(f"{_green('PASSED')} input: {input}, rt: {e - s}")
            else:
                print(f"{_red('FAILED')} input: {input}")
                print(f"{'-'*6} expected: {_red(expected)}")
                print(f"{'-'*6} output: {_red(output)}")
        except Exception:
            print(f"Runtime Error, input: {input}")
            print(_red(traceback.format_exc()))

        return self

    def test(self, serialize=(lambda x: x)):
        for i in range(len(self.test_cases)):
            print(_yellow(f"Running test {i}..."))
            self._test(self.test_cases[i], serialize)
