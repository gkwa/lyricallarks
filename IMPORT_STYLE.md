# Import Style Guide

This project uses **absolute imports** for all imports. This means we import the module itself, not individual items from the module.

## Pattern

❌ **Avoid** (relative imports):
```python
from typing import List, Dict, Optional
from pathlib import Path
from functools import wraps
from telemetry import get_telemetry
```

✅ **Use** (absolute imports):
```python
import typing
import pathlib
import functools
import telemetry
```

## Usage Examples

### Using typing
```python
import typing

def process(items: typing.List[str]) -> typing.Optional[dict]:
    result: typing.Dict[str, int] = {}
    callback: typing.Callable = lambda x: x
    return result
```

### Using functools
```python
import functools

def my_decorator(func: typing.Callable) -> typing.Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Using custom modules
```python
import telemetry
import greeter

t = telemetry.get_telemetry()
result = greeter.process_greeting("World")
```

## Benefits

1. **Explicit namespace**: Clear where each function/class comes from
2. **No name collisions**: Each module keeps its namespace
3. **Better refactoring**: Easier to track dependencies
4. **Consistent style**: Same pattern throughout codebase
5. **IDE friendly**: Better autocomplete and go-to-definition

## Exceptions

Standard library single-item imports that are commonly used alone may be acceptable:
```python
import sys
import os
import re
```

But prefer the absolute form when using multiple items from the module.
