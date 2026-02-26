# Syntax

This page covers the foundational syntax rules of AISL.

## Statements and semicolons

Most statements in AISL end with a semicolon (`;`). The exceptions are
declarations and for loops, which use curly braces to delimit their bodies.

```
let x = 42;                    // semicolon required
append results with value;     // semicolon required
return x + 1;                  // semicolon required
my_function(a, b);             // semicolon required
```

Block statements do not require a trailing semicolon:

```
declare m as model { ... }

for 1..10 { ... }

declare f as function(x) { ... }
```

## Comments

AISL supports single-line and multi-line comments.

```
// This is a single-line comment

/* This is a
   multi-line comment */

let x = 42; // inline comment
```

Comments are ignored by the interpreter and can appear anywhere whitespace is
allowed.

## Identifiers

Identifiers name variables, functions, models, datasets, and other declarations.
An identifier must start with a letter or underscore and can contain letters,
digits, and underscores.

```
my_variable
_private
model1
ground_truth
```

## Whitespace

Whitespace (spaces, tabs, and newlines) is not significant in AISL. It is used
only to separate tokens. You can format your code in any style.

```
// These are equivalent
let x = 1 + 2;

let x=1+2;

let x =
    1 + 2;
```

## Reserved words

The following words have special meaning in AISL and cannot be used as
identifiers:

| Keyword | Purpose |
|---------|---------|
| `declare` | Begin a declaration |
| `as` | Specify declaration type |
| `model` | Model declaration type / dataset option |
| `dataset` | Dataset declaration type |
| `performance` | Performance declaration type |
| `file` | File declaration type |
| `function` | Function declaration type |
| `let` | Variable assignment |
| `for` | Range-based loop |
| `append` | Append to a list |
| `with` | Used in append statements |
| `return` | Return from a function |
| `metric` | Metric invocation in performance blocks |
| `key` | Dataset/file field selector option |
| `name` | File name option |
| `type` | File type option |
| `endpoint` | Model endpoint option |
| `model_name` | Model name option |
| `temperature` | Model temperature option |
| `max_tokens` | Model max tokens option |
| `top_p` | Model top-p option |
| `frequency_penalty` | Model frequency penalty option |
| `presence_penalty` | Model presence penalty option |
| `timeout` | Model timeout option |
| `response_format` | Model response format option |
| `response_schema` | Model response schema option |
