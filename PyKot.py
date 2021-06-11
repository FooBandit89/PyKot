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

it_function_dict = {}


class Accumulator:

    def __init__(self, accumulation_seed):
        self.accumulation_seed = accumulation_seed

    def append(self, element_or_substring):
        if isinstance(self.accumulation_seed, str):
            self.accumulation_seed += element_or_substring
        elif isinstance(self.accumulation_seed, list):
            self.accumulation_seed.append(element_or_substring)
        return Accumulator(self.accumulation_seed)


class StringBuilder:

    def __init__(self):
        self.string = ''

    def __new__(cls):
        return Accumulator('')


class PyKot:

    def __init__(self, variable, recall=False):
        self.variable = variable
        self.recall = recall
        self.var = variable

    def __repr__(self):
        return str(self.variable)

    def last_index(self):  # lastIndex()
        raise_type_error_if_merited("last_index()", self.variable, str, list, tuple, type(np.array([])))
        return PyKot(len(self.variable) - 1)

    def drop(self, drop_from_front: int):  # drop(n)
        raise_type_error_if_merited("drop(Int)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        result = self.variable[drop_from_front:]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def drop_last(self, drop_from_back: int):  # dropLast(n)
        raise_type_error_if_merited("drop_last(Int)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        result = self.variable[:(len(self.variable) - drop_from_back)]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def drop_while(self, it_expression):  # dropWhile(it expression)
        raise_type_error_if_merited("drop_while(it expression)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        while it_expression.in_line_function(self.variable[0]):
            self.variable = self.variable[1:]
        result = post_type_work(self.variable, original_type)
        return PyKot(result, True)

    def drop_last_while(self, it_expression):  # dropLastWhile(it expression)
        raise_type_error_if_merited("drop_last_while(it expression)",
                                    self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        while it_expression.in_line_function(self.variable[-1]):
            self.variable = self.variable[:-1]
        result = post_type_work(self.variable, original_type)
        return PyKot(result, True)

    def take(self, take_from_front: int):  # take(n)
        raise_type_error_if_merited("take(Int)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        result = self.variable[:take_from_front]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def take_last(self, take_from_back: int):  # take_last(n)
        raise_type_error_if_merited("take_last(Int)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        result = self.variable[len(self.variable) - take_from_back:]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def take_while(self, it_expression):  # take_while(it expression)
        raise_type_error_if_merited("take_while(it expression)", self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        if type_compliance(self.variable, str):
            result = ''
            while it_expression.in_line_function(self.variable[0]):
                result += self.variable[0]
                self.variable = self.variable[1:]
        else:
            result = []
            while it_expression.in_line_function(self.variable[0]):
                result.append(self.variable[0])
                self.variable = self.variable[1:]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def take_last_while(self, it_expression):  # take_last_while(it expression)
        raise_type_error_if_merited("take_last_while(it expression)",
                                    self.variable, str, list, tuple, type(np.array([])))
        self.variable, original_type = pre_type_work(self.variable)
        if type_compliance(self.variable, str):
            result = ''
            while it_expression.in_line_function(self.variable[-1]):
                result += self.variable[-1]
                self.variable = self.variable[:-1]
        else:
            result = []
            while it_expression.in_line_function(self.variable[-1]):
                result.append(self.variable[-1])
                self.variable = self.variable[:-1]
        result = post_type_work(result, original_type)
        return PyKot(result, True)

    def length(self):  # length()
        raise_type_error_if_merited("length()", self.variable, str, list, tuple, type(np.array([])))
        return PyKot(len(self.variable))

    def first(self):  # first()
        raise_type_error_if_merited("first()", self.variable, str, list, tuple, type(np.array([])))
        return PyKot(self.variable[0], True)

    def last(self):  # last()
        raise_type_error_if_merited("last()", self.variable, str, list, tuple, type(np.array([])))
        return PyKot(self.variable[-1], True)

    def trim_margin(self, margin="|"):  # trimMargin(margin)
        raise_type_error_if_merited("trim_margin(margin='|')", self.variable, str)
        return PyKot(self.variable[(self.variable.find(margin) + len(margin)):], True)

    def compare_to(self, comparison: str, ignorecase=False):  # compareTo(String, ignorecase=False)
        self.variable, original_type = pre_type_work(self.variable)
        comparison, original_type_comparison = pre_type_work(comparison)
        if type_compliance(self.variable, dict):
            self.variable = tuple(self.variable)
        if type_compliance(comparison, dict):
            comparison = tuple(comparison)
        if ignorecase:
            self.variable = self.variable.lower()
            comparison = comparison.lower()
        original = [self.variable, comparison]
        sort_compare = [self.variable, comparison]
        sort_compare.sort()
        sort_compare = -1 if sort_compare == original else 1
        return PyKot(0 if self.variable == comparison else sort_compare)

    def sub_string(self, first_index, second_index):  # subString(i, j)
        raise_type_error_if_merited("sub_string(Int, Int)", self.variable, str)
        first_index, valid1, second_index, valid2 = unwrap_it(first_index, second_index)
        if valid1:
            first_index = first_index(self.variable)
        if valid2:
            second_index = second_index(self.variable)
        return PyKot(self.variable[first_index: second_index], True)

    def split(self, delimiter=' ', *additional_delimiters, ignorecase=False):  # split(delimiter) or
        # split(delimiter, ignorecase=True) or split(delimiter.toRegex()) or split(regex(delimiter))
        raise_type_error_if_merited("split(delimiter=' ', *additional_delimiters, ignorecase=False)",
                                    self.variable, str)
        if ignorecase:
            string = self.variable.lower()
            delimiter_list = [delimiter.lower()] + [d.lower() for d in additional_delimiters]
        else:
            string = self.variable
            delimiter_list = [delimiter] + [d for d in additional_delimiters]

        if type_compliance(delimiter, type(re.compile(''))):
            result = re.split(delimiter, self.variable)
        else:
            delimiter_indexes = []
            found = 0
            for delimiter in delimiter_list:
                while found != -1 and (len(string) - found) >= len(delimiter):
                    found = string.find(delimiter, found, len(string) - 1)
                    if found == -1:
                        continue
                    delimiter_indexes.append(found)
                    found += len(delimiter)
                    delimiter_indexes.append(found)

                found = 0

            delimiter_indexes.append(0)
            delimiter_indexes.sort()
            delimiter_indexes.append(-1)
            di = iter(delimiter_indexes)
            delimiter_indexes = list(zip(di, di))
            result = [self.variable[i:] if j == -1 else self.variable[i: j] for i, j in delimiter_indexes]

        return PyKot(tuple(result), True)

    def sub_sequence(self, first_index: int, second_index: int):  # subSequence(i, j)
        raise_type_error_if_merited("sub_string(Int, Int)", self.variable, str)
        first_index, valid1, second_index, valid2 = unwrap_it(first_index, second_index)
        if valid1:
            first_index = first_index(self.variable)
        if valid2:
            second_index = second_index(self.variable)
        return PyKot(self.variable[first_index: second_index], True)

    def lines(self):  # lines()
        raise_type_error_if_merited("lines()", self.variable, str)
        return PyKot(self.variable.splitlines(), True)

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
        raise_type_error_if_merited("ends_with(String)", self.variable, str, list, tuple, type(np.array([])))
        if type_compliance(self.variable, str):
            result = True if self.variable[-len(substring):] == substring else False
        else:
            self.variable = unpack_array(self.variable)
            result = True
            for element in self.variable:
                if not type_compliance(element, str):
                    raise TypeError("All elements in iterable must be a String to use ends_with()")
                if result:
                    result = True if element[-len(substring):] == substring else False
        return PyKot(result, True)

    def plus(self, string_or_int):  # plus(String) or plus(Int)
        raise_type_error_if_merited("plus(String) or plus(Int)", self.variable, str, int)
        if type_compliance(self.variable, str) and type_compliance(string_or_int, int):
            string_or_int = str(string_or_int)
        elif type_compliance(self.variable, int) and type_compliance(string_or_int, str):
            string_or_int = int(string_or_int)
        return PyKot(self.variable + string_or_int, True)

    def get(self, index):  # get()
        raise_type_error_if_merited("get(Int)", self.variable, str, list, tuple, type(np.array([])), dict)
        if isinstance(self.variable[index], type(np.array([1])[0])):
            result = int(self.variable[index])
        elif isinstance(self.variable[index], type(np.array([1.0])[0])):
            result = float(self.variable[index])
        elif isinstance(self.variable, dict):
            result = self.variable[index] if index in self.variable.keys() else None
        else:
            result = self.variable[index]
        return PyKot(result, True)

    def to_string(self):  # toString()
        raise_type_error_if_merited("to_string()", self.variable, str, int, list, tuple, range, dict)
        if isinstance(self.variable, str):
            result = self.variable
        else:
            result = str(self.variable)
        return PyKot(result, True)

    def content_to_string(self):  # contentToString()
        raise_type_error_if_merited("content_to_string()", self.variable, list, tuple, type(np.array([])))
        return PyKot(str([x for x in self.variable]), True)

    def any(self, predicate=None):  # any(predicate)
        raise_type_error_if_merited("any(), any(value), or any(predicate)",
                                    self.variable, list, tuple, dict, type(np.array([])))
        result = unpack_array(self.variable)
        if type_compliance(predicate, type(it())):
            predicate = predicate.in_line_function
        if type_compliance(self.variable, dict):
            if not type_compliance(predicate, str, int):
                result = True if len(list(filter(predicate, self.variable.items()))) > 0 else False
        else:
            if not type_compliance(predicate, str, int):
                result = True if len(list(filter(predicate, result))) > 0 else False
        if type_compliance(predicate, str, int):
            if type_compliance(self.variable, dict):
                result = True if predicate in self.variable.keys() else False
            else:
                result = True if predicate in self.variable else False
        if predicate is None:
            if self.variable:
                result = True
            else:
                result = False
        return PyKot(result, True)

    def none(self):  # any(predicate)
        raise_type_error_if_merited("any(), any(value), or any(predicate)",
                                    self.variable, list, tuple, dict, type(np.array([])))
        return PyKot(False if unpack_array(self.variable) else True, True)

    def to_list(self):  # toList()
        raise_type_error_if_merited("to_list()", self.variable, list, tuple, dict, type(np.array([])))
        if type_compliance(self.variable, tuple):
            result = self.variable
        elif type_compliance(self.variable, dict):
            result = tuple([(key, self.variable[key]) for key in self.variable.keys()])
        else:
            result = tuple(self.variable)
        return PyKot(result, True)

    def to_mutable_list(self):  # toMutableList()
        raise_type_error_if_merited("to_mutable_list()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, tuple):
            result = list(self.variable)
        elif type_compliance(self.variable, dict):
            result = [(key, self.variable[key]) for key in self.variable.keys()]
        elif type_compliance(self.variable, type(np.array([]))):
            result = [x for x in unpack_array(self.variable)]
        else:
            result = self.variable
        return PyKot(result, True)

    def contains(self, element):  # contains(element)
        raise_type_error_if_merited("contains()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, dict):
            return PyKot(element in self.variable.keys(), True)
        return PyKot(element in self.variable, True)

    def filter(self, predicate):  # filter(predicate)
        raise_type_error_if_merited("filter(function)", self.variable, list, tuple, dict, type(np.array([])))
        predicate = predicate.in_line_function
        if type_compliance(self.variable, dict):
            new_map = dict(tuple(filter(predicate, self.variable.items())))
            result = new_map
        else:
            result = list(filter(predicate, self.variable))
        return PyKot(result, True)

    def filter_not(self, predicate):  # filterNot(predicate)
        raise_type_error_if_merited("filter_not(function)", self.variable, list, tuple, dict, type(np.array([])))
        predicate = predicate.in_line_function
        if type_compliance(self.variable, dict):
            new_map = {}
            do_not_include = list(filter(predicate, self.variable.items()))
            do_not_include = [x for x, y in do_not_include]
            for key in self.variable.keys():
                if key not in do_not_include:
                    new_map[key] = self.variable[key]
            result = new_map
        else:
            new_list = []
            do_not_include = list(filter(predicate, self.variable))
            for value in [unpack_array_element(x) for x in self.variable]:
                if value not in do_not_include:
                    new_list.append(value)
            result = new_list
        return PyKot(result, True)

    def filter_indexed(self, predicate):  # filter_indexed(predicate)
        raise_type_error_if_merited("filter_indexed(predicate)", self.variable, list, tuple, type(np.array([])))
        raise_type_error_if_merited("filter_indexed()", predicate, type(lambda x: x))
        return PyKot([y for x, y in enumerate(unpack_array(self.variable)) if predicate(x, y)], True)

    def filter_not_null(self):  # filter_not_null()
        raise_type_error_if_merited("filter_not_null()", self.variable, list, tuple, type(np.array([])))
        return PyKot([x for x in unpack_array(self.variable) if x is not None])

    def filter_is_instance(self, acceptable_type):  # filter_is_instance(type)
        raise_type_error_if_merited("filter_is_instance(acceptable_type)",
                                    self.variable, list, tuple, type(np.array([])))
        return PyKot([x for x in unpack_array(self.variable) if type(x) == acceptable_type])

    def partition(self, predicate):  # partition(predicate)
        raise_type_error_if_merited("partition(predicate)", self.variable, list, tuple, type(np.array([])))
        if type_compliance(predicate, type(it())):
            predicate = predicate.in_line_function
        match = []
        rest = []
        for element in unpack_array(self.variable):
            if predicate(element):
                match.append(element)
            else:
                rest.append(element)
        return PyKot((tuple(match), tuple(rest)), True)

    def for_each(self, *statements):  # forEach( statements )
        raise_type_error_if_merited("for_each(*statements)", self.variable, list, tuple, type(np.array([])), dict)
        if type_compliance(self.variable, dict):
            useful_list = [PyKot(self.variable[x]) for x in self.variable.keys()]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        else:
            useful_list = [PyKot(unpack_array_element(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        return PyKot(self.variable, True)

    def also(self, *statements):  # also( statements )
        raise_type_error_if_merited("also(*statements)", self.variable,
                                    str, int, range, list, tuple, type(np.array([])), dict)
        if type_compliance(self.variable, dict):
            useful_list = [PyKot(self.variable[x]) for x in self.variable.keys()]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, range, list, tuple, type(np.array([]))):
            useful_list = [PyKot(unpack_array_element(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, str, int):
            for statement in statements:
                statement(self.variable)
        return PyKot(self.variable, True)

    def let(self, *statements):  # let( statements )
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
            useful_list = [PyKot(unpack_array_element(x)) for x in self.variable]
            for value in useful_list:
                for statement in statements:
                    statement(value)
        elif type_compliance(self.variable, str, int):
            for statement in statements:
                statement(self.variable)
        return PyKot(self.variable, True)

    def find(self, predicate):  # find(predicate)
        raise_type_error_if_merited("find(predicate)", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        found = list(filter(predicate, self.variable))
        if len(found) == 0:
            return PyKot(None, True)
        return PyKot(found[0], True)

    def find_last(self, predicate):  # findLast(predicate)
        raise_type_error_if_merited("find_last(predicate)", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        found = list(filter(predicate, self.variable))
        if len(found) == 0:
            return PyKot(None, True)
        return PyKot(found[-1], True)

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

    def size(self):  # .size()
        raise_type_error_if_merited("size()", self.variable, list, tuple, type(np.array([])), dict)
        if type_compliance(self.variable, dict):
            return len(self.variable.items())
        return PyKot(len(self.variable), True)

    def min_or_null(self):  # minOrNull()
        raise_type_error_if_merited("min_or_null()", self.variable, list, tuple, type(np.array([])))
        if len(self.variable) == 0:
            return PyKot(None, True)
        useful_list = [unpack_array_element(x) for x in self.variable]
        useful_list.sort()
        return PyKot(useful_list[0], True)

    def min_by_or_null(self, predicate):  # minByOrNull(predicate)
        raise_type_error_if_merited("min_by_or_null()", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        useful_list = list(filter(predicate, [unpack_array_element(x) for x in self.variable]))
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
        useful_list = [unpack_array_element(x) for x in self.variable]
        useful_list.sort()
        return PyKot(useful_list[-1], True)

    def max_by_or_null(self, predicate):  # maxByOrNull(predicate)
        raise_type_error_if_merited("max_by_or_null()", self.variable, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        useful_list = list(filter(predicate, [unpack_array_element(x) for x in self.variable]))
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

    def add(self, element):  # add(element)
        raise_type_error_if_merited("add()", self.variable, list)
        self.variable.append(element)
        return PyKot(self.variable, True)

    def add_all(self, *args):  # addAll(elements)
        raise_type_error_if_merited("add_all(element) or add_all(element, ..., element)", self.variable, list)
        self.variable += [arg for arg in args]
        return PyKot(self.variable, True)

    def keys(self):  # keys()
        raise_type_error_if_merited("keys()", self.variable, dict)
        return PyKot(self.variable.keys(), True)

    def values(self):  # values()
        raise_type_error_if_merited("values()", self.variable, dict)
        return PyKot(self.variable.values(), True)

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

    def aggregate(self,
                  four_variable_lambda=lambda map_key_default,
                  accumulator_default=Accumulator([]), element_default=None, first_default=True:
                  accumulator_default.append(map_key_default).append(":").append(element_default) if first_default
                  else accumulator_default.append(element_default)):  # aggregate(lambda)
        raise_type_error_if_merited("aggregate(lambda_expression)", self.variable, dict)
        result = {}
        preliminary_result = []
        for map_key in self.variable.keys():
            first = True
            accumulator = Accumulator([])
            for value in self.variable[map_key]:

                temp = four_variable_lambda(map_key, accumulator, value, first)
                if first and isinstance(temp, type(Accumulator([]))):
                    accumulator = temp
                first = False
            preliminary_result.append(accumulator.accumulation_seed)
        for accumulation in preliminary_result:
            if type_compliance(accumulation, str):
                split_string = accumulation.split(":")
                result[split_string[0]] = split_string[1]
            elif type_compliance(accumulation, list):
                result[accumulation[0]] = accumulation[2]
                if len(accumulation) > 3:
                    for additional_element in accumulation[3:]:
                        result[accumulation[0]] += additional_element
        return PyKot(result, True)

    def set(self, index, value):  # set(index, value)
        raise_type_error_if_merited("set(index, value)", self.variable, list, type(np.array([])))
        if isinstance(self.variable, type(np.array([]))):
            list_array = [x for x in self.variable]
            list_array[index] = value
            self.variable = np.array(list_array)
        else:
            self.variable[index] = value
        return PyKot(self.variable, True)

    def indices(self):  # indices()
        raise_type_error_if_merited("indices()", self.variable, list, tuple, type(np.array([])))
        return PyKot(range(len(self.variable)), True)

    def is_empty(self):  # isEmpty()
        raise_type_error_if_merited("is_empty()", self.variable, list, tuple, dict, type(np.array([])))
        if isinstance(self.variable, range):
            result = True if self.variable == range(0) else False
        else:
            result = True if self.variable.indices() == range(0) else False
        return PyKot(result, True)

    def all(self, predicate=''):  # all()
        raise_type_error_if_merited("all() or all(predicate)", self.variable, str, list, tuple, type(np.array([])))
        predicate = predicate.in_line_function
        if type_compliance(predicate, type(lambda y: y)):
            result = True if len(list(filter(predicate, self.variable))) == len(self.variable) else False
        else:
            result = False
        if isinstance(self.variable, str):
            result = True if predicate == self.variable else False
        if isinstance(self.variable, list) or isinstance(self.variable, tuple):
            for x in self.variable:
                if predicate != x:
                    return PyKot(False, True)
            result = True
        return PyKot(result, True)

    def as_sequence(self):  # asSequence()
        return PyKot(tuple(self.variable), True)

    def as_iterable(self):  # asIterable()
        return PyKot(tuple(self.variable), True)

    def iterator(self):  # iterator()
        return PyKot(tuple(self.variable), True)

    def sequence(self):  # sequence()
        return PyKot(tuple(self.variable), True)

    def uppercase_char(self):  # uppercaseChar()
        if not isinstance(self.variable, str) or not len(self.variable) == 1:
            raise TypeError("Can only use uppercase_char() on PyKot(String) with a length of 1.")
        return PyKot(self.variable.upper(), True)

    def uppercase(self):  # uppercase()
        raise_type_error_if_merited("uppercase()", self.variable, str)
        return PyKot(self.variable.upper(), True)

    def copy_of(self):  # copyOf()
        raise_type_error_if_merited("copy_of()", self.variable, list, dict, tuple, type(np.array([])))
        return PyKot(self.variable.copy(), True)

    def equals(self, other):  # equals(other)
        return PyKot(self.variable == other, True)

    def put(self, key, value):  # put(key, value)
        raise_type_error_if_merited("put(key, value)", self.variable, dict)
        self.variable[key] = value
        return PyKot(self.variable, True)

    def get_or_put(self, key, value):  # getOrPut(key) {value}
        raise_type_error_if_merited("get_or_put(key, value)", self.variable, dict)
        if key not in self.variable.keys():
            self.variable[key] = value
            return PyKot(self.variable, True)
        return PyKot(self.variable[key], True)

    def sub_list(self, from_index: int, to_index: int):  # subList(fromIndex, toIndex)
        raise_type_error_if_merited("sub_list(index, index)", self.variable, list, tuple)
        return PyKot(self.variable[from_index:to_index], True)

    def map(self, lambda_function):
        if type_compliance(lambda_function, str):
            it_functions_hex_ids = re.findall(r'at\s(.*?)>', lambda_function)
            it_functions = []
            for hex_id in it_functions_hex_ids:
                if 'x0' in hex_id:
                    hex_id = hex_id.replace('x0', 'x')
                hex_id = hex_id.lower()
                if hex_id in it_function_dict.keys():
                    it_functions.append(it_function_dict[hex_id].in_line_function)
            results = [tuple(x(y) for x in it_functions) for y in self.variable]
            results = str(tuple(results))

        elif type_compliance(lambda_function, tuple):
            results = []
            for var in self.variable:
                sub_results = []
                for it_function in lambda_function:
                    it_function = it_function.in_line_function
                    sub_results.append(it_function(var))
                results.append(tuple(sub_results))
            results = tuple(results)

        else:
            lambda_function = lambda_function.in_line_function
            results = tuple([lambda_function(x) for x in self.variable])
        return PyKot(results, True)

    def assert_equals(self, other):  # assertEquals(other)
        if type_compliance(self, type(other)):
            if self != other:
                raise AssertionFailedError("Equals assertion failed.")
        if self.variable != other:
            raise AssertionFailedError("Equals assertion failed.")

    def assert_false(self):  # assertFalse()
        if self.variable:
            raise AssertionFailedError("False assertion failed.")

    def assert_true(self):  # assertTrue()
        if not self.variable:
            raise AssertionFailedError("True assertion failed.")

    def assert_not_null(self):  # assertNotNull()
        if self.variable is None:
            raise AssertionFailedError("Not Null assertion failed.")

    def assert_null(self):  # assertNull()
        if self.variable is not None:
            raise AssertionFailedError("Null assertion failed.")

    def assert_not_same(self, other):  # assertNotSame(other)
        if self == other:
            raise AssertionFailedError("Not Same assertion failed.")

    def assert_same(self, other):  # assertSame(other)
        if self != other:
            raise AssertionFailedError("Same assertion failed.")

    def take_if(self, it_expression):  # takeIf(it expression)
        if it_expression.in_line_function(self.variable):
            return PyKot(self.variable, True)
        return PyKot(None, True)

    def take_unless(self, it_expression):  # takeUnless(it expression)
        if it_expression.in_line_function(self.variable):
            return PyKot(None, True)
        return PyKot(self.variable, True)

    def index_of(self, target):  # indexOf(target)
        type_compliance(self.variable, str, list, tuple, type(np.array([])))
        if isinstance(self.variable, str):
            return PyKot(self.variable.find(target), True)
        if target in self.variable:
            return PyKot([unpack_array_element(x) for x in self.variable].index(target), True)
        return PyKot(-1, True)

    def entries(self):  # entries()
        raise_type_error_if_merited("entries()", self.variable, dict)
        return PyKot(tuple([(x, y) for x, y in self.variable.items()]), True)

    def clear(self):  # clear()
        raise_type_error_if_merited("clear()", self.variable, dict)
        return PyKot({}, True)

    def contains_key(self, key):  # containsKey(key)
        aise_type_error_if_merited("contains_key(key)", self.variable, dict)
        return PyKot(True if key in self.variable.keys() else False, True)

    def contains_value(self, value):  # containsValue(value)
        aise_type_error_if_merited("contains_value(value)", self.variable, dict)
        return PyKot(True if value in self.variable.values() else False, True)

    # class methods
    def apply(self, *assignments):
        for assignment in assignments:
            setattr(self.variable, assignment[0], assignment[1])
        return PyKot(self.variable, True)


def println(string):  # println()
    if type_compliance(string, type(it())):
        string = string.in_line_function
        return lambda x: print(string(x))
    print(string)


def regex(regex_expression):  # regex(regular_expression)
    return re.compile(regex_expression)


def list_of(*args):  # listOf(elements)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot(args, False)
    return PyKot(tuple([element for element in args]), False)


def empty_list():  # emptyList<Any>()
    return PyKot(tuple(), False)


def mutable_list_of(*args):  # mutableListOf(elements)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot([args], False)
    return PyKot([element for element in args], False)


def array_of(*args):  # arrayOf(elements)
    if len(args) == 0:
        return PyKot(np.array([]), False)
    if isinstance(args, int) or isinstance(args, str):
        return PyKot(np.array([args]), False)
    return PyKot(np.array([element for element in args]), False)


def empty_array():  # emptyArray()
    return PyKot(np.array([]), False)


def int_array_of(*args):  # intArrayOf(elements)
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


def map_of(*args):  # mapOf()
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


def mutable_map_of(*args):  # mutableMapOf()
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


def hash_map():  # hashMap()
    return PyKot({}, False)


def elvis_operator(not_null_return, alternative_return):  # not_null_return ?: alternative_return
    if type_compliance(not_null_return, type(PyKot(''))):
        not_null_return = not_null_return.variable
    if type_compliance(alternative_return, type(PyKot(''))):
        alternative_return = alternative_return.variable
    if not_null_return:
        return_value = not_null_return
    else:
        return_value = alternative_return
    return PyKot(return_value, True)


def it():  # it
    return It(lambda x: x)


class It:

    def __init__(self, in_line_function):
        self.in_line_function = in_line_function

    def __add__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) + other))

    def __sub__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) - other))

    def __mul__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) * other))

    def __truediv__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) / other))

    def __pow__(self, power):
        return return_function(It(lambda x: self.in_line_function(x) ** power))

    def __lt__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) < comparison))

    def __le__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) <= comparison))

    def __eq__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) == comparison))

    def __ne__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) != comparison))

    def __gt__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) > comparison))

    def __ge__(self, comparison):
        return return_function(It(lambda x: self.in_line_function(x) >= comparison))

    def __mod__(self, modulo):
        return return_function(It(lambda x: self.in_line_function(x) % modulo))

    def __and__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) & other))

    def __or__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) | other))

    def __xor__(self, other):
        return return_function(It(lambda x: self.in_line_function(x) ^ other))

    def __invert__(self):
        return return_function(It(lambda x: ~self.in_line_function(x)))

    def contains(self, string):
        return return_function(It(lambda x: string in self.in_line_function(x.keys()) if isinstance(x, dict)
                                  else string in self.in_line_function(x)))

    def starts_with(self, string, start_index=0, ignorecase=False):
        if ignorecase:
            function = It(lambda x: True if string.lower() == self.in_line_function(x)[start_index:len(string)].lower()
                          else False)
        else:
            function = It(lambda x: True if string == self.in_line_function(x)[start_index:len(string)]
                          else False)
        return return_function(function)

    def ends_with(self, string, ignorecase=False):
        if ignorecase:
            function = It(lambda x:
                          True if string.lower() == self.in_line_function(x)[-len(string):].lower()
                          else False)
        else:
            function = It(lambda x: True if string == self.in_line_function(x)[-len(string):]
                          else False)
        return return_function(function)

    def length(self):
        return return_function(It(lambda x: len(self.in_line_function(x))))

    def uppercase_char(self):
        return return_function(It(lambda x: self.in_line_function(x).upper()))

    def uppercase(self):
        return return_function(It(lambda x: self.in_line_function(x).upper()))

    def first(self):
        return return_function(It(lambda x: self.in_line_function(x)[0]))

    def code(self):
        return return_function(It(lambda x: ord(self.in_line_function(x))))

    def is_not_empty(self):
        return return_function(It(lambda x: True if not self.in_line_function(x)
                                  else False))

    def value(self):
        return return_function(It(lambda x: self.in_line_function(x)[1] if isinstance(x, tuple)
                                  else self.in_line_function(x)))

    def key(self):
        return return_function(It(lambda x: self.in_line_function(x)[0] if isinstance(x, tuple)
                                  else self.in_line_function(x)))

    def to_string(self):
        return return_function(It(lambda x: str(self.in_line_function(x))))

    def sum(self):
        return return_function(It(lambda x: sum(self.in_line_function(x))))


