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


def _green(s):
    return f"{BColors.OKGREEN}{s}{BColors.ENDC}"


def _red(s):
    return f"{BColors.FAIL}{s}{BColors.ENDC}"


class TestRunner:
    def __init__(self, fn) -> None:
        self.run = fn
        self.input = None
        self.expected = None

    def case(self, case):
        self.input = case["input"]
        self.expected = case["expected"]
        return self

    def test(self, serialize=(lambda x: x)):
        s = time.time()
        try:
            output = self.run(**deepcopy(self.input))
        except Exception:
            print(f"Runtime Error, input: {self.input}")
            print(_red(traceback.format_exc()))
            return
        e = time.time()
        if serialize(output) == serialize(self.expected):
            print(f"{_green('PASSED')} input: {self.input}, rt: {e - s}")
        else:
            print(f"{_red('FAILED')} input: {self.input}")
            print(f"{'-'*6} expected: {_red(self.expected)}")
            print(f"{'-'*6} output: {_red(output)}")
        return self
