## String interpolation (String Template Expressions) using $ syntax
    solution:   USE f-string syntax: f"I am {age} years old."
                INSTEAD OF: "I am $age years old."

## Cannot concatenate Int with String data types using the + operator in println statements.
    solutions:  (1) USE f-string syntax: f"Yes, it's {PyKot(string).length()} characters long."
                INSTEAD OF: "Yes, it's " + (string.length) + " characters long."
                
                (2) USE type casting to convert Int to String with str(): str(122) + "bottles of beer on the wall."
                INSTEAD OF: 122 + "bottles of beer on the wall."

## Raw strings
    solution:   USE Python's raw string syntax: r'\\_\\"\'
                INSTEAD OF: """\\_\\"\"""
                
## Multiple variable inline functions using '->' syntax
While single variable inline functions using it() have been maintained, multiple variable inline functions using '->' haven't.

    solution:   USE Python's lambda syntax: lambda x, y, z: (x + y) > z
                INSTEAD OF: z, y, z -> (x + y) > z

## if/else operation order for in-method use must use python syntax
    
    solution:   USE: x if condition else y
                INSTEAD OF: if (condition) x else y
                
    example:    USE: grouped_map.aggregate( lambda key, accumulator, element, first: 
                StringBuilder().append(key).append(":").append(element) if first else accumulator.append("-").append(element))
                
                INSTEAD OF: grouped_map.aggregate( key, accumulator, element, first ->
                if (frist) StringBuilder().append(key).append(":").append(element) else accumulator.append("-").append(element))
    

## Using it() expressions on the right hand side of arithmetic operator
The left operand is resolved into a base type prior to evaluating the right side so the interpter attempts to use native operators on 'it' which results in TypeError.

    solutions:  (1) Mathametically simply expression.
                USE (it() ** 2)
                INSTEAD OF: (it() * it())
                    TypeError: unsupported operand type(s) for *: 'int' and 'It'

## mapOf() "to" syntax
    solution:   use map_of(2, "two", 3, "three") or map_of((2, "two"), (3, "three"))
                INSTEAD OF: mapOf(2 to "two", 3 to "three") 

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
                INSTEAD OF: first_return ?: second_return
                
## Apply syntax for Object assignments
    solution:      INSTEAD OF                                  USE
                Object.apply {                          Object.apply(
                name = 'John'                           ('name', 'John')
                age = 30                                ('age', 30)
                }                                       )

                
## All functions and methods are now eager instead of lazy:
    examples: as_sequence(), sequence(), with_index()

## Functions/Methods which act on character sequences and strings are identical due to char data type being non-existent in python.
