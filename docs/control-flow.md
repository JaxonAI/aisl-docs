# Control Flow

AISL provides a `for` loop for iteration and an `append` statement for building
up lists incrementally.

## For loops

The `for` loop iterates over an inclusive numeric range:

```
for START..END {
    // statements
}
```

Both `START` and `END` must be integer literals. The range is inclusive, meaning
the body executes `END - START + 1` times.

```
for 1..5 {
    // executes 5 times
}

for 0..9 {
    // executes 10 times
}
```

For loops are commonly used to query an LLM multiple times and collect responses:

```
let responses = [];

for 1..20 {
    let output = query_model(my_model, "Is AI beneficial?", {"topic": "ai"});
    append responses with output;
}
```

!!! note

    The loop index is not accessible as a variable inside the loop body. If you
    need a counter, maintain one manually using `let`.

## Append statement

The `append` statement adds a value to the end of a list:

```
append LIST_NAME with EXPRESSION;
```

If the variable does not exist yet, it is automatically created as an empty list
before the value is appended.

```
let results = [];
append results with "first";
append results with "second";
// results is ["first", "second"]
```

This is the primary way to build up collections during loop iterations:

```
let all_scores = [];

for 1..10 {
    let score = accuracy(ground_truth, predictions);
    append all_scores with score;
}
```

## Return statement

The `return` statement exits a function and provides its result value:

```
return EXPRESSION;
```

```
declare compute_mean as function(data) {
    let result = mean(data);
    return result;
}
```

If a function does not contain a `return` statement, it returns the last value
left on the evaluation stack.
