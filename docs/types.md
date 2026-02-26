# Data Types

AISL has several built-in data types for representing values in your programs.

## Numbers

Numbers can be integers or floating-point values.

```
42
3.14
0
100
0.001
```

Numbers are used in arithmetic expressions, model configuration, loop ranges, and
as arguments to functions.

## Strings

Strings are sequences of characters enclosed in double quotes.

```
"hello world"
"model_name"
""
```

Strings support escape sequences:

| Escape | Character |
|--------|-----------|
| `\\` | Backslash |
| `\"` | Double quote |
| `\n` | Newline |
| `\t` | Tab |

## Lists

Lists are ordered collections of values enclosed in square brackets, separated by
commas. Lists can contain values of any type.

```
[1, 2, 3]
["yes", "no", "yes"]
[1.0, 0.8, 0.95]
[]
```

Lists are commonly used for storing collections of results, predictions, or
responses. Many built-in functions accept lists as arguments.

Lists support element-wise operations with scalars. When you apply an arithmetic
or comparison operator between a list and a scalar, the operation is applied to
each element:

```
let scores = [0.8, 0.9, 0.7];
let adjusted = scores + 0.1;    // [0.9, 1.0, 0.8]
let passing = scores > 0.75;    // [true, true, false]
```

## Records

Records are key-value collections enclosed in curly braces. Keys must be strings.

```
{"name": "test_run", "score": 0.95}
{"question": "Is AI safe?", "answer": "yes", "confidence": 0.8}
```

Records are used for structured data such as LLM responses and function return
values. You can access record fields using the `get` and `get_all` built-in
functions.

## Datasets

Datasets are a special type created through `declare ... as dataset` statements.
A dataset loads data from a JSON file and extracts a specific field. Internally,
dataset values are stored as arrays.

```
declare predictions as dataset { data_file, key = y_pred }
```

See [Dataset declarations](declarations/datasets.md) for details.

## Type coercion

AISL performs automatic type coercion in certain contexts:

- **Arithmetic with lists**: A scalar value is broadcast across all elements of a
  list (e.g., `[1, 2, 3] + 1` produces `[2, 3, 4]`)
- **Comparisons**: Values are compared using safe type-aware comparison, meaning
  mixed types are handled without errors
- **Function arguments**: Built-in functions generally expect specific types and
  will raise errors if given incompatible values
