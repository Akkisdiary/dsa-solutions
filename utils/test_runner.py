import time


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
        self.output = self.run(**self.input)
        self.e = time.time()
        if serialize(self.output) == serialize(self.expected):
            print(f"input: {self.input} rt: {self.e-self.s}")
        else:
            print(f"input: {self.input} FAILED!")
            print(f"expected: {self.expected}")
            print(f"output: {self.output}")
        return self
