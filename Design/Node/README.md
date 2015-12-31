# node.py, Class: Node
Aiming for simple and bidirectional node

## Logging 
```Python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```
**_Usage_** 
```Python
logging.debug(('Insert debug here', variable_here'))
```

## Constructor
Four variables: `Name`, `Value`, `Prev`, and `Next`
* `Name` : Name/ID of the node
* `Value`: Value Contain of the node
* `Prev` : Previous Node pointer
* `Next` : Next Node pointer

Constructor Argument:
```Python
example= Node(name_of_node, value_of_node, prev_node, next_node)
```

## Set Variables
Setting Individual Variable:
```python
setName_of_Variable(desired_variable)
```
e.g.: `example.setName('foo')`

Setting Entire Variables:
```python
setAll(desired_Name, desired_Value, desired_Prev, desired_Next)
```
e.g.: `example.setAll('foo', 1234, example2, example3)`

## Return Variables
Methods:
```Python
returnName_of_Variable
```
e.g. `name = example.returnName()`
