# - PyKot - Alpha v0.04
Pykot is a Kotlin style syntax wrapper for Python.

## Installing PyKot (coming soon)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyKot.

```bash
pip install PyKot
```

## How To Wrap Data By Type
Data must be wrapped prior to using Kotlin style methods.

### String
```python
PyKot('Example String')
```

### Int
```python
PyKot(123)
```

### MutableList
```python
PyKot(['L', 'i', 's', 't'])
mutable_list_of('L', 'i', 's', 't')
```

### List
```python
PyKot(('L', 'i', 's', 't'))
list_of('L', 'i', 's', 't')
```

### Array
```python
PyKot(np.array('A', 'r', 'r', 'a', 'y'))
array_of('A', 'r', 'r', 'a', 'y')
```

### Map
```python
PyKot({dict_key: dict_value})
map_of(key, value, key, value)
map_of((key, value), (key, value))
```

## Usage
```python
from PyKot import *

# String examples
example_string = PyKot('example string')

example_string.drop_while(it() == 'e').to_string() # returns 'xample string'
example_string.split(regex(r'\s')) # returns ['example', 'string']

# Int examples
example_int = PyKot(123)

example_int.to_string() # returns '123'
example_int.plus(5) # returns 128

# List examples
example_list = list_of(1, 2, 3)

example_list.contains(2) # returns True
example_list.to_mutable_list() # returns [1, 2, 3]

# MutableList examples
example_mutable_list = mutable_list_of('123', '234', '345', '222')

example_mutable_list.find_last(it().starts_with('2')) # return '222'
example_mutable_list.add("111")  # returns ['123', '234', '345', '222', '111']

# Array examples
example_array = array_of(1, 2, 3)

example_array.all(2) # returns False
example_array.to_mutable_list() # returns [1, 2, 3]

# Map examples
example_map = map_of((1, '1'), (2, '2'), (3, '3'))

example_map.contains(2) # return True
println(example_map) # {1: '1', 2: '2', 3: '3'}
```

## Contributing
Lowest-lift assistance would be to post Kotlin code with no current PyKot method equivalent as an issue and i'll work to include it. Need as many compilable inline "it" examples as possible to improve PyKot mimicry. 

Pull requests to contribute directly. Open an issue if you have large changes in mind so the changes can be discussed. 

Tests must be updated appropriately.

## License
[BSD 3-Clause](https://https://opensource.org/licenses/BSD-3-Clause)