def type_compliance(variable, *args):
    """ Private: internal library function, not intended for public use. """
    return_list = []
    for arg in args:
        if isinstance(variable, arg):
            return_list.append(True)
        else:
            return_list.append(False)
    return True if True in return_list else False


def raise_type_error_if_merited(method: str, variable, *args, type_error_message=''):
    """ Private: internal library function, not intended for public use. """
    pykot_exchange = {
        str: "PyKot(String)",
        int: "PyKot(Int)",
        list: "PyKot(MutableList)",
        tuple: "PyKot(List)",
        dict: "PyKot(Map)",
        range: "PyKot(Range)",
        type(np.array([])): "PyKot(Array)",
        type(None): "PyKot(None)",
        type(lambda x: x): "lambda (->) functions"
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


def unpack_array(array):
    """ Private: internal library function, not intended for public use. """
    return [unpack_array_element(x) for x in array]


def unpack_array_element(element):
    """ Private: internal library function, not intended for public use. """
    if type_compliance(element, type([x for x in np.array([1])][0])):
        return int(element)
    elif type_compliance(element, type([x for x in np.array([1.0])][0])):
        return float(element)
    return element


def return_function(it_function):
    """ Private: internal library function, not intended for public use. """
    if hex(id(it_function)) not in it_function_dict:
        it_function_dict[hex(id(it_function))] = it_function
    return it_function


def pre_type_work(variable):
    """ Private: internal library function, not intended for public use. """
    original_type = type(variable)
    array = type(np.array([]))
    if original_type == array:
        variable = unpack_array(variable)
    if original_type == tuple:
        variable = list(variable)
    return variable, original_type


def post_type_work(result, original_type):
    """ Private: internal library function, not intended for public use. """
    array = type(np.array([]))
    if original_type == array:
        result = np.array(result)
    if original_type == tuple:
        result = tuple(result)
    return result


def unwrap_it(*it_expressions):
    """ Private: internal library function, not intended for public use. """
    results = []
    for it_expression in it_expressions:
        if isinstance(it_expression, type(it())):
            it_expression = it_expression.in_line_function
        results.append(it_expression)
        results.append(isinstance(it_expression, type(lambda x: x)))
    results = tuple(results)
    return results


class Error(Exception):
    pass


class AssertionFailedError(Error):

    def __init__(self, message):
        self.message = message
