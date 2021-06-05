from PyKot import *


# PyKot to wrap variables (int, str, list)


def test(variable, condition):
    return f"{variable} passed" if condition is True else f"{variable} ***failed***"


print("----Base Types----")

a = PyKot("str")
print(test("str", a.status() == f"self.variable = str\n"
                                f"self.variable_type = str\n"
                                f"self.output_type = None\n"
                                f"self.identity = a = 'str'\n"
                                f"self.recall = False"))

b = PyKot(123)
print(test("int", b.status() == f"self.variable = 123\n"
                                f"self.variable_type = 1\n"
                                f"self.output_type = None\n"
                                f"self.identity = b = 123\n"
                                f"self.recall = False"))

c = PyKot((1, 2, 3))
print(test("tuple", c.status() == f"self.variable = (1, 2, 3)\n"
                                  f"self.variable_type = ('t', 'u', 'p', 'l', 'e')\n"
                                  f"self.output_type = None\n"
                                  f"self.identity = c = listOf(1, 2, 3)\n"
                                  f"self.recall = False"))

d = PyKot([1, 2, 3])
print(test("list", d.status() == f"self.variable = [1, 2, 3]\n"
                                 f"self.variable_type = []\n"
                                 f"self.output_type = None\n"
                                 f"self.identity = d = mutableListOf(1, 2, 3)\n"
                                 f"self.recall = False"))

print("----println(Base Types)----")

println(PyKot("str").status() == f"self.variable = str\n"
                                 f"self.variable_type = str\n"
                                 f"self.output_type = None\n"
                                 f"self.identity = println('str'\n"
                                 f"self.recall = False")

println(PyKot(123).status() == f"self.variable = 123\n"
                               f"self.variable_type = 1\n"
                               f"self.output_type = None\n"
                               f"self.identity = println(123\n"
                               f"self.recall = False")

println(PyKot((1, 2, 3)).status() == f"self.variable = (1, 2, 3)\n"
                                     f"self.variable_type = ('t', 'u', 'p', 'l', 'e')\n"
                                     f"self.output_type = None\n"
                                     f"self.identity = println(listOf(1, 2, 3)\n"
                                     f"self.recall = False")

println(PyKot([1, 2, 3]).status() == f"self.variable = [1, 2, 3]\n"
                                     f"self.variable_type = []\n"
                                     f"self.output_type = None\n"
                                     f"self.identity = println(mutableListOf(1, 2, 3)\n"
                                     f"self.recall = False")

print("----String Specific Methods----")

a = PyKot("test string").last_index()
print(test("last_index", a == 10))

b = PyKot("test string").drop(1).status()
print(test("drop", b == f"self.variable = est string\n"
                        f"self.variable_type = str\n"
                        f"self.output_type = None\n"
                        f"self.identity = b = 'test string'.drop(1)\n"
                        f"self.recall = True"))

c = PyKot("test string").drop_last(1).status()
print(test("drop_last", c == f"self.variable = test strin\n"
                             f"self.variable_type = str\n"
                             f"self.output_type = None\n"
                             f"self.identity = c = 'test string'.dropLast(1)\n"
                             f"self.recall = True"))

# d = dropWhile
print("d ***failed***")

# e = dropLastWhile
print("e ***failed***")

f = PyKot("test string").length()
print(test("length", f == 11))

g = PyKot("test string").first().status()
print(test("first", g == f"self.variable = t\n"
                         f"self.variable_type = str\n"
                         f"self.output_type = None\n"
                         f"self.identity = g = 'test string'.first()\n"
                         f"self.recall = True"))

h = PyKot("test string").last().status()
print(test("last", h == f"self.variable = g\n"
                        f"self.variable_type = str\n"
                        f"self.output_type = None\n"
                        f"self.identity = h = 'test string'.last()\n"
                        f"self.recall = True"))

i = PyKot("   |test string").trim_margin().status()
print(test("trim_margin", i == f"self.variable = test string\n"
                               f"self.variable_type = str\n"
                               f"self.output_type = None\n"
                               f"self.identity = i = '   |test string'.trimMargin('|')\n"
                               f"self.recall = True"))

j1 = PyKot("test string").compare_to("TesT STring")
print(test("compare_to_v1", j1 == -1))
j2 = PyKot("test string").compare_to("test string")
print(test("compare_to_v2", j2 == 0))
j3 = PyKot("test string").compare_to("zest string")
print(test("compare_to_v3", j3 == 1))
j4 = PyKot("test string").compare_to("TesT STring", True)
print(test("compare_to_v4", j4 == 0))

k = PyKot("test string").sub_string(7, 11).status()
print(test("sub_string", k == f"self.variable = ring\n"
                              f"self.variable_type = str\n"
                              f"self.output_type = None\n"
                              f"self.identity = k = 'test string'.subString(7, 11)\n"
                              f"self.recall = True"))

l1 = PyKot("test string").split()
print(test("split_v1", l1 == ['test', 'string']))
l2 = PyKot("test string").split("t")
print(test("split_v2", l2 == ['', 'es', ' s', 'ring']))
l3 = PyKot("test string").split(regex(r'\s'))
print(test("split_v3", l3 == ['test', 'string']))
l4 = PyKot("test string").split(regex(r'^(.*?)\s'))
print(test("split_v4", l4 == ['', 'test', 'string']))
l5 = PyKot("TesT STring").split("st", ignorecase=True)
print(test("split_v5", l5 == ['Te', ' ', 'ring']))

m = PyKot("test").plus(" string").status()
print(test("plus", m == f"self.variable = test string\n"
                        f"self.variable_type = str\n"
                        f"self.output_type = None\n"
                        f"self.identity = m = 'test'.plus(' string')\n"
                        f"self.recall = True"))

n = PyKot("test string").sub_sequence(2, 4).status()
print(test("sub_sequence", n == f"self.variable = st\n"
                                f"self.variable_type = str\n"
                                f"self.output_type = None\n"
                                f"self.identity = n = 'test string'.subSequence(2, 4)\n"
                                f"self.recall = True"))

o = PyKot("test\nstring").lines()
print(test("lines", o == ['test', 'string']))

p = PyKot('test string').capitalize().status()
print(test("capitalize", p == f"self.variable = Test string\n"
                              f"self.variable_type = str\n"
                              f"self.output_type = None\n"
                              f"self.identity = p = 'test string'.capitalize()\n"
                              f"self.recall = True"))

print("---- Shared String/List/MutableList Specific Methods----")

h = "nopqrstuvwxyz"
