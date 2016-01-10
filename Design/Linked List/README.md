# linkedlist.py, Class: LinkedList
Aiming for bi-directional Liunked List. 

Will be implemented as a Tictactoe grid in future.

## Logging 
```Python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```
**_Usage_** 
```Python
logging.debug(('Insert debug here', variable_here'))
```

## Constructor
Three variables: `Head`, `Tail`, and `Size`
* `Head`: Head of the Linked List
* `Tail`: Tail of the Linked List
* `Size`: Size of the Linked List

Constructor Argument:
```Python
example = LinkedList() # No argument needed
```

## Setting Variables
Methods:
```Python
setName_of_Variable()
```
e.g. `head = example.setHead()`

## Returning Variables
Methods:
```Python
returnName_of_Variable()
```
e.g. `name = example.returnHead()`

## Custom Functions

### Exchange Node
Methods:
```Python
exchangenode(Node_A, Node_B)
```
e.g. `exchangeNode(TargetA, TargetB)`

### Push Node as Stack (First In Last Out)
```Python
pushS(Node_A)
```
e.g. `pushS(TargetA)`

### Pop Node as Stack (First In Last Out)
```python
popS()
```
e.g. `popS()`

## Search Functions
If target is not found, it'll be `None`.
### Search by Index
```Python
searchIndex(index)
```
e.g. `target = searchIndex(3)`
Note index starts with 0

### Search by Value
```Python
searchValue(value)
```
e.g. `target = searchValue(559)`

### Search by Name
```Python
searchName(name)
```
e.g. `target = searchName('target')`
