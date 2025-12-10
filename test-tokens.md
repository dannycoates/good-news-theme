# Theme Token Test File

This file demonstrates all token types supported by the Good News theme. Open this file in VSCode to preview syntax highlighting.

---

## JavaScript

```javascript
// Single-line comment
/* Multi-line
   comment */

/**
 * JSDoc comment
 * @param {string} name - The name parameter
 * @returns {boolean} Returns true if valid
 */
function greetUser(name) {
  const greeting = "Hello";
  let message = `${greeting}, ${name}!`;
  var legacy = 'old style';

  console.log(message);
  return true;
}

// Constants and literals
const MAX_SIZE = 100;
const pi = 3.14159;
const hex = 0xFF;
const binary = 0b1010;
const isActive = true;
const nothing = null;
const missing = undefined;

// Regular expressions
const pattern = /[a-z]+\d*/gi;
const escaped = "line1\nline2\ttabbed";

// Arrow functions
const add = (a, b) => a + b;
const double = x => x * 2;

// Classes and inheritance
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  speak() {
    console.log(`${this.name} barks!`);
  }
}

// Object literals
const config = {
  host: "localhost",
  port: 3000,
  enabled: true,
  callback: function() {},
  arrow: () => {},
};

// Async/await
async function fetchData(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error("Failed to fetch");
  }
}

// Control flow
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  while (false) {
    break;
  }
}

// Built-ins
const arr = new Array(5);
const now = Date.now();
const random = Math.random();
const parsed = JSON.parse('{}');
const str = Object.keys({}).toString();
```

---

## TypeScript

```typescript
// Type annotations
interface User {
  id: number;
  name: string;
  email?: string;
  readonly createdAt: Date;
}

type Status = "pending" | "active" | "inactive";
type Callback<T> = (data: T) => void;

// Generics
function identity<T>(arg: T): T {
  return arg;
}

class Container<T> {
  private value: T;

  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

// Decorators
function logged(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${key}`);
    return original.apply(this, args);
  };
}

class Service {
  @logged
  process(data: string): boolean {
    return data.length > 0;
  }
}

// Enums
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

// Type guards
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// Utility types
type Partial<T> = { [P in keyof T]?: T[P] };
type Required<T> = { [P in keyof T]-?: T[P] };
```

---

## HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Page</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    body { margin: 0; }
  </style>
</head>
<body>
  <!-- This is a comment -->
  <header id="main-header" class="container">
    <h1 data-value="test">Welcome</h1>
    <nav aria-label="Main navigation">
      <a href="#home">Home</a>
      <a href="#about">About</a>
    </nav>
  </header>

  <main>
    <article>
      <p>Special characters: &amp; &lt; &gt; &quot; &copy;</p>
      <p>Unicode: &#x263A; &#9786;</p>
    </article>

    <form action="/submit" method="POST">
      <input type="text" name="username" required>
      <button type="submit" disabled>Submit</button>
    </form>
  </main>

  <script src="app.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      console.log('Ready');
    });
  </script>
</body>
</html>
```

---

## CSS

```css
/* CSS Variables and Root */
:root {
  --primary-color: #3498db;
  --secondary-color: rgb(52, 73, 94);
  --spacing: 1rem;
}

/* Element selectors */
body {
  margin: 0;
  padding: 0;
  font-family: "Helvetica Neue", Arial, sans-serif;
  background-color: var(--primary-color);
}

/* Class and ID selectors */
.container {
  max-width: 1200px;
  margin: 0 auto;
}

#header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}

/* Pseudo-classes and pseudo-elements */
a:hover,
a:focus {
  color: #e74c3c;
  text-decoration: underline;
}

.button::before {
  content: "";
  display: block;
}

/* Attribute selectors */
input[type="text"] {
  border: 1px solid #ccc;
}

[data-active="true"] {
  opacity: 1;
}

/* Media queries */
@media screen and (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
}

@media (prefers-color-scheme: dark) {
  body {
    background: #1a1a1a;
    color: #ffffff;
  }
}

/* Keyframes */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Import */
@import url("https://fonts.googleapis.com/css2?family=Inter");
```

