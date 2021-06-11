# - PyKot - Alpha v0.05
Pykot is a Kotlin style syntax wrapper for Python.

## Installing PyKot (coming soon)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyKot.

```bash
pip install PyKot
```

## How To Wrap Data By Type
Data must be wrapped prior to using Kotlin style methods and unwrapped if you want the naked data.

### String
```python
# wrapping String
String = PyKot('Example String')

# unwrapping String
String.var
```

### Int
```python
# wrapping Int
Int = PyKot(123)

# unwrapping Int
Int.var
```

### MutableList
```python
# wrapping MutableList
MutableList = PyKot(['L', 'i', 's', 't'])
MutableList = mutable_list_of('L', 'i', 's', 't')

# unwrapping MutableList
MutableList.var 
```

### List
```python
# wrapping List
List = PyKot(('L', 'i', 's', 't'))
List = list_of('L', 'i', 's', 't')

# unwrapping List
List.var
```

### Array
```python
# wrapping Array
Array = PyKot(np.array('A', 'r', 'r', 'a', 'y'))
Array = array_of('A', 'r', 'r', 'a', 'y')

# unwrapping Array
Array.var
```

### Map
```python
# wrapping Map
Map = PyKot({dict_key: dict_value})
Map = map_of(key, value, key, value)
Map = map_of((key, value), (key, value))

# unwrapping Map
Map.var
```

## Usage
```python
from PyKot import *

# String examples
example_string = PyKot('example string')

example_string.drop_while(it() == 'e').to_string().var # returns 'xample string'
example_string.split(regex(r'\s')).var # returns ['example', 'string']

# Int examples
example_int = PyKot(123)

example_int.to_string().var # returns '123'
example_int.plus(5).var # returns 128

# List examples
example_list = list_of(1, 2, 3)

example_list.contains(2).var # returns True
example_list.to_mutable_list().var # returns [1, 2, 3]

# MutableList examples
example_mutable_list = mutable_list_of('123', '234', '345', '222')

example_mutable_list.find_last(it().starts_with('2')).var # return '222'
example_mutable_list.add("111").var  # returns ['123', '234', '345', '222', '111']

# Array examples
example_array = array_of(1, 2, 3)

example_array.all(2).var # returns False
example_array.to_mutable_list().var # returns [1, 2, 3]

# Map examples
example_map = map_of((1, '1'), (2, '2'), (3, '3'))

example_map.contains(2).var # return True
println(example_map).var # {1: '1', 2: '2', 3: '3'}
```

## Contributing
Lowest-lift assistance would be to post Kotlin code with no current PyKot method equivalent as an issue and i'll work to include it. Need as many compilable inline "it" examples as possible to improve PyKot mimicry. 

Pull requests to contribute directly. Open an issue if you have large changes in mind so the changes can be discussed. 

Tests must be updated appropriately.

## License
[BSD 3-Clause](https://https://opensource.org/licenses/BSD-3-Clause)
