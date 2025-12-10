#!/usr/bin/env python3
"""
Module docstring.
This module demonstrates Python syntax highlighting.
"""

from __future__ import annotations
import os
import sys
from typing import Optional, List, Dict, TypeVar, Generic
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from contextlib import contextmanager
import asyncio

# Type variable
T = TypeVar('T')

# Constants
MAX_RETRIES: int = 3
DEFAULT_TIMEOUT: float = 30.0
API_URL: str = "https://api.example.com"

# Decorator
def logged(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

def retry(max_attempts: int = 3):
    """Parameterized decorator for retry logic."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Retry {attempt + 1}/{max_attempts}")
        return wrapper
    return decorator

# Dataclass
@dataclass
class User:
    """User data class."""
    name: str
    email: str
    age: int = 0
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

    @property
    def is_adult(self) -> bool:
        return self.age >= 18

# Abstract base class
class Repository(ABC, Generic[T]):
    """Abstract repository pattern."""

    @abstractmethod
    def get(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def save(self, item: T) -> None:
        pass

# Implementation
class UserRepository(Repository[User]):
    def __init__(self):
        self._storage: Dict[int, User] = {}
        self._counter: int = 0

    def get(self, id: int) -> Optional[User]:
        return self._storage.get(id)

    def save(self, item: User) -> None:
        self._counter += 1
        self._storage[self._counter] = item

# Context manager
@contextmanager
def timer(name: str):
    """Context manager for timing code blocks."""
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.2f}s")

# Async functions
async def fetch_data(url: str) -> dict:
    """Async function to fetch data."""
    await asyncio.sleep(0.1)  # Simulated delay
    return {"url": url, "status": "ok"}

async def process_urls(urls: List[str]) -> List[dict]:
    """Process multiple URLs concurrently."""
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# Main function
@logged
@retry(max_attempts=3)
def main():
    # String types
    single = 'single quotes'
    double = "double quotes"
    triple = """Triple quoted
    multiline string"""
    raw = r"raw string with \n no escapes"
    formatted = f"User count: {len([1, 2, 3])}"

    # Numbers
    integer = 42
    float_num = 3.14159
    complex_num = 1 + 2j
    hex_num = 0xFF
    binary = 0b1010
    octal = 0o755
    scientific = 1.5e-10

    # Collections
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3)
    my_set = {1, 2, 3}
    my_dict = {"key": "value", "count": 42}

    # Comprehensions
    squares = [x**2 for x in range(10)]
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    dict_comp = {k: v for k, v in enumerate(['a', 'b', 'c'])}
    set_comp = {x % 3 for x in range(10)}
    gen_exp = (x**2 for x in range(10))

    # Control flow
    for i, item in enumerate(my_list):
        if item > 3:
            continue
        elif item < 0:
            break
        else:
            print(item)

    # Exception handling
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except (ValueError, TypeError):
        print("Value or type error")
    else:
        print("No exception")
    finally:
        print("Cleanup")

    # With statement
    with timer("file operation"):
        with open("/dev/null", "w") as f:
            f.write("test")

    # Lambda and functional
    double = lambda x: x * 2
    numbers = list(map(lambda x: x * 2, range(5)))
    filtered = list(filter(lambda x: x > 0, [-1, 0, 1, 2]))

    # Pattern matching (Python 3.10+)
    status = {"code": 200, "message": "OK"}
    match status:
        case {"code": 200}:
            print("Success")
        case {"code": 404}:
            print("Not found")
        case _:
            print("Unknown")

    # Walrus operator
    if (n := len(my_list)) > 3:
        print(f"List has {n} items")

    # Boolean and None
    flag = True
    empty = None

    # Assertions
    assert flag is True, "Flag must be True"

    return 0

if __name__ == "__main__":
    sys.exit(main())
