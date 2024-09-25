import time
from copy import deepcopy


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def Green(s):
    return f"{bcolors.OKGREEN}{s}{bcolors.ENDC}"


def Red(s):
    return f"{bcolors.FAIL}{s}{bcolors.ENDC}"


class TestRunner:
    def __init__(self, fn) -> None:
        self.run = fn
        self.s = self.e = None
        self.input = None
        self.expected = None
        self.output = None

    def case(self, case):
        self.input = case["input"]
        self.expected = case["expected"]
        return self

    def test(self, serialize=(lambda x: x)):
        self.s = time.time()
        self.output = self.run(**deepcopy(self.input))
        self.e = time.time()
        if serialize(self.output) == serialize(self.expected):
            print(
                f"{Green('PASSED')} input: {self.input}"
                f", rt: {self.e - self.s}"
            )
        else:
            print(f"{Red('FAILED')} input: {self.input}")
            print(f"{'-'*6} expected: {Red(self.expected)}")
            print(f"{'-'*6} output: {Red(self.output)}")
        return self
