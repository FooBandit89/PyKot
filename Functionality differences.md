## Thunks from as_sequence() and sequence() are not maintained. Both as_sequence() and sequence() are both eager.

## sub_sequence() and sub_string() are identical due to char data type being non-existent in python.

## Can not concatenate Int data type with String data type in println statements.
    solutions:  (1) Use f-string - f"Yes, it's {PyKot(string).length()} characters long."
                Instead of: "Yes, it's " + (string.length) + " characters long."
                
                (2) type cast Int to String with str() - str(122) + "bottles of beer on the wall."
                instead of: 122 + "bottles of beer on the wall."

## String interpolation (String Template Expressions)
    solution:   Use f-string - f"I am {age} years old."
                instead of: "I am $age years old."

## Raw strings
    solution:   Use Python's raw string syntax instead - r'\\_\\"\' -> \\_\\"\
                instead of: """\\_\\"\""" -> \\_\\"\

## multiple split delimiters using split()
    solution:   (1) use regex lib, re.split( delimiter1 | delimiter2, input_string)
                (2) replace() all planned delimiters with a unique tag and split(unique_tag)
                (3) perform nested splits or sequential splits and aggregate lists

## mapOf() "to" syntax
    solution:   use map_of(2, "two", 3, "three") or map_of((2, "two"), (3, "three"))
                instead of: mapOf(2 to "two", 3 to "three") 

## do-while loops (post-test loop)
    solution:                                           loop = True
                do {                                    while loop:
                    doCode                                  do_code
                    doCode                                  do_code
                    doCode                                  do_code
                 } while (condition)                        if condition:
                                                                loop = False

## repeat() loops
    solution:   repeat(n) {                             for i in range(n):
                    repeatedCode                            repeated_code
                }

## when/when else statements
    solution:   when (variable) {                       if n == 1:
                    1 -> {                                  code_if_one
                        codeIfOne                       elif n == 2:
                    }                                       code_if_two
                    2 -> {                              else:
                        codeIfTwo                           code_if_else
                    }
                }
                else {
                    codeIfElse
                }

## Elvis operator syntactical sugar
    solution:   elvis_operator(first_return, second_return)
                instead of: first_return ?: second_return
