# streamlit-state

A thin wrapper for session state in Streamlit.

## 📖

### Import the `state` function

```python
from src.streamlit_state import state
```

### Initialise a session state variable

```python
my_state = state(key='my_state', initial=None)  # my_state: State[None]
```

### Get the current value of a state variable

```python
# Call the function with no arguments to get the current state
>>> print(my_state())
None
```

### Update the state with a value

```python
# Pass a value to update the state
>>> my_state = my_state(0)  # my_state: State[int]
>>> print(my_state())
0
```

### Update the state with a function

```python
# The function takes the current state as its argument
>>> my_state = my_state(lambda x: x + 1)  # my_state: State[int]
>>> print(my_state())
1
```

```python
>>> my_state = my_state({1, 2, 3})  # my_state: State[set[int]]
>>> my_state = my_state(sum)  # my_state: State[int]
>>> print(my_state())
6
```

### Update the state with a callable object

```python
>>> my_state = my_state(float)  # my_state: State[float]
>>> print(my_state())
6.0
```