---

## SCSS

```scss
// Variables
$primary: #3498db;
$secondary: #2ecc71;
$spacing: 8px;

// Mixins
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

@mixin responsive($breakpoint) {
  @media (max-width: $breakpoint) {
    @content;
  }
}

// Nesting
.card {
  padding: $spacing * 2;
  border-radius: 4px;

  &__header {
    font-size: 1.5rem;
    color: $primary;
  }

  &__body {
    padding: $spacing;
  }

  &:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  &.is-active {
    border-color: $secondary;
  }
}

// Interpolation
$property: margin;
$direction: top;

.element {
  #{$property}-#{$direction}: 10px;
}

// Functions
@function calculate-rem($size) {
  @return $size / 16px * 1rem;
}

// Extend
%button-base {
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;
}

.button-primary {
  @extend %button-base;
  background: $primary;
}

// Each loop
$colors: (primary: blue, secondary: green, danger: red);

@each $name, $color in $colors {
  .text-#{$name} {
    color: $color;
  }
}
```

---

## Markdown

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

This is a paragraph with **bold text**, *italic text*, and ***bold italic***.

This has `inline code` and ~~strikethrough~~.

> This is a blockquote
> with multiple lines

- Unordered list item 1
- Unordered list item 2
  - Nested item
  - Another nested item
- Item 3

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

[Link text](https://example.com "Link title")
[Reference link][ref]

[ref]: https://example.com "Reference"

![Alt text](image.png "Image title")

---

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

Footnote reference[^1]

[^1]: Footnote content

Task list:
- [x] Completed task
- [ ] Incomplete task
```

---

## Rust

```rust
//! Module documentation
//! This is a crate-level doc comment

use std::collections::HashMap;
use std::io::{self, Read, Write};

/// A user struct with lifetime parameter
#[derive(Debug, Clone, PartialEq)]
pub struct User<'a> {
    pub name: &'a str,
    pub age: u32,
    email: Option<String>,
}

impl<'a> User<'a> {
    /// Creates a new user
    pub fn new(name: &'a str, age: u32) -> Self {
        Self {
            name,
            age,
            email: None,
        }
    }

    pub fn with_email(mut self, email: String) -> Self {
        self.email = Some(email);
        self
    }

    fn is_adult(&self) -> bool {
        self.age >= 18
    }
}

// Traits
pub trait Greeting {
    fn greet(&self) -> String;

    fn greet_formal(&self) -> String {
        format!("Good day, {}", self.greet())
    }
}

impl<'a> Greeting for User<'a> {
    fn greet(&self) -> String {
        format!("Hello, {}!", self.name)
    }
}

// Enums with variants
#[derive(Debug)]
pub enum Status {
    Active,
    Inactive,
    Pending { reason: String },
    Error(String),
}

// Constants
const MAX_USERS: usize = 100;
static GLOBAL_COUNT: std::sync::atomic::AtomicUsize =
    std::sync::atomic::AtomicUsize::new(0);

// Generic function with trait bounds
fn process<T: std::fmt::Debug + Clone>(items: &[T]) -> Vec<T> {
    items.iter().cloned().collect()
}

// Async function
async fn fetch_data(url: &str) -> Result<String, Box<dyn std::error::Error>> {
    // Simulated async operation
    Ok(String::from("data"))
}

fn main() {
    // Variables and mutability
    let x = 5;
    let mut y = 10;
    y += x;

    // Pattern matching
    let status = Status::Active;
    match status {
        Status::Active => println!("Active"),
        Status::Inactive => println!("Inactive"),
        Status::Pending { reason } => println!("Pending: {}", reason),
        Status::Error(e) => eprintln!("Error: {}", e),
    }

    // Closures
    let add = |a: i32, b: i32| -> i32 { a + b };
    let numbers: Vec<i32> = (0..10).filter(|&n| n % 2 == 0).collect();

    // References and borrowing
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    println!("{} and {}", r1, r2);

    // Macros
    println!("Hello, world!");
    let v = vec![1, 2, 3];
    dbg!(&v);

    // Error handling
    let result: Result<i32, &str> = Ok(42);
    if let Ok(value) = result {
        println!("Value: {}", value);
    }

    // Unsafe block
    unsafe {
        let ptr = &x as *const i32;
        println!("Address: {:?}", ptr);
    }
}

