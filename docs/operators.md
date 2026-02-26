# Operators

AISL provides arithmetic, comparison, and logical operators for building
expressions.

## Arithmetic operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `3 + 2` evaluates to `5` |
| `-` | Subtraction | `3 - 2` evaluates to `1` |
| `*` | Multiplication | `3 * 2` evaluates to `6` |
| `/` | Division | `6 / 2` evaluates to `3` |

Arithmetic operators work on numbers and lists. When applied to a list and a
scalar, the operation is broadcast element-wise:

```
let scores = [80, 90, 70];
let normalized = scores / 100;   // [0.8, 0.9, 0.7]
```

## Comparison operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 0` |
| `<` | Less than | `x < 10` |
| `>` | Greater than | `x > 0` |
| `<=` | Less than or equal | `x <= 100` |
| `>=` | Greater than or equal | `x >= 0.5` |

Comparison operators return boolean-like values. They can be used in ternary
expressions and metric conditions. Like arithmetic operators, comparisons
broadcast over lists:

```
let results = [0.8, 0.6, 0.95];
let passing = results >= 0.7;    // [true, false, true]
```

## Logical operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&&` | Logical AND | `a > 0 && b > 0` |
| `\|\|` | Logical OR | `a == 0 \|\| b == 0` |
| `!` | Logical NOT | `!done` |

## Ternary operator

The ternary operator provides conditional expressions using `?` and `:`. It is
primarily used in metric conditions within performance blocks.

```
condition ? "value_if_true" : "value_if_false"
```

For example, inside a performance declaration:

```
metric[accuracy](y_true, y_pred) > 0.9 ? "Pass" : "Fail"
```

The condition is evaluated first. If truthy, the expression before the colon is
returned; otherwise, the expression after the colon is returned.

## Operator precedence

Operators are evaluated left-to-right with the following precedence, from lowest
to highest:

1. Ternary (`? :`)
2. Logical OR (`||`)
3. Logical AND (`&&`)
4. Comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`)
5. Addition and subtraction (`+`, `-`)
6. Multiplication and division (`*`, `/`)

Use parentheses to override the default precedence:

```
let x = (a + b) * c;
let y = a + (b * c);
```

## Grouping with parentheses

Parentheses group sub-expressions and override operator precedence:

```
let result = (score1 + score2) / 2;
```
