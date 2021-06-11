from PyKot import *

debug = True

tests_passed = 0
tests_failed = 0


def report_card():
    if tests_passed < 10:
        string_tests_passed = f"0{tests_passed}"
    else:
        string_tests_passed = str(tests_passed)
    if tests_failed < 10:
        string_tests_failed = f"0{tests_failed}"
    else:
        string_tests_failed = str(tests_failed)
    print('\n')
    print(' ' * 20 + '*' * 56)
    print(' ' * 15 + '*' * 68)
    print(' ' * 10 + '*' * 15 + ' ' * 14 + '*' * 20 + ' ' * 14 + '*' * 15)
    print(f"{' ' * 6}{'*' * 17}   Tests Passed   {'*' * 16}   Tests Failed   {'*' * 17}")
    print(f"{' ' * 6}{'*' * 17}                  {'*' * 16}                  {'*' * 17}")
    print(f"{' ' * 6 + '*' * 17}{' ' * 7}{string_tests_passed}{' ' * 8}{'*' * 16}"
          f"{' ' * 8}{string_tests_failed}{' ' * 8}{'*' * 17}")
    print(' ' * 10 + '*' * 15 + ' ' * 14 + '*' * 20 + ' ' * 14 + '*' * 15)
    print(' ' * 15 + '*' * 68)
    print(' ' * 20 + '*' * 56)
    print(f"                    {len(it_function_dict) = }")


def section(title):
    if len(title) % 2 == 0:
        print(f"\n{'-' * (51 - (len(f' {title} ') // 2))}[ {title} ]{'-' * (51 - (len(f' {title} ') // 2))}")
    else:
        print(f"\n{'-' * (51 - (len(f' {title} ') // 2))}[ {title} ]{'-' * (50 - (len(f' {title} ') // 2))}")


def debug_test(input_var):
    if debug:
        print(f"Debug information: {input_var = }")


def test(method, input_var, expected_output):
    global tests_passed, tests_failed
    method_length = len(method)

    if isinstance(input_var, type(np.array([]))):
        input_var = unpack_array(input_var)
    if isinstance(expected_output, type(np.array([]))):
        expected_output = unpack_array(expected_output)

    if isinstance(input_var, type(PyKot(''))):
        input_var = input_var.var
    if isinstance(expected_output, type(PyKot(''))):
        expected_output = expected_output.var

    if input_var == expected_output:
        tests_passed += 1
        print(f"{method}    {'-' * (100 - method_length)}{' ' * 5}passed")
    else:
        tests_failed += 1
        print(f"{method}   {'-' * (100 - method_length)}{' ' * 2}***failed***")
    debug_test(input_var)