// Macro definition
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
    ($name:expr) => {
        println!("Hello, {}!", $name);
    };
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_user_creation() {
        let user = User::new("Alice", 30);
        assert_eq!(user.name, "Alice");
        assert!(user.is_adult());
    }
}
```

---

## JSON

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "private": true,
  "description": "A sample project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "build": "webpack --mode production"
  },
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "~4.17.21"
  },
  "devDependencies": {
    "jest": "^29.0.0"
  },
  "config": {
    "port": 3000,
    "debug": true,
    "maxRetries": 5,
    "timeout": null,
    "features": ["auth", "api", "websocket"],
    "database": {
      "host": "localhost",
      "port": 5432,
      "name": "mydb"
    }
  },
  "keywords": ["node", "express", "api"],
  "author": "Developer <dev@example.com>",
  "license": "MIT"
}
```

---

## YAML

```yaml
# Application configuration
name: my-application
version: 1.0.0

# Server settings
server:
  host: localhost
  port: 8080
  ssl:
    enabled: true
    certificate: /path/to/cert.pem
    key: /path/to/key.pem

# Database configuration
database:
  driver: postgresql
  host: localhost
  port: 5432
  name: mydb
  credentials:
    username: admin
    password: secret

# Feature flags
features:
  - authentication
  - authorization
  - caching
  - logging

# Environment-specific overrides
environments:
  development:
    debug: true
    log_level: debug
  production:
    debug: false
    log_level: warn

# Complex nested structure
services:
  api:
    replicas: 3
    memory: 512Mi
    cpu: 250m
    env:
      - name: NODE_ENV
        value: production
      - name: API_KEY
        valueFrom:
          secretKeyRef:
            name: api-secrets
            key: api-key

# Multi-line strings
description: |
  This is a multi-line
  description that preserves
  line breaks.

inline_description: >
  This is a folded multi-line
  string that will be joined
  into a single line.

# Anchors and aliases
defaults: &defaults
  timeout: 30
  retries: 3

service_a:
  <<: *defaults
  name: Service A

service_b:
  <<: *defaults
  name: Service B
  timeout: 60  # Override default
```

---

## Diff

```diff
diff --git a/src/config.js b/src/config.js
index 1234567..abcdefg 100644
--- a/src/config.js
+++ b/src/config.js
@@ -1,10 +1,15 @@
 const config = {
   name: 'my-app',
-  version: '1.0.0',
+  version: '2.0.0',
   settings: {
-    debug: true,
-    timeout: 5000,
+    debug: false,
+    timeout: 10000,
+    maxRetries: 3,
   },
+  features: {
+    newFeature: true,
+    legacyMode: false,
+  },
 };

 module.exports = config;
```

---

## XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE config SYSTEM "config.dtd">
<?xml-stylesheet type="text/xsl" href="transform.xsl"?>

