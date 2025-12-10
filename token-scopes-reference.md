# Syntax Highlighting Token Scopes Reference

A comprehensive reference of known scopes and tokens for syntax highlighting across TextMate, VSCode Semantic Tokens, and Tree-sitter (Zed/Neovim/Helix).

---

## Table of Contents

1. [TextMate Scopes](#textmate-scopes)
2. [VSCode Semantic Tokens](#vscode-semantic-tokens)
3. [Tree-sitter Captures](#tree-sitter-captures)
4. [Sources](#sources)

---

## TextMate Scopes

TextMate uses a hierarchical dot-notation scope naming system where scopes become increasingly specific from left to right (e.g., `string.quoted.double.c`).

### Top-Level Language Scopes

- `source.*` - Programming languages (e.g., `source.python`, `source.javascript`)
- `text.*` - Prose/markup (e.g., `text.html.markdown`, `text.plain`)

### comment

```
comment
comment.line
comment.line.double-slash          // style
comment.line.double-dash           -- style
comment.line.number-sign           # style
comment.line.percentage            % style
comment.line.character             other types
comment.block                      /* */ or <!-- -->
comment.block.documentation        doc comments
```

### constant

```
constant
constant.numeric
constant.character
constant.character.escape          \n, \t, etc.
constant.language                  true, false, nil, YES, NO
constant.other                     CSS colors, etc.
```

### entity

```
entity.name.function
entity.name.type
entity.name.type.class
entity.name.type.enum
entity.name.type.interface
entity.name.type.struct
entity.name.tag                    markup tag names
entity.name.section                section/heading names
entity.name.namespace
entity.other.inherited-class       superclass/baseclass
entity.other.attribute-name        attribute names in tags
```

### invalid

```
invalid.illegal                    syntax errors
invalid.deprecated                 deprecated features
```

### keyword

```
keyword
keyword.control                    if, while, return, continue
keyword.operator                   and, or, not (textual operators)
keyword.other
```

### markup

```
markup.underline
markup.underline.link              hyperlinks
markup.bold
markup.heading
markup.heading.1
markup.heading.2
markup.heading.3
markup.italic
markup.list.numbered
markup.list.unnumbered
markup.quote
markup.raw                         verbatim/code blocks
markup.other
```

### meta

Used to scope larger document sections (function declarations, class bodies). Provides context but typically not directly styled.

```
meta.function
meta.class
meta.block
meta.brace
meta.group
```

### punctuation

```
punctuation.definition
punctuation.delimiter              ; . ,
punctuation.bracket                () {} []
punctuation.special
punctuation.separator
punctuation.terminator
punctuation.accessor
```

### storage

```
storage.type                       class, function, int, var, struct
storage.modifier                   static, final, abstract, public, private
```

### string

```
string
string.quoted
string.quoted.single               'foo'
string.quoted.double               "foo"
string.quoted.triple               """Python"""
string.quoted.other
string.unquoted                    here-docs
string.interpolated                strings with embedded expressions
string.regexp                      /(\w+)/
string.other
```

### support

Framework/library-provided elements:

```
support.function                   NSLog, printf
support.class
support.type
support.constant
support.variable                   NSApp
support.other
```

### variable

```
variable
variable.parameter                 function parameters
variable.language                  this, super, self
variable.other
variable.other.readwrite
variable.other.constant
variable.other.property
```

---

## VSCode Semantic Tokens

Semantic tokens provide language-aware highlighting on top of TextMate grammar-based syntax highlighting. Tokens consist of **types** and **modifiers**.

### Token Types (23 standard)

#### Types & Namespaces

```
namespace                          namespaces, modules, packages
type                               general types
class                              class types
enum                               enumeration types
interface                          interface types
struct                             struct types
typeParameter                      generic type parameters
```

#### Functions & Methods

```
function                           function declarations
method                             class methods
macro                              macro definitions
```

#### Variables & Properties

```
variable                           local/global variables
parameter                          function/method parameters
property                           member properties/fields
enumMember                         enumeration members
event                              event properties
decorator                          decorators/annotations (@Component)
```

#### Other

```
label                              labels (for goto)
comment                            comments
string                             string literals
keyword                            language keywords
number                             numeric literals
regexp                             regular expressions
operator                           operators
```

### Token Modifiers (13 standard)

```
declaration                        symbol declarations
definition                         symbol definitions (header files)
readonly                           readonly/constant members
static                             static class members
deprecated                         deprecated symbols
abstract                           abstract types/methods
async                              async functions
modification                       variable assignment locations
documentation                      documentation contexts
defaultLibrary                     standard library symbols
```

### Semantic Token to TextMate Scope Mapping

| Semantic Token       | TextMate Scope(s)                           |
|---------------------|---------------------------------------------|
| `namespace`         | `entity.name.namespace`                     |
| `type`              | `entity.name.type`, `support.type`          |
| `class`             | `entity.name.type.class`                    |
| `enum`              | `entity.name.type.enum`                     |
| `interface`         | `entity.name.type.interface`                |
| `struct`            | `storage.type.struct`                       |
| `function`          | `entity.name.function`, `support.function`  |
| `method`            | `entity.name.function.member`               |
| `macro`             | `entity.name.other.preprocessor.macro`      |
| `variable`          | `variable.other.readwrite`                  |
| `variable.readonly` | `variable.other.constant`                   |
| `parameter`         | `variable.parameter`                        |
| `property`          | `variable.other.property`                   |
| `property.readonly` | `variable.other.constant.property`          |
| `enumMember`        | `variable.other.enummember`                 |
| `keyword`           | `keyword.control`                           |

---

## Tree-sitter Captures

Tree-sitter uses capture names (prefixed with `@`) in highlight queries (`highlights.scm` files). There's an ongoing effort to standardize these across editors.

### Neovim/nvim-treesitter Standard Captures

This is the most comprehensive standardized list, used as reference by Zed and Helix.

#### Identifiers

```
@variable                          variables
@variable.builtin                  built-in variables (self, this)
@variable.parameter                function parameters
@variable.parameter.builtin        built-in parameters
@variable.member                   member variables/fields
@constant                          constants
@constant.builtin                  built-in constants
@constant.macro                    macro-defined constants
@module                            modules/namespaces
@module.builtin                    built-in modules
@label                             labels (for goto)
```

#### Literals

```
@string                            strings
@string.documentation              documentation strings
@string.regexp                     regular expressions
@string.escape                     escape sequences
@string.special                    special strings
@string.special.symbol             symbols (Ruby, Clojure)
@string.special.url                URLs
@string.special.path               file paths
@character                         character literals
@character.special                 special characters
@boolean                           boolean values
@number                            numbers
@number.float                      floating-point numbers
```

#### Types

```
@type                              type names
@type.builtin                      built-in types
@type.definition                   type definitions
@attribute                         attributes/annotations
@attribute.builtin                 built-in attributes
@property                          properties
```

#### Functions

```
@function                          function definitions
@function.builtin                  built-in functions
@function.call                     function calls
@function.macro                    macro functions
@function.method                   method definitions
@function.method.call              method calls
@constructor                       constructors
@operator                          operators
```

#### Keywords

```
@keyword                           general keywords
@keyword.coroutine                 async, await
@keyword.function                  function, def, fn
@keyword.operator                  and, or, not
@keyword.import                    import keywords
@keyword.type                      typedef, class
@keyword.modifier                  static, const
@keyword.repeat                    for, while
@keyword.return                    return keywords
@keyword.debug                     debugging keywords
@keyword.exception                 try, catch, throw
@keyword.conditional               if, else
@keyword.conditional.ternary       ternary operators
@keyword.directive                 preprocessor directives
@keyword.directive.define          define directives
```

#### Punctuation

```
@punctuation.delimiter             ; . ,
@punctuation.bracket               () {} []
@punctuation.special               special punctuation
```

#### Comments

```
@comment                           comments
@comment.documentation             documentation comments
@comment.error                     error annotations (ERROR, FIXME)
@comment.warning                   warning annotations (WARNING, HACK)
@comment.todo                      TODO annotations
@comment.note                      NOTE annotations
```

#### Markup (Markdown, etc.)

```
@markup.strong                     bold text
@markup.italic                     italic text
@markup.strikethrough              strikethrough
@markup.underline                  underlined text
@markup.heading                    headings
@markup.heading.1                  h1
@markup.heading.2                  h2
@markup.heading.3                  h3
@markup.quote                      quotes
@markup.math                       math expressions
@markup.link                       links
@markup.link.label                 link labels
@markup.link.url                   URLs
@markup.raw                        raw/code blocks
@markup.raw.block                  code blocks
@markup.list                       lists
@markup.list.checked               checked items
@markup.list.unchecked             unchecked items
```

#### Special Captures

```
@none                              disable highlighting
@conceal                           conceal/hide text
@spell                             enable spell checking
@nospell                           disable spell checking
```

### Zed Editor Captures

Zed-specific captures (converging toward Neovim standard):

```
@attribute
@boolean
@comment
@comment.doc
@constant
@constructor
@embedded
@emphasis
@emphasis.strong
@enum
@function
@hint
@keyword
@label
@link_text
@link_uri
@number
@operator
@predictive
@preproc
@primary
@property
@punctuation
@punctuation.bracket
@punctuation.delimiter
@punctuation.list_marker
@punctuation.special
@string
@string.escape
@string.regex
@string.special
@string.special.symbol
@tag
@tag.doctype
@text.literal
@title
@type
@variable
@variable.special
@variant
```

### Helix Editor Scopes

Helix uses a similar system with longest-prefix matching:

```
attribute
type
type.builtin
type.parameter
type.enum
type.enum.variant
constructor
constant
constant.builtin
constant.builtin.boolean
constant.character
constant.character.escape
constant.numeric
constant.numeric.integer
constant.numeric.float
string
string.regexp
string.special
string.special.path
string.special.url
string.special.symbol
comment
comment.line
comment.block
comment.block.documentation
variable
variable.builtin
variable.parameter
variable.other.member
function
function.builtin
function.method
function.macro
function.special
keyword
keyword.control
keyword.control.conditional
keyword.control.repeat
keyword.control.import
keyword.control.return
keyword.control.exception
keyword.operator
keyword.directive
keyword.function
keyword.storage
keyword.storage.type
keyword.storage.modifier
operator
punctuation
punctuation.delimiter
punctuation.bracket
punctuation.special
label
namespace
markup.heading
markup.heading.marker
markup.heading.1
markup.heading.2
markup.heading.3
markup.list
markup.list.numbered
markup.list.unnumbered
markup.bold
markup.italic
markup.strikethrough
markup.link
markup.link.url
markup.link.text
markup.quote
markup.raw
markup.raw.inline
markup.raw.block
diff.plus
diff.minus
diff.delta
```

---

## Sources

### TextMate

- [Language Grammars - TextMate 1.x Manual](https://macromates.com/manual/en/language_grammars)
- [Scope Selectors - TextMate 1.x Manual](https://macromates.com/manual/en/scope_selectors)
- [Introduction to Scopes (TextMate Blog)](https://macromates.com/blog/2005/introduction-to-scopes/)
- [Sublime Text Scope Naming](http://www.sublimetext.com/docs/scope_naming.html)

### VSCode Semantic Tokens

- [Semantic Highlight Guide - VSCode Extension API](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)
- [Semantic Highlighting Overview (GitHub Wiki)](https://github.com/microsoft/vscode/wiki/Semantic-Highlighting-Overview)
- [Syntax Highlight Guide - VSCode Extension API](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide)

### Tree-sitter / Editors

- [Zed Language Extensions Documentation](https://zed.dev/docs/extensions/languages)
- [Neovim Treesitter Documentation](https://neovim.io/doc/user/treesitter.html)
- [nvim-treesitter CONTRIBUTING.md](https://github.com/nvim-treesitter/nvim-treesitter/blob/master/CONTRIBUTING.md)
- [Helix Themes Documentation](https://docs.helix-editor.com/themes.html)
- [Tree-sitter Syntax Highlighting](https://tree-sitter.github.io/tree-sitter/3-syntax-highlighting.html)
