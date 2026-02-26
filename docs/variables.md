# Variables

Variables in AISL store values for use in expressions, function calls, and
declarations.

## Assignment

Variables are assigned using the `let` keyword:

```
let x = 42;
let name = "test_run";
let scores = [0.8, 0.9, 0.7];
let result = accuracy(y_true, y_pred);
```

The right-hand side is any valid expression, which is evaluated immediately and
the result is stored in the variable.

## Reassignment

Variables can be reassigned to new values:

```
let counter = 0;
let counter = counter + 1;
```

Each `let` statement evaluates the expression on the right and binds the result
to the identifier on the left.

## Scope

AISL has two scope levels:

- **Global scope**: Variables declared at the top level of a program are
  accessible throughout the entire program.
- **Function scope**: Variables declared inside a function body are local to that
  function. They shadow any global variables with the same name.

```
let x = 10;  // global

declare add_x as function(n) {
    let x = 5;       // local, shadows global x
    return n + x;    // uses local x (5)
}

let result = add_x(3);  // result is 8
// x is still 10 here
```

Variables assigned in `for` loops share the enclosing scope. Values persist
across iterations:

```
let total = 0;
for 1..3 {
    let total = total + 1;
}
// total is 3
```

## Declarations as variables

All `declare` statements create entries in the variable namespace. After
declaring a model, dataset, file, or performance block, the declared name can be
referenced as a variable:

```
declare my_model as model { model_name = "chat" }
// my_model is now a variable containing the model configuration

declare data as dataset { my_file, key = values }
// data is now a variable containing the loaded dataset
```
