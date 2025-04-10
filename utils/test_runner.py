import time
import traceback
from copy import deepcopy
from typing import Any, Callable, Dict, List, Type


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
    def __init__(self, fn: Callable) -> None:
        self.run = fn

    def _test(
        self, tid: Any, case: Dict, serialize: Callable = (lambda x: x)
    ) -> Type["TestRunner"]:
        input = case["input"]
        expected = case["expected"]

        input_str = _to_str(input)
        try:
            s = time.time()
            output = self.run(**deepcopy(input))
            e = time.time()

            rt = round((e - s) * 1000, 6)
            if serialize(output) == serialize(expected):
                print(f"{tid}. {_green('PASSED')} input={input_str}, {rt=}ms")
            else:
                pad = "." * (8 + len(str(tid)))
                print(f"{tid}. {_red('FAILED')} input={input_str}")
                print(f"{pad} expected: {_red(expected)}")
                print(f"{pad} output: {_red(output)}")
        except Exception:
            print(f"{tid}. {_red('ERROR')}  input={input_str}")
            print(_red(traceback.format_exc()))

        return self

    def test(
        self, test_cases: List[Dict], serialize: Callable = (lambda x: x)
    ) -> Type["TestRunner"]:
        fn_name = f"{self.run.__self__.__class__.__name__}.{self.run.__name__}"
        print(f"Testing {_yellow(fn_name)}")
        for i in range(len(test_cases)):
            self._test(i, test_cases[i], serialize)

        return self
