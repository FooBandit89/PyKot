from PyKot import *


def test(method, condition):
    return f"{method} passed" if condition is True else f"{method} ***failed***"


def run_tests():
    print("----Base Types----")

    a = PyKot("str")
    print(test("str", a.variable == "str"))

    b = PyKot(123)
    print(test("int", b.variable == 123))

    c = PyKot((1, 2, 3))
    print(test("tuple", c.variable == (1, 2, 3)))

    d = PyKot([1, 2, 3])
    print(test("list", d.variable == [1, 2, 3]))

    e = PyKot({1: "one", 2: "two"})
    print(test("dict", e.variable == {1: "one", 2: "two"}))

    print("----println(Base Types)----")

    println(PyKot("str").variable == "str")

    println(PyKot(123).variable == 123)

    println(PyKot((1, 2, 3)).variable == (1, 2, 3))

    println(PyKot([1, 2, 3]).variable == [1, 2, 3])

    print("----String Specific Methods----")

    a = PyKot("test string").last_index()
    print(test("last_index", a == 10))

    b = PyKot("test string").drop(1).variable
    print(test("drop", b == "est string"))

    c = PyKot("test string").drop_last(1).variable
    print(test("drop_last", c == "test strin"))

    d = PyKot("DDDDtest string").drop_while(it() == "D").variable
    print(test("drop_while ( it == comparison )", d == "test string"))

    e = PyKot("test stringDDDD").drop_last_while(it() == "D").variable
    print(test("drop_last_while ( it == comparison )", e == "test string"))

    f = PyKot("test string").length()
    print(test("length", f == 11))

    g = PyKot("test string").first().variable
    print(test("first", g == "t"))

    h = PyKot("test string").last().variable
    print(test("last", h == "g"))

    i = PyKot("   |test string").trim_margin().variable
    print(test("trim_margin", i == "test string"))

    j1 = PyKot("test string").compare_to("TesT STring")
    print(test("compare_to_v1", j1 == -1))
    j2 = PyKot("test string").compare_to("test string")
    print(test("compare_to_v2", j2 == 0))
    j3 = PyKot("test string").compare_to("zest string")
    print(test("compare_to_v3", j3 == 1))
    j4 = PyKot("test string").compare_to("TesT STring", True)
    print(test("compare_to_v4", j4 == 0))

    k = PyKot("test string").sub_string(7, 11).variable
    print(test("sub_string", k == "ring"))

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

    m = PyKot("test").plus(" string").variable
    print(test("plus", m == "test string"))

    n = PyKot("test string").sub_sequence(2, 4).variable
    print(test("sub_sequence", n == "st"))

    o = PyKot("test\nstring").lines()
    print(test("lines", o == ['test', 'string']))

    p = PyKot("test string").capitalize().variable
    print(test("capitalize", p == "Test string"))

    print("---- Shared String/List/MutableList Specific Methods----")

    a1 = PyKot("test string").get(5).variable
    print(test("String.get()", a1 == "s"))
    a2 = PyKot([1, 2, 3]).get(2).variable
    print(test("List.get()", a2 == 3))
    a3 = PyKot((1, 2, 3)).get(1).variable
    print(test("Tuple.get()", a3 == 2))

    b1 = PyKot("test string").any("string")
    print(test("String.any()", b1))
    b2 = PyKot([1, 2, 3]).any(2)
    print(test("List.any()", b2))
    b3 = PyKot((1, 2, 3)).any(4)
    print(test("Tuple.any()", not b3))

    print("---- Shared String/Int/List/MutableList/Array Specific Methods----")

    a1 = PyKot("test string").to_string()
    print(test("String.to_string()", a1 == "test string"))
    a2 = PyKot(123).to_string()
    print(test("Int.to_string()", a2 == "123"))
    a3a = PyKot([1, 2, 3]).to_string()
    print(test("List.to_string()", a3a == "[1, 2, 3]"))
    a3b = PyKot([]).to_string()
    print(test("empty List.to_string()", a3b == "[]"))
    a4a = PyKot((1, 2, 3)).to_string()
    print(test("Tuple.to_string()", a4a == "(1, 2, 3)"))
    a4b = PyKot(()).to_string()
    print(test("empty Tuple.to_string()", a4b == "()"))
    a4c = PyKot((1,)).to_string()
    print(test("singleton Tuple.to_string()", a4c == "(1,)"))
    a5a = array_of(1, 2, 3).to_string()
    print(test("Array.to_string()", a5a == "[1, 2, 3]"))
    a5b = array_of().to_string()
    print(test("empty arrayOf().to_string()", a5b == "[]"))
    a6a = PyKot(range(2)).to_string()
    print(test("range.to_string()", a6a == "range(0, 2)"))
    a6b = PyKot(range(0)).to_string()
    print(test("empty range.to_string()", a6b == "range(0, 0)"))

    print("---- Shared List/MutableList Specific Methods----")

    a1 = PyKot((1, 2, 3)).to_list()
    print(test("Tuple.to_list()", a1 == (1, 2, 3)))
    a2 = PyKot([1, 2, 3]).to_list()
    print(test("List.to_list()", a2 == (1, 2, 3)))

    # find

    z1 = elvis_operator(None, "was None")
    print(test("elvis with None", z1 == "was None"))
    z2 = elvis_operator("return if not None", "alternative return")
    print(test("elvis operator", z2 == "return if not None"))
    variable = 1
    z3 = elvis_operator(variable, "was None")
    print(test("elvis with variable", z3 == 1))

    # list/tuple/dict

    a = PyKot(("one", "two", "three", "four"))
    print(test("filter(it.length > 3)", a.filter(it().length() > 3).variable == ['three', 'four']))


run_tests()


