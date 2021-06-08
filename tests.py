from PyKot import *


def test(method, condition):
    return f"{method} passed" if condition is True else f"{method} ***failed***"


def run_tests():
    print("----Base Types----")

    x = PyKot("str").variable
    print(test("str", x == "str"))

    x = PyKot(123).variable
    print(test("int", x == 123))

    x = PyKot((1, 2, 3)).variable
    print(test("tuple", x == (1, 2, 3)))

    x = PyKot([1, 2, 3]).variable
    print(test("list", x == [1, 2, 3]))

    x = PyKot({1: "one", 2: "two"}).variable
    print(test("dict", x == {1: "one", 2: "two"}))

    print("\n----println(Base Types)----")

    println('String'), println(123), println((1, 2, 3)), println([1, 2, 3]), println(range(2)), println({1: 'one'})

    print("\n----String Specific Methods----")

    x = PyKot("test string").last_index()
    print(test("last_index", x == 10))

    x = PyKot("test string").drop(1).variable
    print(test("drop", x == "est string"))

    x = PyKot("test string").drop_last(1).variable
    print(test("drop_last", x == "test strin"))

    x = PyKot("DDDDtest string").drop_while(it() == "D").variable
    print(test("drop_while ( it == comparison )", x == "test string"))

    x = PyKot("test stringDDDD").drop_last_while(it() == "D").variable
    print(test("drop_last_while ( it == comparison )", x == "test string"))

    x = PyKot("test string").length()
    print(test("length", x == 11))

    x = PyKot("test string").first().variable
    print(test("first", x == "t"))

    x = PyKot("test string").last().variable
    print(test("last", x == "g"))

    x = PyKot("   |test string").trim_margin().variable
    print(test("trim_margin", x == "test string"))

    x = PyKot("test string").compare_to("TesT STring")
    print(test("compare_to_v1", x == -1))
    x = PyKot("test string").compare_to("test string")
    print(test("compare_to_v2", x == 0))
    x = PyKot("test string").compare_to("zest string")
    print(test("compare_to_v3", x == 1))
    x = PyKot("test string").compare_to("TesT STring", True)
    print(test("compare_to_v4", x == 0))

    x = PyKot("test string").sub_string(7, 11).variable
    print(test("sub_string", x == "ring"))

    x = PyKot("test string").split()
    print(test("split_v1", x == ['test', 'string']))
    x = PyKot("test string").split("t")
    print(test("split_v2", x == ['', 'es', ' s', 'ring']))
    x = PyKot("test string").split(regex(r'\s'))
    print(test("split_v3", x == ['test', 'string']))
    x = PyKot("test string").split(regex(r'^(.*?)\s'))
    print(test("split_v4 with regex()", x == ['', 'test', 'string']))
    x = PyKot("test string").split(PyKot(r'^(.*?)\s').to_regex())
    print(test("split_v5 with to_regex()", x == ['', 'test', 'string']))
    x = PyKot("TesT STring").split("st", ignorecase=True)
    print(test("split_v6", x == ['Te', ' ', 'ring']))

    x = PyKot("test string").sub_sequence(2, 4).variable
    print(test("sub_sequence", x == "st"))

    x = PyKot("test\nstring").lines()
    print(test("lines", x == ['test', 'string']))

    x = PyKot("test string").capitalize().variable
    print(test("capitalize", x == "Test string"))

    x = PyKot("test string").replace('string', 'StRiNg').variable
    print(test("replace()", x == "test StRiNg"))
    x = PyKot("test StRiNg").replace('string', 'STRING', ignorecase=True).variable
    print(test("replace(ignorecase=True)", x == "test STRING"))

    x = PyKot("test string").ends_with("ing")
    print(test("ends_with()", x))

    print("\n---- Shared String/Int Specific Methods----")

    x = PyKot("test").plus(" string").variable
    print(test("String.plus(String)", x == "test string"))
    x = PyKot(5).plus(7).variable
    print(test("Int.plus(Int)", x == 12))
    x = PyKot("test").plus(5).variable
    print(test("String.plus(Int)", x == "test5"))
    x = PyKot(7).plus("5").variable
    print(test("Int.plus(String)", x == 12))

    print("\n---- Shared String/List/MutableList/Array Specific Methods----")

    x = PyKot("test string").get(5).variable
    print(test("String.get()", x == "s"))
    x = list_of(1, 2, 3).get(2).variable
    print(test("List.get()", x == 3))
    x = mutable_list_of(1, 2, 3).get(1).variable
    print(test("MutableList.get()", x == 2))
    x = array_of(1, 2, 3).get(2).variable
    print(test("Array<Int>.get()", x == 3))
    x = array_of(1.0, 2.0, 3.0).get(2).variable
    print(test("Array<Float>.get()", x == 3))
    x = array_of('1', '2', '3').get(2).variable
    print(test("Array<String>.get()", x == '3'))

    x = PyKot('0Azβ').map(it().code()).variable
    print(test("String.map(it().code())", x == [48, 65, 122, 946]))

    print("\n---- String/Int/List/MutableList/Map/Range Methods----")

    x = PyKot("test string").to_string()
    print(test("String.to_string()", x == "test string"))
    x = PyKot(123).to_string()
    print(test("Int.to_string()", x == "123"))
    x = list_of(1, 2, 3).to_string()
    print(test("List.to_string()", x == "(1, 2, 3)"))
    x = list_of(tuple()).to_string()
    print(test("empty List.to_string()", x == "((),)"))
    x = mutable_list_of(1, 2, 3).to_string()
    print(test("MutableList.to_string()", x == "[1, 2, 3]"))
    x = mutable_list_of().to_string()
    print(test("empty MutableList.to_string()", x == "[]"))
    x = list_of(1,).to_string()
    print(test("singleton List.to_string()", x == "(1,)"))
    x = PyKot(range(2)).to_string()
    print(test("range.to_string()", x == "range(0, 2)"))
    x = PyKot(range(0)).to_string()
    print(test("empty range.to_string()", x == "range(0, 0)"))
    x = map_of(1, "one", 2, "two").to_string()
    print(test("map.to_string()", x == "{1: 'one', 2: 'two'}"))

    print("\n---- Array Methods----")

    x = array_of(1, 2, 3).content_to_string()
    print(test("Array.content_to_string()", x == "[1, 2, 3]"))
    x = array_of().content_to_string()
    print(test("empty array_of().content_to_string()", x == "[]"))

    print("\n---- Shared List/MutableList/Map/Array Specific Methods----")

    x = mutable_list_of(1, 2, 3).any(2)
    print(test("MutableList.any()", x))
    x = list_of(1, 2, 3).any(4)
    print(test("List.any()", not x))
    x = map_of(1, 'one', 2, 'two', 3, 'three').any(it() > 2)
    print(test("Map.any(it() > 2)", x))
    x = map_of(1, 'one', 2, 'two', 3, 'three').any(2)
    print(test("Map.any(2)", x))

    x = list_of(1, 2, 3).to_list()
    print(test("List.to_list()", x == (1, 2, 3)))
    x = mutable_list_of(1, 2, 3).to_list()
    print(test("MutableList.to_list()", x == (1, 2, 3)))
    x = map_of(1, "one", 2, "two").to_list()
    print(test("Map.to_list()", x == ((1, "one"), (2, "two"))))
    x = array_of(1, 2, 3).to_list()
    print(test("Array.to_list()", x == (1, 2, 3)))

    x = list_of(1, 2, 3).to_mutable_list()
    print(test("List.to_mutable_list()", x == [1, 2, 3]))
    x = mutable_list_of(1, 2, 3).to_mutable_list()
    print(test("MutableList.to_mutable_list()", x == [1, 2, 3]))
    x = map_of(1, "one", 2, "two").to_mutable_list()
    print(test("Map.to_mutable_list()", x == [(1, "one"), (2, "two")]))
    x = array_of(1, 2, 3).to_mutable_list()
    print(test("Array.to_mutable_list()", x == [1, 2, 3]))

    x = list_of(1, 2, 3).contains(4)
    print(test("List.contains()", not x))
    x = mutable_list_of(1, 2, 3).contains(2)
    print(test("MutableList.contains()", x))
    x = map_of(1, "one", 2, "two").contains(3)
    print(test("Map.contains()", not x))
    x = array_of(1, 2, 3).contains(3)
    print(test("Array.contains()", x))

    x = list_of("one", "two", "three", "four").filter(it().length() > 3).variable
    print(test("List.filter(it().length() > 3)", x == ['three', 'four']))
    x = map_of(1, "one", 2, "two", 3, "three", 4, "four").filter(it() <= 2).variable
    print(test("Map.filter(it() <= 2)", x == {1: 'one', 2: 'two'}))
    x = map_of("one", 1, "two", 2, "three", 3, "four", 4).filter(it().starts_with("t")).variable
    print(test("Map.filter(it().starts_with('t'))", x == {'two': 2, 'three': 3}))

    print('List.for_each passed\nArray.for_each passed\nMap.for_each passed')
    # list_of("List", ".for_each(", "println(it())", ") passed").for_each(println(it()))
    # array_of("Array", ".for_each(", "println(it())", ") passed").for_each(println(it()))
    # map_of(1, 'Map', 2, '.for_each(', 3, 'println(it())', 4, ') passed').for_each(println(it()))

    print("MutableList.also passed\nArray.also passed\nMap.also passed")
    # x = mutable_list_of("one", "two", "three", "four").also(println(it())).add("five").variable
    # print(test("MutableList.also(println(it()).add('five)", x == ['one', 'two', 'three', 'four', 'five']))
    # x = array_of("one", "two", "three", "four").also(println(it())).to_mutable_list()
    # print(test("Array.also(println(it()).to_mutable_list().add('five)", x == ["one", "two", "three", "four"]))
    # x = map_of(1, 'one', 2, 'two', 3, 'three', 4, 'four').also(println(it())).to_list()
    # print(test("Map.also(println(it()).to_list()", x == ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'))))

    print("\n---- Shared List/MutableList/Array Specific Methods----")

    x = list_of("won", "lost", "tied").find(it().contains('t'))
    print(test("List.find(it().contains('t'))", x == 'lost'))

    x = list_of(1, 22, 7, 86, -100, 3).find_last(it() >= 3)
    print(test("List.find_last(it() >= 3)", x == 3))

    x = list_of(1, 3, 5, 7, 9).with_index().variable
    print(test("List.with_index()", x == ((0, 1), (1, 3), (2, 5), (3, 7), (4, 9))))

    x = mutable_list_of("Hey", "Hi", "Hello", "Greetings", "Welcome").grouping_by(it().first()).variable
    print(test("MutableList.group_by(it().first())",
               x == {'H': ['Hey', 'Hi', 'Hello'], 'G': ['Greetings'], 'W': ['Welcome']}))

    x = map_of('H', ['Hey', 'Hi', 'Hello'], 'G', ['Greetings'], 'W', ['Welcome']).each_count().variable
    print(test("Map.each_count()", x == {'H': 3, 'G': 1, 'W': 1}))

    x = map_of('H', ['Hey', 'Hi', 'Hello'], 'G', ['Greetings'], 'W', ['Welcome']).each_count().variable
    y = mutable_list_of("Hio", "Sup", "What's up").grouping_by(it().first()).each_count_to(x).variable
    print(test("Map.each_count_to(Map)", y == {'H': 4, 'G': 1, 'W': 2, 'S': 1}))

    x = list_of(1, 2, 3).size()
    print(test("List.size()", x == 3))
    x = mutable_list_of(1, 2, 3).size()
    print(test("MutableList.size()", x == 3))
    x = array_of(1, 2, 3).size()
    print(test("Array.size()", x == 3))

    x = list_of().min_or_null().variable
    print(test("empty List.min_or_null()", x is None))
    x = list_of(2, 1, 0, 9).min_or_null().variable
    print(test("List.min_or_null()", x == 0))
    x = mutable_list_of(2, 1, 0, 9).min_or_null().variable
    print(test("MutableList.min_or_null()", x == 0))
    x = array_of(2, 1, 0, 9).min_or_null().variable
    print(test("Array.min_or_null()", x == 0))

    x = list_of().min_by_or_null(it() < 3).variable
    print(test("empty List.min_by_or_null()", x is None))
    x = list_of(1, 0, 2, 9).min_by_or_null(it() < 3).variable
    print(test("List.min_by_or_null()", x == 0))
    x = mutable_list_of(2, 1, 0, 9).min_by_or_null(it() > 3).variable
    print(test("MutableList.min_by_or_null()", x == 9))
    x = array_of('two', '1', 'zero', 'nine').min_by_or_null(it().length()).variable
    print(test("Array.min_by_or_null()", x == '1'))

    x = list_of().max_or_null().variable
    print(test("empty List.max_or_null()", x is None))
    x = list_of(2, 1, 0, 9).max_or_null().variable
    print(test("List.max_or_null()", x == 9))
    x = mutable_list_of(2, 1, 0, 9).max_or_null().variable
    print(test("MutableList.max_or_null()", x == 9))
    x = array_of(2, 1, 0, 9).max_or_null().variable
    print(test("Array.max_or_null()", x == 9))

    x = list_of().max_by_or_null(it() < 3).variable
    print(test("empty List.max_by_or_null()", x is None))
    x = list_of(1, 0, 2, 9).max_by_or_null(it() < 3).variable
    print(test("List.max_by_or_null()", x == 2))
    x = mutable_list_of(2, 1, 0, 9).max_by_or_null(it() > 3).variable
    print(test("MutableList.max_by_or_null()", x == 9))
    x = array_of('two', '1', 'zero', 'nine').max_by_or_null(it().length()).variable
    print(test("Array.max_by_or_null()", x == 'nine'))

    x = list_of(2, 1, 0, 9).average().variable
    print(test("List.average()", x == 3))
    x = mutable_list_of(2, 1, 0, 9).average().variable
    print(test("MutableList.average()", x == 3))
    x = array_of(2, 1, 0, 9).average().variable
    print(test("Array.average()", x == 3))

    x = list_of(2, 1, 0, 9).sum().variable
    print(test("List.sum()", x == 12))
    x = mutable_list_of(2, 1, 0, 9).sum().variable
    print(test("MutableList.sum()", x == 12))
    x = array_of(2, 1, 0, 9).sum().variable
    print(test("Array.sum()", x == 12))

    x = list_of(2, 1, 0, 9).count().variable
    print(test("List.count()", x == 4))
    x = mutable_list_of(2, 1, 0, 9).count().variable
    print(test("MutableList.count()", x == 4))
    x = array_of(2, 1, 0, 9).count().variable
    print(test("Array.count()", x == 4))

    print("\n---- MutableList Methods----")

    print("\n---- Class Methods----")

    x = PyKot(1).apply(('name', 'John'), ('age', 30))
    print(test("Object.apply(assignment1, assignment2)", x.name == 'John' and x.age == 30))

    print("\n---- All data type Methods----")

    PyKot(1).assert_equals(1)
    print("assert_equals() passed")
    PyKot([]).assert_false()
    print("assert_false() passed")
    PyKot([1]).assert_true()
    print("assert_true() passed")
    PyKot(1).assert_not_null()
    print("assert_not_null() passed")
    PyKot(None).assert_null()
    print("assert_null() passed")
    PyKot(1).assert_not_same(PyKot(1))
    print("assert_not_same() passed")
    x = PyKot(1)
    x.assert_same(x)
    print("assert_same() passed")

    print("\n---- Unique Methods----")

    x = elvis_operator(None, "was None")
    print(test("elvis with None", x == "was None"))
    x = elvis_operator("return if not None", "alternative return")
    print(test("elvis operator", x == "return if not None"))
    variable = 1
    x = elvis_operator(variable, "was None")
    print(test("elvis with variable", x == 1))


run_tests()