<!-- Root configuration element -->
<config xmlns="http://example.com/config"
        xmlns:custom="http://example.com/custom"
        version="1.0">

  <metadata>
    <name>Application Config</name>
    <author>Developer</author>
    <created>2024-01-01</created>
  </metadata>

  <settings environment="production">
    <setting key="debug" type="boolean">false</setting>
    <setting key="timeout" type="integer">30000</setting>
    <setting key="apiUrl" type="string">
      <![CDATA[https://api.example.com/v1?param=value&other=test]]>
    </setting>
  </settings>

  <custom:extensions>
    <custom:plugin name="auth" enabled="true">
      <custom:config>
        <custom:option name="provider">oauth2</custom:option>
      </custom:config>
    </custom:plugin>
  </custom:extensions>

  <items>
    <item id="1" active="true">First item</item>
    <item id="2" active="false">Second item</item>
    <item id="3" active="true">
      Third item with <emphasis>nested</emphasis> content
    </item>
  </items>

  <!-- Special characters -->
  <special>
    <entity>&amp; &lt; &gt; &quot; &apos;</entity>
    <numeric>&#65; &#x41;</numeric>
  </special>

</config>
```

---

## Shell / Bash

```bash
#!/bin/bash

# Script configuration
set -euo pipefail
IFS=$'\n\t'

# Variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly CONFIG_FILE="${SCRIPT_DIR}/config.sh"
readonly LOG_FILE="/var/log/app.log"

# Environment variables
export NODE_ENV="production"
export DEBUG="${DEBUG:-false}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Functions
log() {
    local level="$1"
    shift
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [${level}] $*" >> "${LOG_FILE}"
}

error() {
    echo -e "${RED}Error: $*${NC}" >&2
    log "ERROR" "$*"
    exit 1
}

success() {
    echo -e "${GREEN}$*${NC}"
    log "INFO" "$*"
}

# Check dependencies
check_deps() {
    local deps=("curl" "jq" "docker")
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            error "Required dependency '$dep' not found"
        fi
    done
}

# Main logic
main() {
    check_deps

    # Command line arguments
    while getopts ":hv" opt; do
        case ${opt} in
            h)
                echo "Usage: $0 [-h] [-v]"
                exit 0
                ;;
            v)
                echo "Version 1.0.0"
                exit 0
                ;;
            \?)
                error "Invalid option: -${OPTARG}"
                ;;
        esac
    done

    # Conditionals
    if [[ -f "${CONFIG_FILE}" ]]; then
        source "${CONFIG_FILE}"
    else
        error "Config file not found: ${CONFIG_FILE}"
    fi

    # Loops
    for file in "${SCRIPT_DIR}"/*.sh; do
        echo "Found script: ${file}"
    done

    # Process substitution
    while IFS= read -r line; do
        echo "Processing: ${line}"
    done < <(cat "${CONFIG_FILE}")

    # Command substitution
    local current_date
    current_date=$(date +%Y-%m-%d)

    # Arithmetic
    local count=0
    ((count++))
    result=$((5 + 3 * 2))

    # Arrays
    local -a items=("one" "two" "three")
    echo "First item: ${items[0]}"
    echo "All items: ${items[*]}"
    echo "Count: ${#items[@]}"

    # Associative arrays
    declare -A config
    config[host]="localhost"
    config[port]="8080"

    # Here document
    cat << 'EOF'
This is a here document
with multiple lines
EOF

    success "Script completed successfully"
}

# Run main function
main "$@"
```

---

## Python

```python
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
```

---

## .env (dotenv)

```dotenv
# Environment configuration
NODE_ENV=production
DEBUG=false

# Server settings
HOST=localhost
PORT=3000

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
DB_POOL_SIZE=10

# API Keys
API_KEY=sk_live_abc123xyz
SECRET_KEY="my-secret-key-with-special-chars!@#"

# Feature flags
ENABLE_CACHE=true
MAX_UPLOAD_SIZE=10485760
```

---

## Go

```go
// Package main demonstrates Go syntax highlighting
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"sync"
	"time"
)

// Constants
const (
	MaxRetries    = 3
	DefaultTimeout = 30 * time.Second
)

// Custom type
type Status int

const (
	StatusPending Status = iota
	StatusActive
	StatusInactive
)

// Interface definition
type Repository interface {
	Get(ctx context.Context, id string) (*User, error)
	Save(ctx context.Context, user *User) error
}

// Struct with tags
type User struct {
	ID        string    `json:"id" db:"id"`
	Name      string    `json:"name" db:"name"`
	Email     string    `json:"email,omitempty" db:"email"`
	CreatedAt time.Time `json:"created_at" db:"created_at"`
	metadata  map[string]interface{}
}

// Constructor function
func NewUser(name, email string) *User {
	return &User{
		ID:        generateID(),
		Name:      name,
		Email:     email,
		CreatedAt: time.Now(),
		metadata:  make(map[string]interface{}),
	}
}

// Method with pointer receiver
func (u *User) SetMetadata(key string, value interface{}) {
	u.metadata[key] = value
}

// Method with value receiver
func (u User) String() string {
	return fmt.Sprintf("User{ID: %s, Name: %s}", u.ID, u.Name)
}

// Generic function (Go 1.18+)
func Filter[T any](items []T, predicate func(T) bool) []T {
	result := make([]T, 0)
	for _, item := range items {
		if predicate(item) {
			result = append(result, item)
		}
	}
	return result
}

// Goroutine and channels
func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(100 * time.Millisecond)
		results <- job * 2
	}
}

// Error handling
func fetchData(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("failed to fetch: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status: %d", resp.StatusCode)
	}

	return io.ReadAll(resp.Body)
}

func main() {
	// Variables
	var name string = "Go"
	count := 42
	pi := 3.14159
	isEnabled := true
	var nothing *string = nil

	// Slices and maps
	numbers := []int{1, 2, 3, 4, 5}
	config := map[string]interface{}{
		"host":    "localhost",
		"port":    8080,
		"enabled": true,
	}

	// Control flow
	for i, n := range numbers {
		if n%2 == 0 {
			fmt.Printf("Index %d: %d is even\n", i, n)
		} else {
			fmt.Printf("Index %d: %d is odd\n", i, n)
		}
	}

	// Switch statement
	switch status := StatusActive; status {
	case StatusPending:
		fmt.Println("Pending")
	case StatusActive:
		fmt.Println("Active")
	default:
		fmt.Println("Unknown")
	}

	// Type switch
	var value interface{} = "hello"
	switch v := value.(type) {
	case string:
		fmt.Printf("String: %s\n", v)
	case int:
		fmt.Printf("Int: %d\n", v)
	default:
		fmt.Printf("Unknown type: %T\n", v)
	}

	// Defer
	defer fmt.Println("Cleanup")

	// Goroutines and channels
	jobs := make(chan int, 100)
	results := make(chan int, 100)
	var wg sync.WaitGroup

	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go worker(w, jobs, results, &wg)
	}

	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	go func() {
		wg.Wait()
		close(results)
	}()

	for result := range results {
		fmt.Println("Result:", result)
	}

	// Anonymous function
	add := func(a, b int) int {
		return a + b
	}
	fmt.Println(add(1, 2))

	_ = name
	_ = count
	_ = pi
	_ = isEnabled
	_ = nothing
	_ = config
}

func generateID() string {
	return "generated-id"
}
```

---

## TOML

```toml
# This is a TOML configuration file
# Top-level comment

title = "TOML Example"
description = 'Single quoted string'

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00  # First class dates

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"
priority = 1

[servers.beta]
ip = "10.0.0.2"
role = "backend"
priority = 2

# Array of tables
[[products]]
name = "Hammer"
sku = 738594937
price = 9.99
in_stock = true

[[products]]
name = "Nail"
sku = 284758393
price = 0.05
quantity = 500

[[products.reviews]]
author = "Alice"
rating = 5
comment = """
Multi-line string
with line breaks preserved
"""

[[products.reviews]]
author = "Bob"
rating = 4
comment = '''\
  Literal string with \
  no escape sequences
'''

# Inline tables
point = { x = 1, y = 2 }
animal = { type.name = "pug" }

# Different number formats
int1 = +99
int2 = -17
int3 = 1_000_000
hex1 = 0xDEADBEEF
oct1 = 0o755
bin1 = 0b11010110

# Floats
float1 = +1.0
float2 = 3.1415
float3 = -0.01
float4 = 5e+22
float5 = 1e06
float6 = -2E-2
float7 = 6.626e-34
special1 = inf
special2 = nan

# Dates and times
date1 = 2024-01-15
time1 = 07:32:00
datetime1 = 2024-01-15T07:32:00Z
datetime2 = 2024-01-15T07:32:00-07:00
datetime3 = 2024-01-15 07:32:00

[environment]
PATH = "/usr/local/bin:/usr/bin"
HOME = "/home/user"
DEBUG = false
```