def run_tests():
    section('Base Types')

    test("String",
         PyKot("String").var,
         "String")

    test("Int",
         PyKot(123).var,
         123)

    test("List",
         PyKot((1, 2, 3)).var,
         (1, 2, 3))

    test("MutableList",
         PyKot([1, 2, 3]).var,
         [1, 2, 3])

    test("Map",
         PyKot({1: "one", 2: "two"}).var,
         {1: "one", 2: "two"})

    test("Array",
         unpack_array(array_of(1, 2, 3).var),
         unpack_array(np.array([1, 2, 3])))

    section('println(Base Types)')

    test("println('String')",
         println('String'),
         print('String'))

    test("println(123)",
         println(123),
         print(123))

    test("println((1, 2, 3))",
         println((1, 2, 3)),
         print((1, 2, 3)))

    test("println([1, 2, 3])",
         println([1, 2, 3]),
         print([1, 2, 3]))

    test("println(range(2))",
         println(range(2)),
         print(range(2)))

    test("println({1: 'one'})",
         println({1: 'one'}),
         print({1: 'one'}))

    test("println(array_of(1, 2, 3))",
         println(array_of(1, 2, 3).var),
         print(array_of(1, 2, 3).var))

    section('plus() Method')

    test("String.plus(String)",
         PyKot("test").plus(" string").var,
         "test string")
    test("Int.plus(Int)",
         PyKot(5).plus(7).var,
         12)
    test("String.plus(Int)",
         PyKot("test").plus(5).var,
         "test5")
    test("Int.plus(String)",
         PyKot(7).plus("5").var,
         12)

    section('get() Method')

    test("String.get()",
         PyKot("test string").get(5).var,
         "s")
    test("List.get()",
         list_of(1, 2, 3).get(2).var,
         3)
    test("MutableList.get()",
         mutable_list_of(1, 2, 3).get(1).var,
         2)
    test("Array<Int>.get()",
         array_of(1, 2, 3).get(2).var,
         3)
    test("Array<Float>.get()",
         array_of(1.0, 2.0, 3.0).get(2).var,
         3.0)
    test("Array<String>.get()",
         array_of('1', '2', '3').get(2).var,
         '3')

    section('code() Method')

    test("String.map(it().code())",
         PyKot('0Azβ').map(it().code()).var,
         (48, 65, 122, 946))

    section('last_index() Method')

    test("String.last_index()",
         PyKot("test string").last_index().var,
         10)

    test("List.last_index()",
         PyKot((1, 2, 3)).last_index().var,
         2)

    test("empty List.last_index()",
         PyKot(()).last_index().var,
         -1)

    test("MutableList.last_index()",
         PyKot([1, 2, 3]).last_index().var,
         2)

    test("Array.last_index()",
         array_of(1, 2, 3).last_index().var,
         2)

    section('drop() Method')

    test("String.drop()",
         PyKot("test string").drop(1).var,
         "est string")

    test("List.drop()",
         PyKot((1, 2, 3)).drop(1).var,
         (2, 3))

    test("MutableList.drop()",
         PyKot([1, 2, 3]).drop(1).var,
         [2, 3])

    test("Array.drop()",
         array_of(1, 2, 3).drop(1).var,
         np.array([2, 3]))

    section('drop_last() Method')

    test("String.drop_last()",
         PyKot("test string").drop_last(1).var,
         "test strin")

    test("List.drop_last()",
         PyKot((1, 2, 3)).drop_last(1).var,
         (1, 2))

    test("MutableList.drop_last()",
         PyKot([1, 2, 3]).drop_last(1).var,
         [1, 2])

    test("Array.drop_last()",
         array_of(1, 2, 3).drop_last(1).var,
         np.array([1, 2]))

    section('drop_while(it expression) Method')

    test("String.drop_while(it expression)",
         PyKot("DDDDtest string").drop_while(it() == "D").var,
         "test string")

    test("List.drop_while(it expression)",
         PyKot((0, 0, 0, 1, 2, 3)).drop_while(it() == 0).var,
         (1, 2, 3))

    test("MutableList.drop_while(it expression)",
         PyKot([0, 0, 0, 1, 2, 3]).drop_while(it() == 0).var,
         [1, 2, 3])

    test("Array.drop_while(it expression)",
         array_of(0, 0, 0, 1, 2, 3).drop_while(it() == 0).var,
         np.array([1, 2, 3]))

    section('drop_last_while(it expression) Method')

    test("String.drop_last_while(it expression)",
         PyKot("test stringDDDD").drop_last_while(it() == "D").var,
         "test string")

    test("List.drop_last_while(it expression)",
         PyKot((1, 2, 3, 0, 0, 0)).drop_last_while(it() == 0).var,
         (1, 2, 3))

    test("MutableList.drop_last_while(it expression)",
         PyKot([1, 2, 3, 0, 0, 0]).drop_last_while(it() == 0).var,
         [1, 2, 3])

    test("Array.drop_last_while(it expression)",
         array_of(1, 2, 3, 0, 0, 0).drop_last_while(it() == 0).var,
         np.array([1, 2, 3]))

    section('take() Method')

    test("String.take()",
         PyKot("test string").take(1).var,
         "t")

    test("List.take()",
         PyKot((1, 2, 3)).take(1).var,
         (1,))

    test("MutableList.take()",
         PyKot([1, 2, 3]).take(1).var,
         [1])

    test("Array.take()",
         array_of(1, 2, 3).take(1).var,
         np.array([1]))

    section('take_last() Method')

    test("String.take_last()",
         PyKot("test string").take_last(1).var,
         "g")

    test("List.take_last()",
         PyKot((1, 2, 3)).take_last(1).var,
         (3,))

    test("MutableList.take_last()",
         PyKot([1, 2, 3]).take_last(1).var,
         [3])

    test("Array.take_last()",
         array_of(1, 2, 3).take_last(1).var,
         np.array([3]))

    section('take_while(it expression) Method')

    test("String.take_while(it expression)",
         PyKot("DDDDtest string").take_while(it() == "D").var,
         "DDDD")

    test("List.take_while(it expression)",
         PyKot((0, 0, 0, 1, 2, 3)).take_while(it() == 0).var,
         (0, 0, 0))

    test("MutableList.take_while(it expression)",
         PyKot([0, 0, 0, 1, 2, 3]).take_while(it() == 0).var,
         [0, 0, 0])

    test("Array.take_while(it expression)",
         array_of(0, 0, 0, 1, 2, 3).take_while(it() == 0).var,
         np.array([0, 0, 0]))

    section('take_last_while(it expression) Method')

    test("String.take_last_while(it expression)",
         PyKot("test stringDDDD").take_last_while(it() == "D").var,
         "DDDD")

    test("List.take_last_while(it expression)",
         PyKot((1, 2, 3, 0, 0, 0)).take_last_while(it() == 0).var,
         (0, 0, 0))

    test("MutableList.take_last_while(it expression)",
         PyKot([1, 2, 3, 0, 0, 0]).take_last_while(it() == 0).var,
         [0, 0, 0])

    test("Array.take_last_while(it expression)",
         array_of(1, 2, 3, 0, 0, 0).take_last_while(it() == 0).var,
         np.array([0, 0, 0]))

    section('length() Method')

    test("String.length()",
         PyKot("test string").length(),
         11)

    test("List.length()",
         PyKot((1, 2, 3)).length(),
         3)

    test("MutableList.length()",
         PyKot([1, 2, 3]).length(),
         3)

    test("Array.length()",
         array_of(1, 2, 3).length(),
         3)

    section('first() Method')

    test("String.first()",
         PyKot("test string").first().var,
         "t")

    test("List.first()",
         list_of(1, 2, 3).first().var,
         1)

    test("MutableList.first()",
         mutable_list_of(1, 2, 3).first().var,
         1)

    test("Array.first()",
         array_of(1, 2, 3).first().var,
         1)

    section('last() Method')

    test("String.last()",
         PyKot("test string").last().var,
         "g")

    test("List.last()",
         list_of(1, 2, 3).last().var,
         3)

    test("MutableList.last()",
         mutable_list_of(1, 2, 3).last().var,
         3)

    test("Array.last()",
         array_of(1, 2, 3).last().var,
         3)

    section('trim_margin() Method')

    test("trim_margin",
         PyKot("   |test string").trim_margin().var,
         "test string")

    section('compare_to() Method')

    test("String.compare_to(STRING)",
         PyKot("test string").compare_to("TesT STring").var,
         1)
    test("String.compare_to(String)",
         PyKot("test string").compare_to("test string").var,
         0)
    test("String.compare_to(zString)",
         PyKot("test string").compare_to("zest string").var,
         -1)
    test("String.compare_to*(STRING, ignorecase=True",
         PyKot("test string").compare_to("TesT STring", ignorecase=True).var,
         0)

    test("Int.compare_to(Int)",
         PyKot(1).compare_to(2).var,
         -1)

    test("Int.compare_to(Int)",
         PyKot(1).compare_to(1).var,
         0)

    test("Int.compare_to(Int)",
         PyKot(1).compare_to(0).var,
         1)

    test("List.compare_to(List)",
         PyKot((1, 2)).compare_to((2, 3)).var,
         -1)

    test("Array.compare_to(Array)",
         array_of(1, 2).compare_to(np.array([2, 3])).var,
         -1)

    test("Map.compare_to(Map)",
         PyKot({1: 'one', 2: 'two'}).compare_to({2: 'two', 3: 'three'}).var,
         -1)

    section("substring() Method")

    test("sub_string",
         PyKot("test string").sub_string(7, 11).var,
         "ring")

    test("sub_string",
         PyKot("test string").sub_string(7, it().length()).var,
         "ring")

    test("sub_string",
         PyKot("test string").sub_string(it().length() - 4, it().length()).var,
         "ring")

    section("split() Method")

    test("split()",
         PyKot("test string").split().var,
         ('test', 'string'))

    test("split('t')",
         PyKot("test string").split("t").var,
         ('', 'es', ' s', 'ring'))

    test(r"split(regex(r'\s'))",
         PyKot("test string").split(regex(r'\s')).var,
         ('test', 'string'))

    test(r"split(regex(r'^(.*?)\s'))",
         PyKot("test string").split(regex(r'^(.*?)\s')).var,
         ('', 'test', 'string'))

    test(r"split(PyKot(r'^(.*?)\s').to_regex())",
         PyKot("test string").split(PyKot(r'^(.*?)\s').to_regex()).var,
         ('', 'test', 'string'))

    test(r"split('st', ignorecase=True)",
         PyKot("TesT STring").split("st", ignorecase=True).var,
         ('Te', ' ', 'ring'))

    test(r"split('s', 't')",
         PyKot("test string").split("s", "t").var,
         ('', 'e', '', ' ', '', 'ring'))

    test(r"split('s', 't', ignorecase=True)",
         PyKot("TesT STRing").split('s', 't', ignorecase=True).var,
         ('', 'e', '', ' ', '', 'Ring'))

    section("sub_sequence() Method")

    test("String.sub_sequence",
         PyKot("test string").sub_sequence(2, 4).var,
         "st")

    test("String.sub_sequence(Int, It().length())",
         PyKot("test string").sub_sequence(7, it().length()).var,
         "ring")

    section("lines() Method")

    test("String.lines()",
         PyKot("test\nstring").lines(),
         ['test', 'string'])

    section("capitalize() Method")

    test("String.capitalize",
         PyKot("test string").capitalize().var,
         "Test string")

    section("replace() Method")

    test("String.replace()",
         PyKot("test string").replace('string', 'StRiNg').var,
         "test StRiNg")

    test("String.replace(ignorecase=True)",
         PyKot("test StRiNg").replace('string', 'STRING', ignorecase=True).var,
         "test STRING")

    section('ends_with() Method')

    test("String.ends_with()",
         PyKot("test string").ends_with("ing"),
         True)

    test("List.ends_with()",
         list_of('looking', 'Stopping', 'loss').ends_with("ing"),
         False)

    test("MutableList.ends_with()",
         mutable_list_of('looking', 'Stopping', 'losing').ends_with("ing"),
         True)

    test("Array.ends_with()",
         array_of('look', 'Stopping', 'loss').ends_with("ing"),
         False)

    section('to_string() Method')

    test("String.to_string()",
         PyKot("test string").to_string(),
         "test string")

    test("Int.to_string()",
         PyKot(123).to_string(),
         "123")

    test("List.to_string()",
         list_of(1, 2, 3).to_string(),
         "(1, 2, 3)")

    test("empty List.to_string()",
         list_of(tuple()).to_string(),
         "((),)")

    test("MutableList.to_string()",
         mutable_list_of(1, 2, 3).to_string(),
         "[1, 2, 3]")

    test("empty MutableList.to_string()",
         mutable_list_of().to_string(),
         "[]")

    test("singleton List.to_string()",
         list_of(1, ).to_string(),
         "(1,)")

    test("range.to_string()",
         PyKot(range(2)).to_string(),
         "range(0, 2)")

    test("empty range.to_string()",
         PyKot(range(0)).to_string(),
         "range(0, 0)")

    test("map.to_string()",
         map_of(1, "one", 2, "two").to_string(),
         "{1: 'one', 2: 'two'}")

    section('content_to_string() Method')

    test("List.content_to_string()",
         PyKot((1, 2, 3)).content_to_string(),
         "[1, 2, 3]")

    test("MutableList.content_to_string()",
         PyKot([1, 2, 3]).content_to_string(),
         "[1, 2, 3]")

    test("Array.content_to_string()",
         array_of(1, 2, 3).content_to_string(),
         "[1, 2, 3]")

    test("empty array_of().content_to_string()",
         array_of().content_to_string(),
         "[]")

    section('any() Method')

    test("MutableList.any()",
         mutable_list_of(1, 2, 3).any(2),
         True)

    test("List.any()",
         list_of(1, 2, 3).any(4),
         False)

    test("Map.any(it() > 2)",
         map_of(1, 'one', 2, 'two', 3, 'three').any(it().key() > 2),
         True)

    test("Map.any(2)",
         map_of(1, 'one', 2, 'two', 3, 'three').any(2),
         True)

    test("empty_list().any()",
         empty_list().any(),
         False)

    test("empty_array().any()",
         empty_array().any(),
         False)

    section("none() Method")

    test("empty_list().none()",
         empty_list().none(),
         True)

    test("empty_array().none()",
         empty_array().none(),
         True)

    section("to_list() Method")

    test("List.to_list()",
         list_of(1, 2, 3).to_list(),
         (1, 2, 3))

    test("MutableList.to_list()",
         mutable_list_of(1, 2, 3).to_list(),
         (1, 2, 3))

    test("Map.to_list()",
         map_of(1, "one", 2, "two").to_list(),
         ((1, "one"), (2, "two")))

    test("Array.to_list()",
         array_of(1, 2, 3).to_list(),
         (1, 2, 3))

    section("to_mutable_lit() Method")

    test("List.to_mutable_list()",
         list_of(1, 2, 3).to_mutable_list(),
         [1, 2, 3])

    test("MutableList.to_mutable_list()",
         mutable_list_of(1, 2, 3).to_mutable_list(),
         [1, 2, 3])

    test("Map.to_mutable_list()",
         map_of(1, "one", 2, "two").to_mutable_list(),
         [(1, "one"), (2, "two")])

    test("Array.to_mutable_list()",
         array_of(1, 2, 3).to_mutable_list(),
         [1, 2, 3])

    section("contains() Method")

    test("List.contains()",
         list_of(1, 2, 3).contains(4),
         False)

    test("MutableList.contains()",
         mutable_list_of(1, 2, 3).contains(2),
         True)

    test("Map.contains()",
         map_of(1, "one", 2, "two").contains(3),
         False)

    test("Array.contains()",
         array_of(1, 2, 3).contains(3),
         True)

    section("filter() Method")

    test("List.filter(it().length() > 3)",
         list_of("one", "two", "three", "four").filter(it().length() > 3).var,
         ['three', 'four'])

    test("Map.filter(it().key() <= 2)",
         map_of(1, "one", 2, "two", 3, "three", 4, "four").filter(it().key() <= 2).var,
         {1: 'one', 2: 'two'})

    test("Map.filter(it().value().starts_with('t'))",
         map_of(1, "one", 2, "two", 3, "three", 4, "four").filter(it().value().starts_with("t")).var,
         {2: "two", 3: "three"})

    test("Map.filter(it().value().ends_with('e'))",
         map_of(1, "one", 2, "two", 3, "three", 4, "four").filter(it().value().ends_with("e")).var,
         {1: "one", 3: "three"})

    test("Map.filter(it().value().starts_with('t', ignorecase=True))",
         map_of(1, "one", 2, "Two", 3, "three", 4, "four").filter(
             it().value().starts_with("t", ignorecase=True)).var,
         {2: "Two", 3: "three"})

    test("Map.filter(it().value().ends_with('e', ignorecase=True))",
         map_of(1, "onE", 2, "two", 3, "three", 4, "four").filter(
             it().value().ends_with("e", ignorecase=True)).var,
         {1: "onE", 3: "three"})

    test("List.filter_not(it().length() > 3)",
         list_of("one", "two", "three", "four").filter_not(it().length() > 3).var,
         ['one', 'two'])

    test("Map.filter_not(it().key() <= 2)",
         map_of(1, "one", 2, "two", 3, "three", 4, "four").filter_not(it().key() <= 2).var,
         {3: 'three', 4: 'four'})

    test("Map.filter_not(it().value().starts_with('t'))",
         map_of(1, "one", 2, "two", 3, "three", 4, "four").filter_not(it().value().starts_with("t")).var,
         {1: "one", 4: "four"})

    section("filter_indexed()")

    test("List.filter_indexed(lambda a, b: a < b)",
         list_of(1, 3, 5, 2).filter_indexed(lambda a, b: a < b).var,
         [1, 3, 5])
    test("MutableList.filter_indexed(lambda a, b: a + 2 == b)",
         mutable_list_of(2, 2, 1, 5).filter_indexed(lambda a, b: a + 2 == b).var,
         [2, 5])
    test("MutableList.filter_indexed(lambda a, b: a != b)",
         array_of(1, 4, 2, 3).filter_indexed(lambda a, b: a != b).var,
         [1, 4])

    # filter_not_null
    #
    # filter_is_instance
    #
    # group_by
    #
    # group_by(key_selector, value_transform)
    #
    # fold
    #
    # reduce
    #
    # aggregate
    #
    # chunked and chunked(expression)
    #
    # slice()
    #
    # set_of()
    #
    # zip_with_next()
    #
    # windowed()

    section("partition()")

    test("list.partition(it().length() > 3)",
         list_of('one', 'two', 'three', 'four', 'five', 'six').partition(it().length() > 3),
         (('three', 'four', 'five'), ('one', 'two', 'six')))

    list_of("List", ".for_each(", "println(it())", ")").for_each(println(it()))
    test("List.for_each(println(it()))", True, True)
    array_of("Array", ".for_each(", "println(it())", ") passed").for_each(println(it()))
    test("Array.for_each(println(it()))", True, True)
    map_of(1, 'Map', 2, '.for_each(', 3, 'println(it())', 4, ') passed').for_each(println(it()))
    test("Map.for_each(println(it()))", True, True)

    test("MutableList.also(println(it()).add('five)",
         mutable_list_of("one", "two", "three", "four").also(println(it())).add("five").var,
         ['one', 'two', 'three', 'four', 'five'])
    test("Array.also(println(it()).to_mutable_list().add('five)",
         array_of("one", "two", "three", "four").also(println(it())).to_mutable_list(),
         ["one", "two", "three", "four"])
    test("Map.also(println(it()).to_list()",
         map_of(1, 'one', 2, 'two', 3, 'three', 4, 'four').also(println(it())).to_list(),
         ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')))

    section('Shared List/MutableList/Array Specific Methods')

    test("List.find(it().contains('t'))",
         list_of("won", "lost", "tied").find(it().contains('t')),
         'lost')

    test("List.find_last(it() >= 3)",
         list_of(1, 22, 7, 86, -100, 3).find_last(it() >= 3),
         3)

    test("List.with_index()",
         list_of(1, 3, 5, 7, 9).with_index().var,
         ((0, 1), (1, 3), (2, 5), (3, 7), (4, 9)))

    test("MutableList.group_by(it().first())",
         mutable_list_of("Hey", "Hi", "Hello", "Greetings", "Welcome").grouping_by(it().first()).var,
         {'H': ['Hey', 'Hi', 'Hello'], 'G': ['Greetings'], 'W': ['Welcome']})

    section("aggregate()")

    test("MutableList.group_by(it().first()).aggregate()",
         mutable_list_of("Hey", "Hi", "Hello", "Greetings", "Welcome").grouping_by(it().first()).aggregate().var,
         {'H': 'HeyHiHello', 'G': 'Greetings', 'W': 'Welcome'})

    test("Map<String, List<Int>>.aggregate()",
         map_of('H', (1, 2, 3), 'G', (2, 3, 4), 'W', (0, 0, 2, 0, 10, -10, 2)).aggregate().var,
         {'H': 6, 'G': 9, 'W': 4})

    test("MutableList.group_by(it().first()).aggregate()",
         mutable_list_of("Hey", "Hi", "Hello", "Greetings", "Welcome").grouping_by(it().first()).
         aggregate(lambda key, accumulator, element, first: StringBuilder().append(key).append(':').append(element)
                   if first else accumulator.append(element)).var,
         {'H': 'HeyHiHello', 'G': 'Greetings', 'W': 'Welcome'})

    test("Map.each_count()",
         map_of('H', ['Hey', 'Hi', 'Hello'], 'G', ['Greetings'], 'W', ['Welcome']).each_count().var,
         {'H': 3, 'G': 1, 'W': 1})

    x = map_of('H', ['Hey', 'Hi', 'Hello'], 'G', ['Greetings'], 'W', ['Welcome']).each_count().var
    test("Map.each_count_to(Map)",
         mutable_list_of("Hio", "Sup", "What's up").grouping_by(it().first()).each_count_to(x).var,
         {'H': 4, 'G': 1, 'W': 2, 'S': 1})

    test("List.size()",
         list_of(1, 2, 3).size(),
         3)
    test("MutableList.size()",
         mutable_list_of(1, 2, 3).size(),
         3)
    test("Array.size()",
         array_of(1, 2, 3).size(),
         3)

    test("empty List.min_or_null()",
         list_of().min_or_null().var,
         None)
    test("List.min_or_null()",
         list_of(2, 1, 0, 9).min_or_null().var,
         0)
    test("MutableList.min_or_null()",
         mutable_list_of(2, 1, 0, 9).min_or_null().var,
         0)
    test("Array.min_or_null()",
         array_of(2, 1, 0, 9).min_or_null().var,
         0)

    test("empty List.min_by_or_null()",
         list_of().min_by_or_null(it() < 3).var,
         None)
    test("List.min_by_or_null()",
         list_of(1, 0, 2, 9).min_by_or_null(it() < 3).var,
         0)
    test("MutableList.min_by_or_null()",
         mutable_list_of(2, 1, 0, 9).min_by_or_null(it() > 3).var,
         9)
    test("Array.min_by_or_null()",
         array_of('two', '1', 'zero', 'nine').min_by_or_null(it().length()).var,
         '1')

    test("empty List.max_or_null()",
         list_of().max_or_null().var,
         None)
    test("List.max_or_null()",
         list_of(2, 1, 0, 9).max_or_null().var,
         9)
    test("MutableList.max_or_null()",
         mutable_list_of(2, 1, 0, 9).max_or_null().var,
         9)
    test("Array.max_or_null()",
         array_of(2, 1, 0, 9).max_or_null().var,
         9)

    test("empty List.max_by_or_null()",
         list_of().max_by_or_null(it() < 3).var,
         None)
    test("List.max_by_or_null()",
         list_of(1, 0, 2, 9).max_by_or_null(it() < 3).var,
         2)
    test("MutableList.max_by_or_null()",
         mutable_list_of(2, 1, 0, 9).max_by_or_null(it() > 3).var,
         9)
    test("Array.max_by_or_null()",
         array_of('two', '1', 'zero', 'nine').max_by_or_null(it().length()).var,
         'nine')

    test("List.average()",
         list_of(2, 1, 0, 9).average().var,
         3)
    test("MutableList.average()",
         mutable_list_of(2, 1, 0, 9).average().var,
         3)
    test("Array.average()",
         array_of(2, 1, 0, 9).average().var,
         3)

    test("List.sum()",
         list_of(2, 1, 0, 9).sum().var,
         12)
    test("MutableList.sum()",
         mutable_list_of(2, 1, 0, 9).sum().var,
         12)
    test("Array.sum()",
         array_of(2, 1, 0, 9).sum().var,
         12)

    test("List.count()",
         list_of(2, 1, 0, 9).count().var,
         4)
    test("MutableList.count()",
         mutable_list_of(2, 1, 0, 9).count().var,
         4)
    test("Array.count()",
         array_of(2, 1, 0, 9).count().var,
         4)

    section('Assertion Methods')

    test("assert_equals()",
         PyKot(1).assert_equals(1),
         PyKot(1).assert_equals(1))

    test("assert_false()",
         PyKot([]).assert_false(),
         PyKot([]).assert_false())

    test("assert_true()",
         PyKot([1]).assert_true(),
         PyKot([1]).assert_true())

    test("assert_not_null()",
         PyKot(1).assert_not_null(),
         PyKot(1).assert_not_null())

    test("assert_null()",
         PyKot(None).assert_null(),
         PyKot(None).assert_null())

    test("assert_not_same()",
         PyKot(1).assert_not_same(PyKot(1)),
         PyKot(1).assert_not_same(PyKot(1)))

    x = PyKot(1)
    test("assert_same()",
         x.assert_same(x),
         x.assert_same(x))

    section('Map Method')

    test("Dict.entries().map(f'({it().key()}, {it().value()})')",
         PyKot({1: 'one', 2: 'two'}).entries().map(f"({it().key()}, {it().value()})").var,
         "((1, 'one'), (2, 'two'))")

    test("Dict.entries().entries().map(it().key(), it().value())",
         PyKot({1: 'one', 2: 'two'}).entries().map((it().key(), it().value())).var,
         ((1, 'one'), (2, 'two')))

    test("List.map((it() ** 2))",
         list_of(1, 2, 3).map((it() ** 2)).var,
         (1, 4, 9))

    test("List.map((it() > it().to_string().code()))",
         list_of(1, 2, 3).map((it() > it().to_string().code())).var,
         (False, False, False))

    test("List.map((it().length()))",
         list_of('one', 'two', 'three').map((it().length())).var,
         (3, 3, 5))

    test("List(list, list).map((it().sum()))",
         list_of((1, 2, 3), (4, 5, 0)).map((it().sum())).var,
         (6, 9))

    section('Elvis Operator Method')

    test("elvis with None",
         elvis_operator(None, "was None"),
         "was None")

    test("elvis operator",
         elvis_operator("return if not None", "alternative return"),
         "return if not None")

    var = 1
    test("elvis with var",
         elvis_operator(var, "was None"),
         1)

    section('*** Class Methods ***')

    section('Apply Method')

    test("Object.apply(assignment1, assignment2)",
         PyKot(it()).apply(('age', 30)).var.age,
         30)


run_tests()
report_card()
