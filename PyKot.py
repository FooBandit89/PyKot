"""
Copyright (c) 2021, Russell Wallace Butler
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

import traceback as tb
from dataclasses import dataclass
import re as re


class PyKot:

    def __init__(self, variable, recall=False):
        self.variable = variable
        self.recall = recall

    def __repr__(self):
        return str(self.variable)

    def status(self):
        return f"self.variable = {self.variable}\n" \
               f"self.variable_type = {self.variable_type}\n" \
               f"self.output_type = {self.output_type}\n" \
               f"self.identity = {self.identity}\n" \
               f"self.recall = {self.recall}"

    # str methods
    def last_index(self):  # lastIndex()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use last_index() on PyKot(string)")
        return len(self.variable) - 1

    def drop(self, drop_from_front: int):  # drop(n)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use drop(int) on PyKot(string)")
        return PyKot(self.variable[drop_from_front:], True)

    def drop_last(self, drop_from_back: int):  # dropLast(n)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use drop_last(it conditional) on PyKot(string)")
        return PyKot(self.variable[: (len(self.variable) - drop_from_back)], True)

    def drop_while(self, condition_lambda):  # dropWhile( it expression )
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use drop_last_while(it conditional) on PyKot(string)")
        while condition_lambda(self.variable[0]):
            self.variable = self.variable[1:]
        return PyKot(self.variable, True)

    def drop_last_while(self, condition_lambda):  # dropLastWhile( it expression )
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use drop_last_while(it expression) on PyKot(string)")
        while condition_lambda(self.variable[-1]):
            self.variable = self.variable[:-1]
        return PyKot(self.variable, True)

    def length(self):  # length()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use length() on PyKot(string)")
        return len(self.variable)

    def first(self):  # first()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use first() on PyKot(string)")
        return PyKot(self.variable[0], True)

    def last(self):  # last()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use last() on PyKot(string)")
        return PyKot(self.variable[-1], True)

    def trim_margin(self, margin="|"):  # trimMargin(margin)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use trim_margin(str) on PyKot(string)")
        return PyKot(self.variable[(self.variable.find(margin) + len(margin)):], True)

    def compare_to(self, comparison: str, ignorecase=False):  # compareTo(String, ignorecase=False)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use compare_to(str) on PyKot(string)")
        if ignorecase:
            self.variable = self.variable.lower()
            comparison = comparison.lower()
        original = [self.variable, comparison]
        sort_compare = [self.variable, comparison]
        sort_compare.sort()
        sort_compare = 1 if sort_compare == original else -1
        return 0 if self.variable == comparison else sort_compare

    def sub_string(self, first_index, second_index):  # subString(i, j)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use substring(int, int) on PyKot(string)")
        return PyKot(self.variable[first_index: second_index], True)

    def split(self, delimiter=' ', ignorecase=False, regex_split=False):  # split(delimiter) or
        # split(delimiter, ignorecase=True) or split(delimiter.toRegex()) or split(regex(delimiter))
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use split(str) on PyKot(string)")
        if type_compliance(delimiter, tuple):
            delimiter, ignorecase, regex_split = delimiter[0], delimiter[1], delimiter[2]
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
        if regex_split:
            return re.split(delimiter, self.variable)
        return self.variable.split(delimiter)

    def sub_sequence(self, first_index, second_index):  # subSequence(i, j)
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use sub_sequence(int, int) on PyKot(string)")
        return PyKot(self.variable[first_index:second_index], True)

    def lines(self):  # lines()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use lines() on PyKot(string)")
        return self.variable.splitlines()

    def capitalize(self):  # capitalize()
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use capitalize() on PyKot(string)")
        return PyKot(self.variable.capitalize(), True)

    def to_regex(self):
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use to_regex(str) on PyKot(string)")
        return self.variable, False, True

    def replace(self, old_value: str, new_value: str, ignorecase=False):
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use replace(str, str, ignorecase=False) on PyKot(string)")
        if ignorecase:
            find_index = self.variable.lower().find(oldvalue.lower())
            if find_index == -1:
                return PyKot(self.variable, True)
            return PyKot(self.variable[:find_index] + new_value + self.variable[(find_index + len(old_value)):], True)
        return PyKot(self.variable.replace(old_value, new_value), True)

    def ends_with(self, substring):
        if not type_compliance(self.variable, str):
            raise TypeError("Can only use ends_with(substring) on Pykot(string)")
        return True if self.variable[-len(substring)] == substring else False

    # str/int methods
    def plus(self, string_or_int):  # plus(String) or plus(Int)
        if not type_compliance(self.variable, str, int):
            raise TypeError("Can only use plus(string_or_int) on PyKot(string) or PyKot(int)")
        return PyKot(self.variable + string_or_int, True)

    # str/list/mutable_list methods
    def get(self, index):
        if not type_compliance(self.variable, str, list, tuple):
            raise TypeError("Can only use get(int) on PyKot(string), PyKot(list), or PyKot(mutable_list)")
        return PyKot(self.variable[index], True)

    def any(self, predicate=''):
        if not type_compliance(self.variable, str, list, tuple):
            raise TypeError("Can only use any() on PyKot(string), PyKot(list), or PyKot(mutable_list)")
        if type_compliance(self.variable, str) and predicate == '':
            return len(self.variable) > 0
        return True if predicate in self.variable else False

    # str/int/list/mutable_list methods
    def to_string(self):
        if not type_compliance(self.variable, str, int, list, tuple, range):
            raise TypeError("Can only use to_string() on PyKot(string), PyKot(int), "
                            "PyKot(list), PyKot(mutable_list), or PyKot(range)")
        if isinstance(self.variable, str):
            return self.variable
        return str(self.variable)

    # list/mutable_list methods
    def to_list(self):
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use to_list() on PyKot(list) or PyKot(mutable_list)")
        if type_compliance(self.variable, tuple):
            return self.variable
        return tuple(self.variable)

    def to_mutable_list(self):
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use to_mutable_list() on PyKot(list) or PyKot(mutable_list)")
        if isinstance(self.variable_type, tuple):
            return list(self.variable)
        return self.variable

    def contains(self, element):
        if not type_compliance(self.variable, list, tuple, dict):
            raise TypeError("Can only use contains() on PyKot(Int), PyKot(list), PyKot(mutable_list), or PyKot(map)")
        if isinstance(self.variable, dict):
            return element in self.variable.keys()
        return element in self.variable

    def find(self, predicate, subcall=""):
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use find() on PyKot(list) or PyKot(mutable_list)")
        if isinstance(predicate, tuple):
            predicate, subcall = predicate[0], predicate[1]
        for element in self.variable:
            if isinstance(element, str):
                if element.find(predicate) != -1:
                    if subcall.startswith("startsWith"):
                        if element.startswith(predicate):
                            return element
                        else:
                            continue
                    return element
            elif predicate == element:
                return element
        return None

    def find_last(self, predicate, subcall=""):
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use find_last() on PyKot(list) or PyKot(mutable_list)")
        if isinstance(predicate, tuple):
            predicate, subcall = predicate[0], predicate[1]
        found_last = ""
        for element in self.variable:
            if isinstance(element, str):
                if element.find(predicate) != -1:
                    if subcall.startswith("startsWith"):
                        if element.startswith(predicate):
                            found_last = element
                            continue
                        continue
                    found_last = element
            elif predicate == element:
                found_last = element
        if found_last != "":
            return found_last
        return None

    def with_index(self):  # withIndex()
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use with_index() on PyKot(list) or PyKot(tuple)")
        new_variable = [(i, e) for i, e in enumerate(self.variable)]
        if type_compliance(self.variable, list):
            return PyKot(new_variable, True)
        return PyKot(tuple(new_variable), True)

    # mutable_list methods
    def add(self, element):
        if not type_compliance(self.variable, list):
            raise TypeError("Can only use add() on PyKot(MutableList)")
        return PyKot(self.variable.append(element), True)

    def add_all(self, *args):
        if not type_compliance(self.variable, list):
            raise TypeError("Can only use add_all() on PyKot(MutableList)")
        for arg in args:
            if type_compliance(arg, tuple, list):
                self.variable += [x for x in arg]
            else:
                self.variable.append(arg)
        return PyKot(self.variable, True)

    # int methods

    # map methods
    def keys(self):
        if not type_compliance(self.variable, dict):
            raise TypeError("Can only use keys() on PyKot(dict)")
        return self.variable.keys()

    def values(self):
        if not type_compliance(self.variable, dict):
            raise TypeError("Can only use values() on PyKot(dict)")
        return self.variable.values()

    # ------------------------------------------------------------------------------------------------------------------

    def filter(self, contains):
        if not type_compliance(self.variable, list, tuple, dict):
            pass
        if isinstance(contains, type(lambda: 0)):
            return PyKot(list(filter(contains, self.variable)), True)
        if type_compliance(self.variable, dict):
            pass
        return PyKot(filter(contains, self.variable), True)

    def for_each(self):
        pass

    def size(self):  # .size
        if not isinstance(self.variable, list) and not isinstance(self.variable, tuple):
            raise TypeError("Can only use size() on PyKot(list), or PyKot(MutableList)")
        return len(self.variable)

    def set(self, index, value):  # .set(index, value)
        if not isinstance(self.variable, list):
            raise TypeError("Can only use set() on mutable collections")
        self.variable[index] = value
        return PyKot(self.variable, True)

    def indices(self):  # .indices
        if not isinstance(self.variable, list) and not isinstance(self.variable, tuple):
            raise TypeError("Can only use indices() on collections")
        return PyKot(range(len(self.variable)), True)

    def is_empty(self):  # .isEmpty()
        if isinstance(self.variable, range):
            return True if self.variable == range(0) else False
        return True if self.variable.indices() == range(0) else False

    def all(self, predicate=''):  # .all()
        if not isinstance(self.variable_type, str) \
                and not isinstance(self.variable_type, list) \
                and not isinstance(self.variable_type, tuple):
            raise TypeError("Can only use all() on PyKot(string), PyKot(list), or PyKot(mutable_list)")
        if isinstance(self.variable_type, str):
            return True if predicate == self.variable else False
        if isinstance(self.variable_type, list) or isinstance(self.variable_type, tuple):
            for x in self.variable:
                if predicate != x:
                    return False
            return True
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
        if not type_compliance(self.variable, list, map):
            raise TypeError("Can only use copy_of() on PyKot(list) or PyKot(map)")
        return PyKot(self.variable.copy(), True)

    def equals(self, other):  # .equals(other)
        return self.variable == other

    def put(self, key, value):  # .put(key, value)
        if not type_compliance(self.variable, map):
            raise TypeError("Can only use .put() on PyKot(map)")
        self.variable[key] = value
        return PyKot(self.variable, True)

    def get_or_put(self, key, value):  # .getOrPut(key) {value}
        if not type_compliance(self.variable, map):
            raise TypeError("Can only use .get_or_put() on PyKot(map)")
        if key not in self.variable.keys():
            self.variable[key] = value
            return PyKot(self.variable, True)
        return self.variable[key]

    def sub_list(self, from_index: int, to_index: int):  # subList(fromIndex, toIndex)
        if not type_compliance(self.variable, list, tuple):
            raise TypeError("Can only use sub_list(from_index, to_index) on PyKot(list) or PyKot(mutableList)")
        return PyKot(self.variable[from_index:to_index], True)


def println(string):
    print(string)


def regex(regex_expression):
    return regex_expression, False, True


def list_of(*args):
    if isinstance(args, int) or isinstance(args, str):
        return PyKot(args, False)
    return PyKot(tuple([element for element in args]), False)


def empty_list():  # emptyList<Any>()
    return PyKot([], False)


def mutable_list_of(*args):  # mutableListOf(element, ..., element)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot([args], False)
    return PyKot([element for element in args], False)


def array_of(*args):  # arrayOf(element, ..., element)
    if len(args) == 0:
        return PyKot([], False)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot([args], False)
    return PyKot([element for element in args], False)


def empty_array():  # emptyArray()
    return PyKot([]), False


def int_array_of(*args):  # intArrayOf(int,..., int)
    int_array = []
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("Can only use int_Array_of(int) with int type elements")
        int_array.append(arg)
    return PyKot(int_array), False


def array_of_nulls(size=0):  # arrayOfNulls(int)
    null_array = []
    for i in range(size):
        null_array.append(None)
    return PyKot(null_array), False


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
    return It("it")


class It:
    # functions seen with it syntax
    # filter

    def __init__(self, identity):
        self.identity = identity

    def __add__(self, additive):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) + additive
        return lambda x: x + additive

    def __lt__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) < comparison
        return lambda x: x < comparison

    def __le__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) <= comparison
        return lambda x: x <= comparison

    def __eq__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) == comparison
        return lambda x: x == comparison

    def __ne__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) != comparison
        return lambda x: x != comparison

    def __gt__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) > comparison
        return lambda x: x > comparison

    def __ge__(self, comparison):
        if type_compliance(self.identity, type(lambda: 0)):
            return lambda x: self.identity(x) >= comparison
        return lambda x: x >= comparison

    def contains(self, string):
        self.identity += f".contains('{string}')"
        return lambda x: string in x, f"contains('{string}')"

    def starts_with(self, string):
        self.identity += f".startsWith('{string}')"
        return string, f"startsWith('{string}')"

    def length(self):
        return It(lambda x: len(x))

    def uppercase_char(self):
        pass

    def uppercase(self):
        # research different locales
        pass


def type_compliance(variable, *args):
    """
    Validate a variable's data type as acceptable and returns True or False
    :param variable:
    :param args: collection of acceptable data types
    :return:
    """
    return_list = []
    for arg in args:
        if isinstance(variable, arg):
            return_list.append(True)
        else:
            return_list.append(False)
    return True if True in return_list else False
