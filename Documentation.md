# Documentation

All Kotlin functions and methods in PyKot are called using the same name in snake_case instead of lowerCamelCase.

### Examples:
map_of() instead of mapOf()

.to_string() instead of .toString()

## PyKot Functions
### list_of()
```python
list_of(1, 2, 3)  # PyKot((1, 2, 3))
```
### empty_list()
```python
empty_list()  # PyKot(())
```
### mutable_list_of()
```python
mutable_list_of(1, 2, 3)  # PyKot([1, 2, 3])
```
### array_of()
```python
array_of('1', '2', '3')  # PyKot(['1' '2' '3'])
```
### empty_array()
```python
empty_array()  # PyKot([ ])
```
### int_array_of()
```python
int_array_of(1, 2, 3)  # PyKot([1 2 3])
```
### array_of_nulls()
```python
array_of_nulls(4)  # PyKot([None None None None])
```
### map_of()
```python
map_of(1, '1', 2, '2', 3, '3')  # PyKot({1: '1', 2: '2', 3: '3'})
map_of((1, '1'), (2, '2'), (3, '3'))  # PyKot({1: '1', 2: '2', 3: '3'})
```
### mutable_map_of()
```python
mutable_map_of(1, '1', 2, '2', 3, '3')  # PyKot({1: '1', 2: '2', 3: '3'})
mutable_map_of((1, '1'), (2, '2'), (3, '3'))  # PyKot({1: '1', 2: '2', 3: '3'})
```
### elvis_operator()
```python
x = None
y = 'Not None'
elvis_operator(x, y)  # 'Not None'

x = 'No longer None'
elvis_operator(x, y)  # 'No longer None'
```
### println()
```python
println('Hello PyKot')  # 'Hello PyKot'
```

## PyKot Methods (Coming Soon)







