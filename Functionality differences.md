## Can not concatenate Int with String data types using the + operator in println statements.
    solutions:  (1) Use f-string - f"Yes, it's {PyKot(string).length()} characters long."
                Instead of: "Yes, it's " + (string.length) + " characters long."
                
                (2) type cast Int to String with str() - str(122) + "bottles of beer on the wall."
                instead of: 122 + "bottles of beer on the wall."

## String interpolation (String Template Expressions) using $ syntax
    solution:   Use f-string - f"I am {age} years old."
                instead of: "I am $age years old."

## Raw strings
    solution:   Use Python's raw string syntax instead - r'\\_\\"\'
                instead of: """\\_\\"\"""

## multiple split delimiters using split()
    solutions:  (1) use regex lib, re.split( delimiter1 | delimiter2, input_string)
                (2) replace() all planned delimiters with a unique tag and split(unique_tag)
                (3) perform nested splits or sequential splits and aggregate lists

## mapOf() "to" syntax
    solution:   use map_of(2, "two", 3, "three") or map_of((2, "two"), (3, "three"))
                instead of: mapOf(2 to "two", 3 to "three") 

## do-while loops (post-test loop)
    solution:      INSTEAD OF                                  USE
                                                        loop = True
                do {                                    while loop:
                    doCode                                  do_code
                    doCode                                  do_code
                    doCode                                  do_code
                 } while (condition)                        if condition:
                                                                loop = False

## repeat() loops
    solution:     INSTEAD OF                                   USE
                repeat(n) {                             for i in range(n):
                    repeatedCode                            repeated_code
                }

## when/when else statements
    solution:      INSTEAD OF                                  USE
                when (variable) {                       if variable == 1:
                    1 -> {                                  code_if_one
                        codeIfOne                       elif variable == 2:
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
                
## Apply syntax for Object assignments
    solution:      INSTEAD OF                                  USE
                Object.apply {                          Object.apply(
                name = 'John'                           ('name', 'John')
                age = 30                                ('age', 30)
                }                                       )

                
## Functions that are now eager instead of lazy:
as_sequence(), sequence(), with_index()

## Functions which act on sequences and strings are identical due to char data type being non-existent in python.
