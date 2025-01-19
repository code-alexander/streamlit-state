# streamlit-state

A thin wrapper for session state in [Streamlit](https://streamlit.io/).

## 🚀 TLDR

Install with [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```bash
pip install git+https://github.com/code-alexander/streamlit-state.git
```

or install with [uv](https://github.com/astral-sh/uv):

```bash
uv add git+https://github.com/code-alexander/streamlit-state
```

## 💡 Motivation

### Initialising variables

Streamlit session state variables have to be [initialised](docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state#initialize-values-in-session-state) as follows:

```python
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
```

This can get repetitive if you have many variables.

`streamlit-state` introduces an idempotent function that handles the conditional logic internally:

```python
my_state = state(key='my_state', initial=None)
```

### Typing

Streamlit session state variables are not typed:

```python
if 'my_state' not in st.session_state:
    st.session_state['my_state'] = None

current = st.session_state['my_state']
# (type) current = Any
```

Whereas `streamlit-state` keeps track of the type last assigned to the variable:

```python
my_state = state('my_state', initial=None)  # my_state: State[None]
current = my_state()  # current: None = None

my_state = my_state(0)  # my_state: State[int]
current = my_state()  # current: int = 0
```

You can even pass a function to update the state:

```python
# The function takes the current state as its argument
my_state = my_state(lambda x: x + 1)  # my_state: State[int]
current = my_state()  # current: int = 1
```

The type is inferred from the return type of the function (or other callable object):

```python
my_state = my_state(float)  # my_state: State[float]
current = my_state()  # current: float = 1.0
```

## 📖 Usage

### Import the `state` function

```python
from streamlit_state import state
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
