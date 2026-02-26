# Functions

AISL supports user-defined functions for organizing reusable logic.

## Defining functions

Functions are declared using the `declare ... as function` syntax:

```
declare FUNCTION_NAME as function(PARAM1, PARAM2, ...) {
    // function body
}
```

Parameters are positional identifiers separated by commas. The function body is a
block of one or more statements.

```
declare add as function(a, b) {
    return a + b;
}

declare evaluate_model as function(model, question, context) {
    let result = query_model(model, question, context);
    let value = get(result, "value");
    return value;
}
```

Functions can have no parameters:

```
declare get_threshold as function() {
    return 0.9;
}
```

## Calling functions

Functions are called by name with arguments in parentheses:

```
let sum = add(3, 5);
let threshold = get_threshold();
let value = evaluate_model(my_model, "Is AI safe?", {"topic": "safety"});
```

Arguments are evaluated left-to-right and passed by value to the corresponding
parameters.

## Variable scope in functions

Each function call creates a new local scope. Variables assigned with `let` inside
a function body are local to that invocation and do not affect the global scope.
The local scope has access to global variables for reading, but writing creates a
local shadow.

```
let x = 10;

declare double_x as function() {
    let x = x * 2;  // local x, shadows global
    return x;
}

let result = double_x();  // 20
// global x is still 10
```

## Return values

Functions return a value in one of two ways:

1. **Explicit return**: Using a `return` statement.

    ```
    declare square as function(n) {
        return n * n;
    }
    ```

2. **Implicit return**: If no `return` statement is reached, the function returns
   the last value computed on the evaluation stack.

## Recursion

Functions can call themselves recursively:

```
declare factorial as function(n) {
    let result = n == 1 ? 1 : n * factorial(n - 1);
    return result;
}
```

## Built-in functions

AISL includes over 40 built-in functions for metrics, statistics, data
operations, and LLM queries. These are always available without declaration. See
the [Built-in Functions](built-ins/index.md) section for a complete reference.

Built-in functions are called with the same syntax as user-defined functions:

```
let avg = mean([1, 2, 3, 4, 5]);
let acc = accuracy(y_true, y_pred);
let parsed = parse_json(response_text);
```
