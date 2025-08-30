# Type Safety in Python

This project demonstrates different approaches to achieve type safety in Python using three different methods:

## 1. TypedDict

```python
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: int
```

### Key Points:
- **Static Type Checking Only**: Works with mypy/pyright
- **No Runtime Validation**: Type hints only
- **Dictionary-like**: Must use dictionary access syntax
- **No Methods**: Cannot add methods to TypedDict

## 2. Dataclass

```python
from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    year: int
    rating: int
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"
```

### Key Points:
- **Static Type Checking**: Works with mypy/pyright
- **No Built-in Validation**: But can be added manually
- **Class-based**: Can include methods
- **Performance**: Very fast, compiles to regular Python

## 3. Pydantic

```python
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str
    year: int = Field(..., gt=1900, lt=2100)
    rating: float = Field(..., ge=0, le=10)
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating:.1f}/10"
```

### Key Points:
- **Runtime Validation**: Validates data on creation and update
- **Type Conversion**: Automatically converts types when possible
- **Rich Validation**: Supports complex validation rules
- **Performance**: Slightly slower due to validation overhead

## Comparison

| Feature          | TypedDict | Dataclass | Pydantic |
|------------------|-----------|-----------|----------|
| Type Checking    | Static    | Static    | Both     |
| Runtime Check    | ❌        | ❌        | ✅       |
| Validation       | ❌        | ❌        | ✅       |
| Performance      | ⚡ Fast   | ⚡ Fast   | 🐢 Slower|
| Serialization    | Manual    | Manual    | Built-in |
| Methods Support  | ❌        | ✅        | ✅       |
| Schema Generation| ❌        | ❌        | ✅       |

## Running the Examples

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run type checking:
   ```bash
   mypy typesafe_*.py
   ```

3. Run the examples:
   ```bash
   python -m typesafe_typeddict
   python -m typesafe_dataclass
   python -m typesafe_pydantic
   ```
