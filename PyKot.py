"""
Copyright (c) 2021, Russell Wallace Butler
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

import traceback as tb
from dataclasses import dataclass
import re as re
import numpy as np


class PyKot:

    def __init__(self, variable, recall=False):
        self.variable = variable
        self.recall = recall

    def __repr__(self):
        return str(self.variable)

    def status(self):
        return f"self.variable = {self.variable}\n" \
               f"self.recall = {self.recall}"

    # str methods
    def last_index(self):  # lastIndex()
        raise_type_error_if_merited("last_index()", self.variable, str)
        return len(self.variable) - 1

    def drop(self, drop_from_front: int):  # drop(n)
        raise_type_error_if_merited("drop(Int)", self.variable, str)
        return PyKot(self.variable[drop_from_front:], True)

    def drop_last(self, drop_from_back: int):  # dropLast(n)
        raise_type_error_if_merited("drop_last(Int)", self.variable, str)
        return PyKot(self.variable[: (len(self.variable) - drop_from_back)], True)

    def drop_while(self, it_expression):  # dropWhile(it expression)
        raise_type_error_if_merited("drop_while(it expression)", self.variable, str)
        while it_expression.in_line_function(self.variable[0]):
            self.variable = self.variable[1:]
        return PyKot(self.variable, True)

    def drop_last_while(self, it_expression):  # dropLastWhile(it expression)
        raise_type_error_if_merited("drop_last_while(it expression)", self.variable, str)
        while it_expression.in_line_function(self.variable[-1]):
            self.variable = self.variable[:-1]
        return PyKot(self.variable, True)

    def length(self):  # length()
        raise_type_error_if_merited("length()", self.variable, str)
        return len(self.variable)

    def first(self):  # first()
        raise_type_error_if_merited("first()", self.variable, str)
        return PyKot(self.variable[0], True)

    def last(self):  # last()
        raise_type_error_if_merited("last()", self.variable, str)
        return PyKot(self.variable[-1], True)

    def trim_margin(self, margin="|"):  # trimMargin(margin)
        raise_type_error_if_merited("trim_margin(margin='|')", self.variable, str)
        return PyKot(self.variable[(self.variable.find(margin) + len(margin)):], True)

    def compare_to(self, comparison: str, ignorecase=False):  # compareTo(String, ignorecase=False)
        raise_type_error_if_merited("compare_to(String, ignorecase=False)", self.variable, str)
        if ignorecase:
            self.variable = self.variable.lower()
            comparison = comparison.lower()
        original = [self.variable, comparison]
        sort_compare = [self.variable, comparison]
        sort_compare.sort()
        sort_compare = 1 if sort_compare == original else -1
        return 0 if self.variable == comparison else sort_compare

    def sub_string(self, first_index, second_index):  # subString(i, j)
        raise_type_error_if_merited("sub_string(Int, Int)", self.variable, str)
        return PyKot(self.variable[first_index: second_index], True)

    def split(self, delimiter=' ', ignorecase=False):  # split(delimiter) or
        # split(delimiter, ignorecase=True) or split(delimiter.toRegex()) or split(regex(delimiter))
        raise_type_error_if_merited("split(delimiter=' ', ignorecase=False)", self.variable, str)
        if type_compliance(delimiter, type(re.compile(''))):
            return re.split(delimiter, self.variable)
        if ignorecase:
            delimiter_indexes = [0]
            find, first_index = 0, 0
            while find != -1 and (len(self.variable) - find) >= len(delimiter):
                find = self.variable.lower().find(delimiter.lower(), find, (len(self.variable) - 1))
                if find == -1:
                    continue
                delimiter_indexes.append(find)
                find += len(delimiter)
                delimiter_indexes.append(find)
            split_list = []
            first = True
            first_index = 0
            for index in delimiter_indexes:
                if first:
                    first_index = index
                    first = False
                    continue
                elif not first:
                    split_list.append(self.variable[first_index:index])
                    first = True
            if not first:
                split_list.append(self.variable[first_index:])
                return split_list
            return split_list
        return self.variable.split(delimiter)

    def sub_sequence(self, first_index: int, second_index: int):  # subSequence(i, j)
        raise_type_error_if_merited("sub_sequence(Int, Int)", self.variable, str)
        return PyKot(self.variable[first_index:second_index], True)

    def lines(self):  # lines()
        raise_type_error_if_merited("lines()", self.variable, str)
        return self.variable.splitlines()

    def capitalize(self):  # capitalize()
        raise_type_error_if_merited("capitalize()", self.variable, str)
        return PyKot(self.variable.capitalize(), True)

    def to_regex(self):  # toRegex()
        raise_type_error_if_merited("to_regex()", self.variable, str)
        return re.compile(self.variable)

    def replace(self, old_value: str, new_value: str, ignorecase=False):  # replace(old, new, ignorecase=False)
        raise_type_error_if_merited("replace(String, String, ignorecase=False)", self.variable, str)
        if ignorecase:
            find_index = self.variable.lower().find(old_value.lower())
            if find_index == -1:
                return PyKot(self.variable, True)
            return PyKot(self.variable[:find_index] + new_value + self.variable[(find_index + len(old_value)):], True)
        return PyKot(self.variable.replace(old_value, new_value), True)

    def ends_with(self, substring):  # endsWith(substring)
        raise_type_error_if_merited("ends_with(String)", self.variable, str)
        return True if self.variable[-len(substring):] == substring else False

    # str/int methods
    def plus(self, string_or_int):  # plus(String) or plus(Int)
        raise_type_error_if_merited("plus(String) or plus(Int)", self.variable, str, int)
        if type_compliance(self.variable, str) and type_compliance(string_or_int, int):
            string_or_int = str(string_or_int)
        elif type_compliance(self.variable, int) and type_compliance(string_or_int, str):
            string_or_int = int(string_or_int)
        return PyKot(self.variable + string_or_int, True)

    # str/list/mutable_list methods
    def get(self, index):
        raise_type_error_if_merited("get(Int)", self.variable, str, list, tuple, type(np.array([])))
        if not type_compliance(self.variable[index], str, int, list, tuple):
            if isinstance(self.variable[index], type(np.array([1])[0])):
                return PyKot(int(self.variable[index]), True)
            elif isinstance(self.variable[index], type(np.array([1.0])[0])):
                return PyKot(float(self.variable[index]), True)
        return PyKot(self.variable[index], True)

    # all data type methods
    def to_string(self):  # toString()
        raise_type_error_if_merited("to_string()", self.variable, str, int, list, tuple, range, dict)
        if isinstance(self.variable, str):
            return self.variable
        return str(self.variable)

    def content_to_string(self):
        raise_type_error_if_merited("content_to_string()", self.variable, type(np.array([])))
        return str([x for x in self.variable])

    # list/mutable_list/Map/Array methods
    def any(self, predicate=None):  # any(predicate)
        raise_type_error_if_merited("any(), any(value), or any(predicate)",
                                    self.variable, list, tuple, dict, type(np.array([])))
        if type_compliance(predicate, str, int):
            if type_compliance(self.variable, dict):
                return True if predicate in self.variable.keys() else False
            return True if predicate in self.variable else False
        if predicate is None:
            if self.variable:
                return True
            return False
        predicate = predicate.in_line_function
        if type_compliance(self.variable, dict):
            return True if len(list(filter(predicate, self.variable.keys()))) > 0 else False
        return True if len(list(filter(predicate, self.variable))) > 0 else False

    def to_list(self):  # toList()
        raise_type_error_if_merited("to_list()", self.variable, list, tuple, dict, type(np.array([])))
        if type_compliance(self.variable, tuple):
            return self.variable
        elif type_compliance(self.variable, dict):
            return tuple([(key, self.variable[key]) for key in self.variable.keys()])
        return tuple(self.variable)

    def to_mutable_list(self):  # toMutableList()
        raise_type_error_if_merited("to_mutable_list()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, tuple):
            return list(self.variable)
        elif type_compliance(self.variable, dict):
            return [(key, self.variable[key]) for key in self.variable.keys()]
        elif type_compliance(self.variable, type(np.array([]))):
            return [x for x in self.variable]
        return self.variable

    def contains(self, element):  # contains(element)
        raise_type_error_if_merited("contains()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, dict):
            return element in self.variable.keys()
        return element in self.variable

    def filter(self, predicate):  # filter(predicate)
        raise_type_error_if_merited("filter(function)", self.variable, list, tuple, dict, type(np.array([])))
        predicate = predicate.in_line_function
        if type_compliance(self.variable, dict):
            new_map = {}
            for key in list(filter(predicate, self.variable.keys())):
                new_map[key] = self.variable[key]
            return PyKot(new_map, True)
        return PyKot(list(filter(predicate, self.variable)), True)

    def for_each(self, *statements):
        raise_type_error_if_merited("for_each(*statements)", self.variable, list, tuple, type(np.array([])), dict)
        if type_compliance(self.variable, dict):
            useful_list = [PyKot(self.variable[x]) for x in self.variable.keys()]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        else:
            useful_list = [PyKot(unpack_array(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        return PyKot(self.variable, True)

    def also(self, *statements):
        raise_type_error_if_merited("also(*statements)", self.variable,
                                    str, int, range, list, tuple, type(np.array([])), dict)
        if type_compliance(self.variable, dict):
            useful_list = [PyKot(self.variable[x]) for x in self.variable.keys()]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, range, list, tuple, type(np.array([]))):
            useful_list = [PyKot(unpack_array(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, str, int):
            for statement in statements:
                statement(self.variable)
        return PyKot(self.variable, True)

    def let(self, *statements):
        raise_type_error_if_merited("let(*statements)", self.variable,
                                    str, int, range, list, tuple, type(np.array([])), dict, type(None))
        if self.variable is None:
            return PyKot(self.variable, True)
        if type_compliance(self.variable, dict):
            useful_list = [PyKot(self.variable[x]) for x in self.variable.keys()]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, range, list, tuple, type(np.array([]))):
            useful_list = [PyKot(unpack_array(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, str, int):
            for statement in statements:
                statement(self.variable)
        return PyKot(self.variable, True)

    # list/mutable_list/array methods

    def find(self, predicate):  # find(predicate)
        raise_type_error_if_merited("find(predicate)", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        found = list(filter(predicate, self.variable))
        if len(found) == 0:
            return None
        return found[0]

    def find_last(self, predicate):  # findLast(predicate)
        raise_type_error_if_merited("find_last(predicate)", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        found = list(filter(predicate, self.variable))
        if len(found) == 0:
            return None
        return found[-1]

    def with_index(self):  # withIndex()
        raise_type_error_if_merited("with_index()", self.variable, list, tuple, type(np.array([])))
        new_variable = [(i, e) for i, e in enumerate(self.variable)]
        if type_compliance(self.variable, list):
            return PyKot(new_variable, True)
        return PyKot(tuple(new_variable), True)

    def grouping_by(self, predicate):  # groupingBy(it expression)
        raise_type_error_if_merited("grouping_by(predicate)", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        output_map = {}
        for element in self.variable:
            if predicate(element) in output_map:
                output_map[predicate(element)] = output_map[predicate(element)] + [element]
                continue
            output_map[predicate(element)] = [element]
        return PyKot(output_map, True)

    def size(self):  # .size
        raise_type_error_if_merited("size()", self.variable, list, tuple, type(np.array([])))
        return len(self.variable)

    def min_or_null(self):  # minOrNull()
        raise_type_error_if_merited("min_or_null()", self.variable, list, tuple, type(np.array([])))
        if len(self.variable) == 0:
            return PyKot(None, True)
        useful_list = [unpack_array(x) for x in self.variable]
        useful_list.sort()
        return PyKot(useful_list[0], True)

    def min_by_or_null(self, predicate):
        raise_type_error_if_merited("min_by_or_null()", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        useful_list = list(filter(predicate, [unpack_array(x) for x in self.variable]))
        if len(useful_list) == 0:
            return PyKot(None, True)
        if len(useful_list) == len(self.variable):
            useful_list.sort(key=predicate)
        else:
            useful_list.sort()
        return PyKot(useful_list[0], True)

    def max_or_null(self):  # maxOrNull()
        raise_type_error_if_merited("max_or_null()", self.variable, list, tuple, type(np.array([])))
        if len(self.variable) == 0:
            return PyKot(None, True)
        useful_list = [unpack_array(x) for x in self.variable]
        useful_list.sort()
        return PyKot(useful_list[-1], True)

    def max_by_or_null(self, predicate):
        raise_type_error_if_merited("max_by_or_null()", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        useful_list = list(filter(predicate, [unpack_array(x) for x in self.variable]))
        if len(useful_list) == 0:
            return PyKot(None, True)
        if len(useful_list) == len(self.variable):
            useful_list.sort(key=predicate)
        else:
            useful_list.sort()
        return PyKot(useful_list[-1], True)

    def average(self):  # average()
        raise_type_error_if_merited("max_or_null()", self.variable, list, tuple, type(np.array([])))
        useful_list = [x for x in self.variable]
        return PyKot(int(sum(useful_list) / len(useful_list)), True)

    def sum(self):  # sum()
        raise_type_error_if_merited("max_or_null()", self.variable, list, tuple, type(np.array([])))
        return PyKot(int(sum([x for x in self.variable])), True)

    def count(self):  # count()
        raise_type_error_if_merited("max_or_null()", self.variable, list, tuple, type(np.array([])))
        return PyKot(len([x for x in self.variable]), True)

    # mutable_list methods
    def add(self, element):
        if not type_compliance(self.variable, list):
            raise TypeError("Can only use add() on PyKot(MutableList)")
        self.variable.append(element)
        return PyKot(self.variable, True)

    def add_all(self, *args):
        raise_type_error_if_merited("add_all(element) or add_all(element, ..., element)", self.variable, list)
        self.variable += [arg for arg in args]
        return PyKot(self.variable, True)

    # int methods

    # map methods
    def keys(self):  # keys()
        if not type_compliance(self.variable, dict):
            raise TypeError("Can only use keys() on PyKot(dict)")
        return self.variable.keys()

    def values(self):  # values()
        if not type_compliance(self.variable, dict):
            raise TypeError("Can only use values() on PyKot(dict)")
        return self.variable.values()

    def each_count(self):  # eachCount()
        raise_type_error_if_merited("each_count()", self.variable, dict)
        output_map = dict([(key, len(self.variable[key]))
                           if type_compliance(self.variable[key], list, tuple, type(np.array([])))
                           else (key, 1) for key in self.variable.keys()])
        return PyKot(output_map, True)

    def each_count_to(self, count_map):  # eachCountTo(Map)
        raise_type_error_if_merited("each_count_to(Map)", self.variable, dict)
        new_count_map = dict([(key, len(self.variable[key]))
                              if type_compliance(self.variable[key], list, tuple, type(np.array([])))
                              else (key, 1) for key in self.variable.keys()])
        for key in count_map.keys():
            if key in new_count_map:
                new_count_map[key] = count_map[key] + new_count_map[key]
            else:
                new_count_map[key] = count_map[key]
        return PyKot(new_count_map, True)

    def aggregate(self):
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def set(self, index, value):  # .set(index, value)
        raise_type_error_if_merited("set(index, value)", self.variable, list, type(np.array([])))
        if isinstance(self.variable, type(np.array([]))):
            list_array = [x for x in self.variable]
            list_array[index] = value
            self.variable = np.array(list_array)
        else:
            self.variable[index] = value
        return PyKot(self.variable, True)

    def indices(self):  # .indices
        raise_type_error_if_merited("indices()", self.variable, list, tuple, type(np.array([])))
        return PyKot(range(len(self.variable)), True)

    def is_empty(self):  # .isEmpty()
        raise_type_error_if_merited("is_empty()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, range):
            return True if self.variable == range(0) else False
        return True if self.variable.indices() == range(0) else False

    def all(self, predicate=''):  # .all()
        raise_type_error_if_merited("all() or all(predicate)", self.variable, str, list, tuple, type(np.array([])))
        if isinstance(self.variable, str):
            return True if predicate == self.variable else False
        if isinstance(self.variable, list) or isinstance(self.variable, tuple):
            for x in self.variable:
                if predicate != x:
                    return False
            return True
        predicate = predicate.in_line_function
        if type_compliance(predicate, type(lambda y: y)):
            return True if len(list(filter(predicate, self.variable))) == len(self.variable) else False
        return False

    def as_sequence(self):  # .asSequence()
        return PyKot(tuple(self.variable), True)

    def as_iterable(self):  # .asIterable()
        return PyKot(tuple(self.variable), True)

    def iterator(self):  # .iterator()
        return PyKot(tuple(self.variable), True)

    def sequence(self):  # .sequence()
        return PyKot(tuple(self.variable), True)

    def uppercase_char(self):  # .uppercaseChar()
        if not isinstance(self.variable, str) or not len(self.variable) == 1:
            raise TypeError("Can only use uppercase_char() on len(PyKot(String)) == 1")
        return PyKot(self.variable.upper(), True)

    def uppercase(self):  # .uppercase()
        if not isinstance(self.variable, str):
            raise TypeError("Can only use uppercase() on PyKot(String)")
        return PyKot(self.variable.upper(), True)

    def copy_of(self):  # .copyOf()
        raise_type_error_if_merited("copy_of()", self.variable, list, map, tuple, type(np.array([])))
        return PyKot(self.variable.copy(), True)

    def equals(self, other):  # .equals(other)
        return self.variable == other

    def put(self, key, value):  # .put(key, value)
        raise_type_error_if_merited("put(key, value)", self.variable, map)
        self.variable[key] = value
        return PyKot(self.variable, True)

    def get_or_put(self, key, value):  # .getOrPut(key) {value}
        raise_type_error_if_merited("get_or_put(key, value)", self.variable, map)
        if key not in self.variable.keys():
            self.variable[key] = value
            return PyKot(self.variable, True)
        return self.variable[key]

    def sub_list(self, from_index: int, to_index: int):  # subList(fromIndex, toIndex)
        raise_type_error_if_merited("sub_list(index, index)", self.variable, list, tuple)
        return PyKot(self.variable[from_index:to_index], True)

    def map(self, lambda_function):
        lambda_function = lambda_function.in_line_function
        return PyKot([lambda_function(x) for x in self.variable], True)

    def assert_equals(self, other):
        if type_compliance(self, type(other)):
            if self != other:
                raise AssertionFailedError("Equals assertion failed.")
        if self.variable != other:
            raise AssertionFailedError("Equals assertion failed.")

    def assert_false(self):
        if self.variable:
            raise AssertionFailedError("False assertion failed.")

    def assert_true(self):
        if not self.variable:
            raise AssertionFailedError("True assertion failed.")

    def assert_not_null(self):
        if self.variable is None:
            raise AssertionFailedError("Not Null assertion failed.")

    def assert_null(self):
        if self.variable is not None:
            raise AssertionFailedError("Null assertion failed.")

    def assert_not_same(self, other):
        if self == other:
            raise AssertionFailedError("Not Same assertion failed.")

    def assert_same(self, other):
        if self != other:
            raise AssertionFailedError("Same assertion failed.")

    def take_if(self, lambda_function):
        if lambda_function.in_line_function(self.variable):
            return PyKot(self.variable, True)
        return PyKot(None, True)

    def take_unless(self, lambda_function):
        if lambda_function.in_line_function(self.variable):
            return PyKot(None, True)
        return PyKot(self.variable, True)

    def index_of(self, target):
        type_compliance(self.variable, str, list, tuple, type(np.array([])))
        if isinstance(self.variable, str):
            return self.variable.find(target)
        if target in self.variable:
            return [unpack_array(x) for x in self.variable].index(target)
        return -1

    # class methods
    def apply(self, *assignments):
        for assignment in assignments:
            setattr(self, assignment[0], assignment[1])
        return self


def println(string):
    if type_compliance(string, type(it())):
        string = string.in_line_function
        return lambda x: print(string(x))
    print(string)


def regex(regex_expression):
    return re.compile(regex_expression)


def list_of(*args):
    if isinstance(args, int) or isinstance(args, str):
        return PyKot(args, False)
    return PyKot(tuple([element for element in args]), False)


def empty_list():  # emptyList<Any>()
    return PyKot(tuple(), False)


def mutable_list_of(*args):  # mutableListOf(element, ..., element)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot([args], False)
    return PyKot([element for element in args], False)


def array_of(*args):  # arrayOf(element, ..., element)
    if len(args) == 0:
        return PyKot(np.array([]), False)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot(np.array([args]), False)
    return PyKot(np.array([element for element in args]), False)


def empty_array():  # emptyArray()
    return PyKot(np.array([])), False


def int_array_of(*args):  # intArrayOf(int,..., int)
    int_array = []
    for arg in args:
        raise_type_error_if_merited("int_array_of(Int)", self.variable, int)
        int_array.append(arg)
    return PyKot(np.array(int_array)), False


def array_of_nulls(size=0):  # arrayOfNulls(int)
    null_array = []
    for i in range(size):
        null_array.append(None)
    return PyKot(np.array(null_array)), False


def map_of(*args):
    list_of_keys_and_values = list(args)
    if isinstance(args[0], tuple):
        return PyKot(dict(args), False)
    result_dict = {}
    if len(list_of_keys_and_values) % 2 == 1:
        result_dict[list_of_keys_and_values[-1]] = None
        list_of_keys_and_values = list_of_keys_and_values[:-1]
    index_lead = 0
    for i in range((len(list_of_keys_and_values) // 2)):
        dict_key = list_of_keys_and_values[index_lead]
        dict_value = list_of_keys_and_values[index_lead + 1]
        if dict_key in result_dict.keys():
            if not isinstance(result_dict[dict_key], list):
                result_dict[dict_key] = [result_dict[dict_key]]
            result_dict[dict_key].append(dict_value)
        else:
            result_dict[dict_key] = dict_value
        index_lead += 2
    return PyKot(result_dict, False)


def mutable_map_of(*args):
    list_of_keys_and_values = list(args)
    if isinstance(args[0], tuple):
        return PyKot(dict(args), False)
    result_dict = {}
    if len(list_of_keys_and_values) % 2 == 1:
        result_dict[list_of_keys_and_values[-1]] = None
        list_of_keys_and_values = list_of_keys_and_values[:-1]
    index_lead = 0
    for i in range((len(list_of_keys_and_values) // 2)):
        dict_key = list_of_keys_and_values[index_lead]
        dict_value = list_of_keys_and_values[index_lead + 1]
        if dict_key in result_dict.keys():
            if not isinstance(result_dict[dict_key], list):
                result_dict[dict_key] = [result_dict[dict_key]]
            result_dict[dict_key].append(dict_value)
        else:
            result_dict[dict_key] = dict_value
        index_lead += 2
    return PyKot(result_dict, False)


def elvis_operator(not_null_return, alternative_return):
    if not_null_return:
        return_value = not_null_return
    else:
        return_value = alternative_return
    return return_value


def it():
    return It(lambda x: x)


class It:

    def __init__(self, in_line_function):
        self.in_line_function = in_line_function

    def __add__(self, other):
        return It(lambda x: self.in_line_function(x) + other)

    def __sub__(self, other):
        return It(lambda x: self.in_line_function(x) - other)

    def __mul__(self, other):
        return It(lambda x: self.in_line_function(x) * other)

    def __truediv__(self, other):
        return It(lambda x: self.in_line_function(x) / other)

    def __lt__(self, comparison):
        return It(lambda x: self.in_line_function(x) < comparison)

    def __le__(self, comparison):
        return It(lambda x: self.in_line_function(x) <= comparison)

    def __eq__(self, comparison):
        return It(lambda x: self.in_line_function(x) == comparison)

    def __ne__(self, comparison):
        return It(lambda x: self.in_line_function(x) != comparison)

    def __gt__(self, comparison):
        return It(lambda x: self.in_line_function(x) > comparison)

    def __ge__(self, comparison):
        return It(lambda x: self.in_line_function(x) >= comparison)

    def __mod__(self, modulo):
        return It(lambda x: self.in_line_function(x) % modulo)

    def contains(self, string):
        return It(lambda x:
                  string in self.in_line_function(x.keys()) if isinstance(x, dict)
                  else string in self.in_line_function(x))

    def starts_with(self, string, start_index=0, ignorecase=False):
        if ignorecase:
            return It(lambda x:
                      True if string.lower() == self.in_line_function(x)[start_index:len(string)].lower()
                      else False)
        return It(lambda x:
                  True if string == self.in_line_function(x)[start_index:len(string)]
                  else False)

    def length(self):
        return It(lambda x:
                  len(self.in_line_function(x)))

    def uppercase_char(self):
        return It(lambda x:
                  self.in_line_function(x).upper())

    def uppercase(self):
        return It(lambda x:
                  self.in_line_function(x).upper())

    def first(self):
        return It(lambda x:
                  self.in_line_function(x)[0])

    def code(self):
        return It(lambda x:
                  ord(self.in_line_function(x)))

    def is_not_empty(self):
        return It(lambda x:
                  True if not self.in_line_function(x) else False)


def type_compliance(variable, *args):
    """
    Validates a variable's data type as acceptable or not returning True or False respectively.
    :param variable: target of data type validation
    :param args: collection of acceptable data types
    :return: True or False
    """
    return_list = []
    for arg in args:
        if isinstance(variable, arg):
            return_list.append(True)
        else:
            return_list.append(False)
    return True if True in return_list else False


def raise_type_error_if_merited(method: str, variable, *args, type_error_message=''):
    pykot_exchange = {
        str: "PyKot(String)",
        int: "PyKot(Int)",
        list: "PyKot(MutableList)",
        tuple: "PyKot(List)",
        dict: "PyKot(Map)",
        range: "PyKot(Range)",
        type(np.array([])): "PyKot(Array)",
        type(None): "PyKot(None)"
    }

    if not type_compliance(variable, args):

        if type_error_message != '':
            raise TypeError(type_error_message)

        pykot_types = []
        for i in range(len(args)):
            pykot_types.append(pykot_exchange[args[i]])

        type_error_message = f"Can only use {method} with "
        if len(pykot_types) == 1:
            type_error_message += f"{pykot_exchange[args[0]]}."
        elif len(pykot_types) == 2:
            type_error_message += f"{pykot_exchange[args[0]]} or {pykot_exchange[args[1]]}."
        else:
            for arg in args[:-2]:
                type_error_message += f"{pykot_exchange[arg]}, "
            type_error_message += f"{pykot_exchange[args[-2]]} or {pykot_exchange[args[-1]]}."

        raise TypeError(type_error_message)


def unpack_array(element):
    if type_compliance(element, type([x for x in np.array([1])][0])):
        return int(element)
    elif type_compliance(element, type([x for x in np.array([1.0])][0])):
        return float(element)
    return element


class Error(Exception):
    pass


class AssertionFailedError(Error):

    def __init__(self, message):
        self.message = message
